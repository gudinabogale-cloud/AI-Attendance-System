Write-Host "AI Attendance System - Setup" -ForegroundColor Cyan
Write-Host ""

Write-Host "Checking Python..." -ForegroundColor Yellow
python --version

Write-Host ""
Write-Host "Creating virtual environment..." -ForegroundColor Yellow
python -m venv venv

Write-Host ""
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
.\venv\Scripts\Activate.ps1

Write-Host ""
Write-Host "Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

Write-Host ""
Write-Host "Installing dependencies (this will take time)..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host ""
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "Run: python app.py" -ForegroundColor Cyan
pause
