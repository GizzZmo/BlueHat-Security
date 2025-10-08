#!/bin/bash
# BlueHat Security Launcher for Linux/Mac
# This script launches the BlueHat Security application

echo ""
echo "========================================"
echo "  BlueHat Security - Launcher"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "ERROR: Python is not installed or not in PATH"
        echo "Please install Python 3.7 or higher"
        exit 1
    else
        PYTHON_CMD=python
    fi
else
    PYTHON_CMD=python3
fi

echo "Checking Python version..."
$PYTHON_CMD --version

# Check if dependencies are installed
echo ""
echo "Checking dependencies..."
if ! $PYTHON_CMD -c "import psutil" &> /dev/null; then
    echo "Installing dependencies..."
    $PYTHON_CMD -m pip install -r requirements.txt
fi

echo ""
echo "Starting BlueHat Security..."
echo ""
$PYTHON_CMD bluehat_security.py

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Application failed to start"
    exit 1
fi
