@echo off
REM BlueHat Security Launcher for Windows
REM This script launches the BlueHat Security application

echo.
echo ========================================
echo   BlueHat Security - Launcher
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7 or higher from python.org
    pause
    exit /b 1
)

echo Checking Python version...
python --version

REM Check if dependencies are installed
echo.
echo Checking dependencies...
python -c "import psutil" >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
)

echo.
echo Starting BlueHat Security...
echo.
python bluehat_security.py

if errorlevel 1 (
    echo.
    echo ERROR: Application failed to start
    pause
    exit /b 1
)
