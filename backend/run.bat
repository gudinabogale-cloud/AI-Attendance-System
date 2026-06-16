@echo off
echo ========================================
echo  AI Attendance System - Starting...
echo ========================================
echo.

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing/Updating dependencies...
pip install -r requirements.txt

echo.
echo ========================================
echo  Starting Flask Server...
echo  Access at: http://localhost:5000
echo ========================================
echo.

:: Use the virtual environment's Python to avoid interpreter mismatch
.\venv\Scripts\python.exe app.py

pause
