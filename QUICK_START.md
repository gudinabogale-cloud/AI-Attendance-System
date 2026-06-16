# 🚀 Quick Start Guide - AI Attendance System

## Installation & Setup

### Step 1: Install Dependencies

**For PowerShell Users (Windows):**
```powershell
cd backend
.\setup.ps1
```

**For CMD Users:**
```cmd
cd backend
setup.bat
```

**For Linux/Mac:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

This will:
- Create a virtual environment
- Install all required Python packages
- Setup the project structure

### Step 2: Start the Server

**For PowerShell Users (Windows):**
```powershell
cd backend
.\run.ps1
```

**For CMD Users:**
```cmd
cd backend
run.bat
```

**For Linux/Mac:**
```bash
cd backend
source venv/bin/activate
python app.py
```

The server will start at: **http://localhost:5000**

> **Note:** If you get "execution policy" error in PowerShell, see `POWERSHELL_INSTRUCTIONS.md`

---

## 📖 Usage Workflow

### 1️⃣ Register Students (First Time Setup)

1. Open browser and go to http://localhost:5000
2. Click **"Register Student"**
3. Enter student name (e.g., "John Doe")
4. Click **"Start Camera"**
5. Click **"Capture Image"** 30-50 times
   - Move your head slightly between captures
   - Try different expressions
   - Ensure good lighting
6. Click **"Train Model"** when done
7. Wait for training to complete

**Repeat for each student you want to register**

### 2️⃣ Mark Attendance

1. Go to **"Mark Attendance"**
2. Click **"Start Camera"**
3. Position face in front of camera
4. Click **"Mark Attendance"**
5. System will recognize and mark attendance
6. See real-time list of marked students on the right

### 3️⃣ View Reports

1. Go to **"Reports"**
2. Select date range
3. Click **"Generate Report"**
4. View:
   - Overall statistics
   - Per-student attendance rates
   - Detailed attendance records

---

## 📊 Dashboard Features

### Main Dashboard
- Total registered students
- Today's attendance count
- Average attendance rate

### Register Page
- Real-time camera feed
- Face detection
- Progress tracking
- Model training

### Attendance Page
- Live face recognition
- Auto-attendance marking
- Today's attendance list
- Real-time updates

### Reports Page
- Date range filtering
- Student-wise statistics
- Attendance rate color coding:
  - 🟢 Green: ≥75% (Good)
  - 🟡 Yellow: 50-74% (Average)
  - 🔴 Red: <50% (Poor)

---

## 🗂️ Data Storage

All data is stored locally:

- **Student Images**: `backend/dataset/[student_name]/`
- **Trained Model**: `backend/trainer/trainer.yml`
- **Attendance Records**: `backend/attendance/attendance_YYYY-MM-DD.csv`

---

## ⚙️ System Requirements

- **Python**: 3.8 or higher
- **Webcam**: Required for face capture
- **Browser**: Chrome, Firefox, or Edge (latest version)
- **OS**: Windows, macOS, or Linux

---

## 🔧 Troubleshooting

### Camera Not Working?
- Grant camera permissions in browser
- Close other apps using the camera
- Try refreshing the page

### Face Not Detected?
- Ensure good lighting
- Look directly at camera
- Move closer to camera

### Low Recognition Accuracy?
- Capture more training images (30-50 per student)
- Retrain the model
- Ensure consistent lighting

### "Model Not Trained" Error?
- Register at least one student first
- Click "Train Model" after capturing images
- Wait for training to complete

---

## 🎯 Tips for Best Results

1. **Registration Phase**:
   - Capture 30-50 images per student
   - Use natural, consistent lighting
   - Vary angles slightly (±15 degrees)
   - Include different expressions
   - No sunglasses or face coverings

2. **Attendance Phase**:
   - Same lighting conditions as registration
   - Face the camera directly
   - Stay still for 1-2 seconds
   - One person at a time

3. **General**:
   - Retrain model when adding new students
   - More training images = better accuracy
   - Keep camera lens clean

---

## 🔐 Security & Privacy

- All data stored locally on your machine
- No cloud uploads or external APIs
- Camera access requires user permission
- Attendance records in standard CSV format

---

## 📈 Advanced Features

### API Integration

The system provides REST APIs for integration:

```bash
# Get all students
GET http://localhost:5000/api/students

# Mark attendance (with base64 image)
POST http://localhost:5000/api/mark-attendance

# Get attendance report
GET http://localhost:5000/api/attendance-report?start_date=2024-01-01&end_date=2024-01-31
```

### Customization

Edit `app.py` to customize:
- Recognition confidence threshold
- Camera resolution
- Server port
- Data directories

---

## 🆘 Support

For issues:
1. Check the troubleshooting section above
2. Review `backend/README.md` for detailed docs
3. Check Python console for error messages

---

## ✅ Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created (`setup.bat`)
- [ ] Dependencies installed
- [ ] Server running (`run.bat`)
- [ ] Camera working in browser
- [ ] At least one student registered
- [ ] Model trained successfully
- [ ] Attendance marking tested

---

**Ready to go! 🎉**

Start with `run.bat` and open http://localhost:5000 in your browser!
