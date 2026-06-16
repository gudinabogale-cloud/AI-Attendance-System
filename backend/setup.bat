@echo off
echo ========================================
echo  AI Attendance System - Setup
echo ========================================
echo.

echo Creating virtual environment...
python -m venv venv

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ========================================
echo  Setup Complete!
echo  Run 'run.bat' to start the server
echo ========================================
echo.

pause
