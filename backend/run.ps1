# AI Attendance System - Run Script (PowerShell)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  AI Attendance System - Starting..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
if (-not (Test-Path ".\venv\Scripts\Activate.ps1")) {
    Write-Host "✗ Virtual environment not found!" -ForegroundColor Red
    Write-Host "Please run setup.ps1 first" -ForegroundColor Yellow
    Write-Host ""
    pause
    exit 1
}

Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

Write-Host "✓ Environment activated" -ForegroundColor Green
Write-Host ""

# Check if requirements are installed
Write-Host "Checking dependencies..." -ForegroundColor Yellow
$flaskInstalled = pip list | Select-String "Flask"

if (-not $flaskInstalled) {
    Write-Host "⚠ Dependencies not installed. Installing now..." -ForegroundColor Yellow
    pip install -r requirements.txt
    Write-Host ""
}

Write-Host "========================================" -ForegroundColor Green
Write-Host "  Starting Flask Server..." -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "  Access the application at:" -ForegroundColor Cyan
Write-Host "  → http://localhost:5000" -ForegroundColor White
Write-Host ""
Write-Host "  Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

# Run the Flask application using the virtual environment's Python
.\venv\Scripts\python.exe app.py

Write-Host ""
Write-Host "Server stopped." -ForegroundColor Yellow
pause
