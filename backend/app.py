from flask import Flask, render_template, request, jsonify, Response, send_file
from flask_cors import CORS
import cv2
import numpy as np
import os
from datetime import datetime
import pandas as pd
from pathlib import Path
import pickle

app = Flask(__name__)
CORS(app)

# Configuration
BASE_DIR = Path(__file__).parent
DATASET_DIR = BASE_DIR / 'dataset'
TRAINER_DIR = BASE_DIR / 'trainer'
ATTENDANCE_DIR = BASE_DIR / 'attendance'
STATIC_DIR = BASE_DIR / 'static'

# Create directories if they don't exist
for directory in [DATASET_DIR, TRAINER_DIR, ATTENDANCE_DIR, STATIC_DIR]:
    directory.mkdir(exist_ok=True)

# Face detection cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Global variables
camera = None
recognizer = None
label_names = {}

def load_recognizer():
    """Load trained face recognizer"""
    global recognizer, label_names
    recognizer_path = TRAINER_DIR / 'trainer.yml'
    labels_path = TRAINER_DIR / 'labels.pkl'
    
    if recognizer_path.exists() and labels_path.exists():
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(str(recognizer_path))
        with open(labels_path, 'rb') as f:
            label_names = pickle.load(f)
        return True
    return False

@app.route('/')
def index():
    """Main dashboard"""
    return render_template('index.html')

@app.route('/register')
def register_page():
    """Registration page"""
    return render_template('register.html')

@app.route('/attendance')
def attendance_page():
    """Attendance marking page"""
    return render_template('attendance.html')

@app.route('/reports')
def reports_page():
    """Reports page"""
    return render_template('reports.html')

@app.route('/api/students', methods=['GET'])
def get_students():
    """Get list of registered students"""
    students = []
    if DATASET_DIR.exists():
        for student_dir in DATASET_DIR.iterdir():
            if student_dir.is_dir():
                image_count = len(list(student_dir.glob('*.jpg')))
                students.append({
                    'name': student_dir.name,
                    'images': image_count
                })
    return jsonify(students)

@app.route('/api/register', methods=['POST'])
def register_student():
    """Register a new student"""
    data = request.json
    student_name = data.get('name', '').strip()
    
    if not student_name:
        return jsonify({'success': False, 'message': 'Name is required'}), 400
    
    student_dir = DATASET_DIR / student_name
    student_dir.mkdir(exist_ok=True)
    
    return jsonify({'success': True, 'message': f'Student {student_name} registered'})

@app.route('/api/capture/<student_name>', methods=['POST'])
def capture_images(student_name):
    """Capture face images for training"""
    student_dir = DATASET_DIR / student_name
    student_dir.mkdir(exist_ok=True)
    
    # Get existing image count
    existing_images = len(list(student_dir.glob('*.jpg')))
    
    # Get image data from request
    image_data = request.json.get('image')
    if not image_data:
        return jsonify({'success': False, 'message': 'No image data'}), 400
    
    # Decode base64 image
    import base64
    image_bytes = base64.b64decode(image_data.split(',')[1])
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Detect face
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) == 0:
        return jsonify({'success': False, 'message': 'No face detected'}), 400
    
    # Save the largest face
    largest_face = max(faces, key=lambda rect: rect[2] * rect[3])
    x, y, w, h = largest_face
    face_img = gray[y:y+h, x:x+w]
    
    # Save image
    image_path = student_dir / f'{existing_images + 1}.jpg'
    cv2.imwrite(str(image_path), face_img)
    
    return jsonify({
        'success': True, 
        'message': f'Image captured ({existing_images + 1})',
        'count': existing_images + 1
    })

@app.route('/api/train', methods=['POST'])
def train_model():
    """Train the face recognition model"""
    faces = []
    labels = []
    label_names = {}
    current_label = 0
    
    # Collect all face images
    for student_dir in DATASET_DIR.iterdir():
        if student_dir.is_dir():
            student_name = student_dir.name
            label_names[current_label] = student_name
            
            for image_path in student_dir.glob('*.jpg'):
                img = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    faces.append(img)
                    labels.append(current_label)
            
            current_label += 1
    
    if len(faces) == 0:
        return jsonify({'success': False, 'message': 'No training data found'}), 400
    
    # Train recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(labels))
    
    # Save trained model
    recognizer.write(str(TRAINER_DIR / 'trainer.yml'))
    with open(TRAINER_DIR / 'labels.pkl', 'wb') as f:
        pickle.dump(label_names, f)
    
    # Reload the recognizer
    load_recognizer()
    
    return jsonify({
        'success': True, 
        'message': f'Model trained with {len(set(labels))} students and {len(faces)} images'
    })

