# Quick Start Guide - BlueHat Security

Get BlueHat Security up and running in 3 simple steps!

## Prerequisites

- Windows 11 (or Windows 10)
- Internet connection for downloading Python (if not installed)

## Step 1: Install Python

If you don't have Python installed:

1. Visit [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.11 or later
3. Run the installer
4. ⚠️ **IMPORTANT**: Check "Add Python to PATH" during installation
5. Click "Install Now"

To verify Python is installed:
```cmd
python --version
```

## Step 2: Download BlueHat Security

Choose one option:

### Option A: Download ZIP (Easiest)
1. Go to [github.com/GizzZmo/BlueHat-Security](https://github.com/GizzZmo/BlueHat-Security)
2. Click the green "Code" button
3. Click "Download ZIP"
4. Extract the ZIP file to a folder (e.g., `C:\BlueHat-Security`)

### Option B: Clone with Git
```bash
git clone https://github.com/GizzZmo/BlueHat-Security.git
cd BlueHat-Security
```

## Step 3: Run BlueHat Security

### Windows (Easiest Way)
1. Navigate to the BlueHat-Security folder
2. Double-click `launch.bat`
3. The application will start automatically!

### Alternative: Command Line
```cmd
cd C:\Path\To\BlueHat-Security
pip install -r requirements.txt
python bluehat_security.py
```

## What's Next?

### Explore the Dashboard
- View your system information
- Click "Start Monitoring" for real-time security monitoring
- Check the security status of your system

### Try the Scanner
1. Go to the "Security Scanner" tab
2. Enter a path (e.g., `C:\Users\YourName\Downloads`)
3. Click "Start Scan"
4. Review the results

### Check Your Network
1. Go to the "Network Monitor" tab
2. Click "Refresh Network Info"
3. View your active connections and network statistics

### View Firewall Status
1. Go to the "Firewall Status" tab
2. Click "Check Firewall Status"
3. Note: Requires running as Administrator for full details

### Generate Reports
1. Go to the "Security Reports" tab
2. Click "Generate Security Report"
3. Review the comprehensive security analysis
4. Click "Export Report" to save it

## Troubleshooting

### "Python is not recognized"
- Reinstall Python and ensure "Add Python to PATH" is checked
- Or add Python to PATH manually:
  1. Search "Environment Variables" in Windows
  2. Edit "Path" variable
  3. Add your Python installation path

### Application won't start
- Open Command Prompt in the BlueHat-Security folder
- Run: `pip install -r requirements.txt`
- Run: `python bluehat_security.py`
- Check for error messages

### Need Administrator Rights
For full firewall checking:
1. Right-click `launch.bat`
2. Select "Run as administrator"

## Tips

### Create a Desktop Shortcut
1. Right-click `launch.bat`
2. Select "Send to" → "Desktop (create shortcut)"
3. Rename to "BlueHat Security"

### Run on Startup
1. Press `Win + R`
2. Type `shell:startup` and press Enter
3. Copy/create a shortcut to `launch.bat` in this folder

### First-Time Recommendations
1. Generate a security report to establish a baseline
2. Enable monitoring and let it run for a few minutes
3. Scan your Downloads folder
4. Check your firewall status
5. Review network connections

## Getting Help

- **Documentation**: Read [README.md](README.md) for detailed information
- **Installation**: See [INSTALLATION.md](INSTALLATION.md) for detailed setup
- **Features**: Check [FEATURES.md](FEATURES.md) for all capabilities
- **Issues**: Report bugs on GitHub

## Demo Mode

Want to see what it does without the GUI?
```cmd
python demo.py
```

This runs a command-line demo showing all features.

## Testing

Verify everything works:
```cmd
python test_bluehat.py
```

---

**You're all set!** Enjoy using BlueHat Security! 🛡️

For detailed documentation, see:
- [README.md](README.md) - Full documentation
- [INSTALLATION.md](INSTALLATION.md) - Detailed installation guide
- [FEATURES.md](FEATURES.md) - Complete feature list
- [SCREENSHOTS.md](SCREENSHOTS.md) - UI reference
