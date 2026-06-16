# 🎓 AI-Based Attendance System

A complete face recognition-based attendance system using Flask and OpenCV.

## Features

- 👤 **Student Registration** - Capture and train face images
- 📸 **Real-time Face Recognition** - Automatic attendance marking
- 📊 **Attendance Reports** - View statistics and analytics
- 💾 **CSV Export** - Daily attendance records
- 🎨 **Modern UI** - Clean and responsive interface

## Installation

### 1. Install Python Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## Usage Guide

### Step 1: Register Students

1. Go to **Register Student** page
2. Enter student name
3. Click **Start Camera**
4. Click **Capture Image** multiple times (30+ recommended)
   - Try different angles and expressions
   - Ensure good lighting
5. Click **Train Model** when done

### Step 2: Mark Attendance

1. Go to **Mark Attendance** page
2. Click **Start Camera**
3. Position face in front of camera
4. Click **Mark Attendance**
5. System will automatically recognize and mark attendance

### Step 3: View Reports

1. Go to **Reports** page
2. Select date range
3. View attendance statistics and records
4. Export data if needed

## API Endpoints

### Student Management
- `GET /api/students` - Get all registered students
- `POST /api/register` - Register new student
- `POST /api/capture/<name>` - Capture face image

### Training
- `POST /api/train` - Train face recognition model

### Attendance
- `POST /api/recognize` - Recognize face from image
- `POST /api/mark-attendance` - Mark attendance
- `GET /api/attendance-report` - Get attendance records
- `GET /api/attendance-stats` - Get attendance statistics

## Directory Structure

```
backend/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── dataset/              # Student face images
│   └── [student_name]/   # Individual student folders
├── trainer/              # Trained models
│   ├── trainer.yml       # LBPH model
│   └── labels.pkl        # Label mappings
├── attendance/           # Attendance CSV files
│   └── attendance_YYYY-MM-DD.csv
├── templates/            # HTML templates
│   ├── index.html
│   ├── register.html
│   ├── attendance.html
│   └── reports.html
└── static/              # Static assets
```

## Technical Details

### Face Recognition
- **Algorithm**: LBPH (Local Binary Patterns Histograms)
- **Detection**: Haar Cascade Classifier
- **Confidence Threshold**: 50 (adjustable)

### Technologies
- **Backend**: Flask (Python)
- **Computer Vision**: OpenCV
- **Face Recognition**: opencv-contrib-python
- **Data Processing**: Pandas, NumPy
- **Frontend**: HTML5, CSS3, JavaScript

## Configuration

Edit `app.py` to customize:

```python
# Confidence threshold (lower = stricter)
if confidence < 50:  # Default: 50

# Camera resolution
video: { width: 640, height: 480 }

# Server settings
app.run(debug=True, host='0.0.0.0', port=5000)
```

## Tips for Best Results

1. **Image Capture**:
   - Capture 30-50 images per student
   - Use good lighting
   - Capture different angles and expressions
   - Avoid obstructions (glasses, masks)

2. **Recognition**:
   - Ensure proper lighting during attendance
   - Position face clearly in frame
   - Look directly at camera

3. **Training**:
   - Retrain model when adding new students
   - More training images = better accuracy

## Troubleshooting

### Camera not working?
- Grant camera permissions in browser
- Check if camera is being used by another app

### Low recognition accuracy?
- Capture more training images
- Ensure consistent lighting conditions
- Retrain the model

### Model not found error?
- Register at least one student
- Click "Train Model" after capturing images

## Browser Compatibility

- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari
- ⚠️ Requires HTTPS or localhost for camera access

## Security Notes

- Camera access requires user permission
- Data stored locally on server
- No external API dependencies
- Attendance records in CSV format

## Future Enhancements

- [ ] Database integration (SQLite/PostgreSQL)
- [ ] Multi-face detection in single frame
- [ ] Email notifications
- [ ] Export to Excel/PDF
- [ ] Mobile app
- [ ] Cloud deployment
- [ ] Anti-spoofing (liveness detection)

## License

MIT License - Feel free to use and modify!

## Support

For issues or questions, please create an issue in the repository.

---

**Made with ❤️ using Python, Flask, and OpenCV**