@app.route('/api/recognize', methods=['POST'])
def recognize_face():
    """Recognize face from image"""
    if not load_recognizer():
        return jsonify({'success': False, 'message': 'Model not trained'}), 400
    
    # Get image data
    image_data = request.json.get('image')
    if not image_data:
        return jsonify({'success': False, 'message': 'No image data'}), 400
    
    # Decode base64 image
    import base64
    image_bytes = base64.b64decode(image_data.split(',')[1])
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) == 0:
        return jsonify({'success': False, 'message': 'No face detected'}), 400
    
    recognized_students = []
    
    for (x, y, w, h) in faces:
        face_img = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(face_img)
        
        if confidence < 50:  # Good match
            student_name = label_names.get(label, 'Unknown')
            recognized_students.append({
                'name': student_name,
                'confidence': float(100 - confidence)
            })
    
    return jsonify({
        'success': True,
        'students': recognized_students
    })

@app.route('/api/mark-attendance', methods=['POST'])
def mark_attendance():
    """Mark attendance for recognized students"""
    if not load_recognizer():
        return jsonify({'success': False, 'message': 'Model not trained'}), 400
    
    # Get image data
    image_data = request.json.get('image')
    if not image_data:
        return jsonify({'success': False, 'message': 'No image data'}), 400
    
    # Decode base64 image
    import base64
    image_bytes = base64.b64decode(image_data.split(',')[1])
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) == 0:
        return jsonify({'success': False, 'message': 'No face detected'}), 400
    
    # Get today's attendance file
    today = datetime.now().strftime('%Y-%m-%d')
    attendance_file = ATTENDANCE_DIR / f'attendance_{today}.csv'
    
    # Load existing attendance
    if attendance_file.exists():
        df = pd.read_csv(attendance_file)
        marked_students = set(df['Name'].tolist())
    else:
        df = pd.DataFrame(columns=['Name', 'Time', 'Date'])
        marked_students = set()
    
    newly_marked = []
    
    for (x, y, w, h) in faces:
        face_img = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(face_img)
        
        if confidence < 50:  # Good match
            student_name = label_names.get(label, 'Unknown')
            
            if student_name not in marked_students:
                # Mark attendance
                current_time = datetime.now().strftime('%H:%M:%S')
                new_row = pd.DataFrame([{
                    'Name': student_name,
                    'Time': current_time,
                    'Date': today
                }])
                df = pd.concat([df, new_row], ignore_index=True)
                marked_students.add(student_name)
                newly_marked.append(student_name)
    
    # Save attendance
    df.to_csv(attendance_file, index=False)
    
    return jsonify({
        'success': True,
        'marked': newly_marked,
        'message': f'Attendance marked for {len(newly_marked)} student(s)'
    })

@app.route('/api/attendance-report', methods=['GET'])
def get_attendance_report():
    """Get attendance report for a date range"""
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    all_records = []
    
    for attendance_file in ATTENDANCE_DIR.glob('attendance_*.csv'):
        df = pd.read_csv(attendance_file)
        all_records.append(df)
    
    if not all_records:
        return jsonify({'records': []})
    
    combined_df = pd.concat(all_records, ignore_index=True)
    
    # Filter by date range if provided
    if start_date and end_date:
        combined_df = combined_df[
            (combined_df['Date'] >= start_date) & 
            (combined_df['Date'] <= end_date)
        ]
    
    records = combined_df.to_dict('records')
    return jsonify({'records': records})

@app.route('/api/attendance-stats', methods=['GET'])
def get_attendance_stats():
    """Get attendance statistics"""
    all_records = []
    
    for attendance_file in ATTENDANCE_DIR.glob('attendance_*.csv'):
        df = pd.read_csv(attendance_file)
        all_records.append(df)
    
    if not all_records:
        return jsonify({'stats': {}})
    
    combined_df = pd.concat(all_records, ignore_index=True)
    
    # Calculate stats
    total_days = combined_df['Date'].nunique()
    student_stats = combined_df.groupby('Name').size().to_dict()
    
    stats = {
        'total_days': total_days,
        'students': []
    }
    
    for name, count in student_stats.items():
        attendance_rate = (count / total_days * 100) if total_days > 0 else 0
        stats['students'].append({
            'name': name,
            'present_days': int(count),
            'attendance_rate': round(attendance_rate, 2)
        })
    
    return jsonify({'stats': stats})

if __name__ == '__main__':
    # Try to load existing recognizer
    load_recognizer()
    app.run(debug=True, host='0.0.0.0', port=5000)
