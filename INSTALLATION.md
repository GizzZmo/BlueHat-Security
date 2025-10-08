# BlueHat Security - Installation Guide

## Quick Start for Windows 11

### Method 1: Simple Installation (Recommended)

1. **Download the repository**
   - Click the green "Code" button on GitHub
   - Select "Download ZIP"
   - Extract the ZIP file to a folder (e.g., `C:\BlueHat-Security`)

2. **Install Python**
   - Download Python 3.11 or later from [python.org](https://www.python.org/downloads/)
   - During installation, **check "Add Python to PATH"**
   - Click "Install Now"

3. **Run the launcher**
   - Double-click `launch.bat` in the BlueHat-Security folder
   - The launcher will automatically install dependencies and start the application

### Method 2: Manual Installation

1. **Install Python**
   - Download and install Python 3.11+ from [python.org](https://www.python.org/downloads/)
   - Ensure "Add Python to PATH" is checked during installation

2. **Open Command Prompt**
   - Press `Win + R`
   - Type `cmd` and press Enter

3. **Navigate to the BlueHat-Security folder**
   ```cmd
   cd C:\Path\To\BlueHat-Security
   ```

4. **Install dependencies**
   ```cmd
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```cmd
   python bluehat_security.py
   ```

### Method 3: Using Virtual Environment (For Developers)

1. **Open Command Prompt as Administrator**
   - Right-click Command Prompt
   - Select "Run as administrator"

2. **Navigate to the project folder**
   ```cmd
   cd C:\Path\To\BlueHat-Security
   ```

3. **Create a virtual environment**
   ```cmd
   python -m venv venv
   ```

4. **Activate the virtual environment**
   ```cmd
   venv\Scripts\activate
   ```

5. **Install dependencies**
   ```cmd
   pip install -r requirements.txt
   ```

6. **Run the application**
   ```cmd
   python bluehat_security.py
   ```

## System Requirements

### Minimum Requirements
- **OS**: Windows 11 or Windows 10 (64-bit)
- **Python**: 3.7 or higher
- **RAM**: 4 GB
- **Disk Space**: 100 MB free space
- **Display**: 1024x768 or higher resolution

### Recommended Requirements
- **OS**: Windows 11 (latest updates)
- **Python**: 3.11 or higher
- **RAM**: 8 GB or more
- **Disk Space**: 500 MB free space
- **Display**: 1920x1080 or higher resolution

## Verifying Installation

After installation, verify that everything is working:

1. **Check Python installation**
   ```cmd
   python --version
   ```
   Should display: `Python 3.x.x`

2. **Check dependencies**
   ```cmd
   pip list | findstr psutil
   ```
   Should show psutil version

3. **Run the test script**
   ```cmd
   python test_bluehat.py
   ```
   Should pass all core tests (GUI test may fail in headless environments)

## Troubleshooting

### Python not recognized
**Problem**: `'python' is not recognized as an internal or external command`

**Solution**:
1. Reinstall Python and check "Add Python to PATH"
2. Or manually add Python to PATH:
   - Search for "Environment Variables" in Windows
   - Edit "Path" in System Variables
   - Add Python installation directory (e.g., `C:\Python311`)

### pip not recognized
**Problem**: `'pip' is not recognized as an internal or external command`

**Solution**:
```cmd
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

### tkinter errors
**Problem**: `ModuleNotFoundError: No module named 'tkinter'`

**Solution**:
- Tkinter comes with Python on Windows
- Reinstall Python and ensure "tcl/tk and IDLE" is selected during installation

### Permission errors for Firewall Status
**Problem**: Cannot check firewall status

**Solution**:
1. Close the application
2. Right-click on `launch.bat`
3. Select "Run as administrator"

### Application crashes on startup
**Problem**: Application closes immediately

**Solution**:
1. Run from Command Prompt to see error messages:
   ```cmd
   python bluehat_security.py
   ```
2. Check that all dependencies are installed:
   ```cmd
   pip install -r requirements.txt
   ```

## Uninstallation

To remove BlueHat Security:

1. **Delete the application folder**
   - Simply delete the BlueHat-Security folder

2. **Remove Python packages (optional)**
   ```cmd
   pip uninstall psutil
   ```

3. **Remove Python (optional)**
   - Use Windows "Add or Remove Programs"
   - Search for Python and uninstall

## Advanced Configuration

### Running on Startup

To run BlueHat Security when Windows starts:

1. Press `Win + R`
2. Type `shell:startup` and press Enter
3. Create a shortcut to `launch.bat` in the Startup folder

### Creating a Desktop Shortcut

1. Right-click on `launch.bat`
2. Select "Send to" > "Desktop (create shortcut)"
3. Rename the shortcut to "BlueHat Security"

### Running as Administrator by Default

1. Right-click `launch.bat`
2. Select "Properties"
3. Click "Advanced"
4. Check "Run as administrator"
5. Click OK

## Getting Help

If you encounter issues:

1. Check the [Troubleshooting](#troubleshooting) section
2. Review the [README.md](README.md) documentation
3. Run the test script: `python test_bluehat.py`
4. Open an issue on GitHub with:
   - Error messages
   - Python version (`python --version`)
   - Windows version
   - Steps to reproduce the issue

## Next Steps

After successful installation:

1. Read the [Usage Guide](README.md#usage-guide) in README.md
2. Explore each tab in the application
3. Generate a security report to familiarize yourself with the interface
4. Enable real-time monitoring for continuous protection

---

**Enjoy using BlueHat Security!** 🛡️
