# 🎓 AI-Based Attendance System

A complete face recognition-based attendance system using Flask and OpenCV.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 👤 **Student Registration** - Capture and train face images
- 📸 **Real-time Face Recognition** - LBPH algorithm for accurate detection
- ✅ **Automated Attendance** - One-click attendance marking
- 📊 **Reports & Analytics** - View statistics and trends
- 💾 **CSV Export** - Daily attendance records
- 🎨 **Modern UI** - Clean and responsive interface

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Webcam (for face capture)
- Modern browser (Chrome, Firefox, or Edge)

### Installation

#### For Windows (PowerShell):

```powershell
cd backend
.\setup_new.ps1
```

#### For Windows (CMD):

```cmd
cd backend
setup.bat
```

#### Manual Installation:

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Run the Application

```bash
cd backend
python app.py
```

Then open your browser and go to: **http://localhost:5000**

## 📖 Usage Guide

### 1. Register Students

1. Go to **Register Student** page
2. Enter student name
3. Click **Start Camera**
4. Click **Capture Image** 30-50 times
   - Try different angles and expressions
   - Ensure good lighting
5. Click **Train Model** when done

### 2. Mark Attendance

1. Go to **Mark Attendance** page
2. Click **Start Camera**
3. Position face in front of camera
4. Click **Mark Attendance**
5. System automatically recognizes and marks attendance

### 3. View Reports

1. Go to **Reports** page
2. Select date range
3. View attendance statistics and records

## 🏗️ Project Structure

```
AI_Attendance_System/
│
├── backend/
│   ├── app.py                    # Main Flask application
│   ├── requirements.txt          # Python dependencies
│   ├── setup.ps1                # PowerShell setup script
│   ├── setup.bat                # CMD setup script
│   ├── run.ps1                  # PowerShell run script
│   ├── run.bat                  # CMD run script
│   │
│   ├── dataset/                 # Training images
│   │   └── [student_name]/      # Per-student folders
│   │
│   ├── trainer/                 # Trained models
│   │   ├── trainer.yml          # LBPH model
│   │   └── labels.pkl           # Name-to-ID mapping
│   │
│   ├── attendance/              # Attendance records
│   │   └── attendance_YYYY-MM-DD.csv
│   │
│   └── templates/               # HTML templates
│       ├── index.html           # Dashboard
│       ├── register.html        # Registration
│       ├── attendance.html      # Mark attendance
│       └── reports.html         # Reports & analytics
│
├── QUICK_START.md               # Quick start guide
├── PROJECT_OVERVIEW.md          # Technical documentation
└── README.md                    # This file
```

## 🔧 Technology Stack

**Backend:**
- Python 3.8+
- Flask (Web Framework)
- OpenCV (Computer Vision)
- NumPy (Numerical Computing)
- Pandas (Data Processing)

**Frontend:**
- HTML5
- CSS3
- Vanilla JavaScript
- WebRTC (Camera Access)

**Machine Learning:**
- LBPH Face Recognizer
- Haar Cascade Classifier

## 📊 API Endpoints

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

## 💡 Tips for Best Results

1. **Image Capture**:
   - Capture 30-50 images per student
   - Use good, consistent lighting
   - Capture different angles (±15 degrees)
   - Include different expressions

2. **Recognition**:
   - Ensure proper lighting during attendance
   - Position face clearly in frame
   - Look directly at camera

3. **Training**:
   - Retrain model when adding new students
   - More training images = better accuracy

## 🐛 Troubleshooting

### Camera not working?
- Grant camera permissions in browser
- Check if camera is being used by another app

### Low recognition accuracy?
- Capture more training images (30-50 recommended)
- Ensure consistent lighting conditions
- Retrain the model

### "Model not found" error?
- Register at least one student first
- Click "Train Model" after capturing images

### Module import errors?
- Make sure virtual environment is activated
- Run `pip install -r requirements.txt`

## 🔒 Security & Privacy

- All data stored locally on your machine
- No cloud uploads or external APIs
- Camera access requires user permission
- Attendance records in standard CSV format

## 📈 Future Enhancements

- [ ] Database integration (SQLite/PostgreSQL)
- [ ] Multi-face detection in single frame
- [ ] Email notifications
- [ ] Export to Excel/PDF
- [ ] Mobile app
- [ ] Anti-spoofing (liveness detection)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Created with ❤️ using Python, Flask, and OpenCV

## 🙏 Acknowledgments

- OpenCV for computer vision capabilities
- Flask for the web framework
- The Python community for amazing libraries

## 📞 Support

For issues or questions:
1. Check the `QUICK_START.md` guide
2. Review `PROJECT_OVERVIEW.md` documentation
3. Create an issue in the repository

---

**Made with ❤️ for efficient attendance management**

⭐ Star this repo if you find it helpful!
