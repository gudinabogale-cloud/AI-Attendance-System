# 🚀 PowerShell Setup Instructions

## Quick Start for PowerShell Users

### Option 1: Run PowerShell Scripts (Recommended)

#### Step 1: Enable Script Execution (One-time)

Open PowerShell **as Administrator** and run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Step 2: Setup the Application
```powershell
cd c:\Users\gudin\Desktop\AI_Attendance_System\backend
.\setup.ps1
```

#### Step 3: Run the Application
```powershell
.\run.ps1
```

---

### Option 2: Use CMD Instead

#### Right-click on `.bat` files and select "Open with Command Prompt"

OR

#### Switch to CMD:
```powershell
# From PowerShell, type:
cmd

# Then run:
setup.bat
run.bat
```

---

### Option 3: Manual Installation (No Scripts)

```powershell
# Navigate to backend folder
cd c:\Users\gudin\Desktop\AI_Attendance_System\backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

---

## Opening Your Browser

After running the server, open:
```
http://localhost:5000
```

---

## Common Issues

### "Execution Policy" Error?

**Error Message:**
```
.\setup.ps1 cannot be loaded because running scripts is disabled on this system.
```

**Solution:**
Run PowerShell as Administrator and execute:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try again.

---

### "Python not found" Error?

**Solution:**
1. Install Python from: https://www.python.org/downloads/
2. During installation, check "Add Python to PATH"
3. Restart PowerShell
4. Try again

---

### Virtual Environment Already Exists?

If you need to recreate the virtual environment:
```powershell
# Remove old environment
Remove-Item -Recurse -Force venv

# Run setup again
.\setup.ps1
```

---

## Quick Reference

| Task | PowerShell Command | CMD Command |
|------|-------------------|-------------|
| Setup | `.\setup.ps1` | `setup.bat` |
| Run | `.\run.ps1` | `run.bat` |
| Test | `python test_installation.py` | Same |
| Activate venv | `.\venv\Scripts\Activate.ps1` | `venv\Scripts\activate.bat` |
| Stop server | `Ctrl + C` | `Ctrl + C` |

---

## File Structure

```
backend/
├── setup.ps1          # PowerShell setup script
├── run.ps1            # PowerShell run script
├── setup.bat          # CMD setup script
├── run.bat            # CMD run script
├── app.py             # Main application
└── requirements.txt   # Dependencies
```

Both PowerShell (`.ps1`) and CMD (`.bat`) scripts are provided!

---

## Verification

After setup, verify installation:
```powershell
python test_installation.py
```

This will check:
- ✓ Python version
- ✓ Required packages
- ✓ OpenCV face module
- ✓ Directory structure
- ✓ Camera access

---

## Next Steps

1. ✅ Run `.\setup.ps1` (one-time)
2. ✅ Run `.\run.ps1` (every time you want to start)
3. ✅ Open `http://localhost:5000` in browser
4. ✅ Register students and mark attendance!

---

**Need help?** Check the error messages in PowerShell - they usually indicate what's missing!
