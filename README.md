# BlueHat-Security 🛡️

A comprehensive security monitoring and protection application for Windows 11. BlueHat Security provides real-time system monitoring, security scanning, network analysis, and firewall status checking to keep your Windows 11 system secure.

## Features

### 🎯 Dashboard
- **System Information**: Real-time CPU, memory, and disk usage monitoring
- **Security Status**: Active monitoring with suspicious activity detection
- **Process Monitoring**: Track running processes and identify high CPU usage
- **One-Click Refresh**: Instant security status updates

### 🔍 Security Scanner
- **File & Directory Scanning**: Scan individual files or entire directories
- **Threat Detection**: Identify potentially suspicious files
- **Real-time Results**: See scan progress and results instantly
- **Comprehensive Reports**: Detailed scan summaries with file analysis

### 🌐 Network Monitor
- **Network Interfaces**: View all network adapters and their configurations
- **Active Connections**: Monitor all active network connections
- **Traffic Statistics**: Track bytes sent/received and packet counts
- **IP Information**: Display hostname and local IP addresses

### 🔥 Firewall Status
- **Windows Firewall Checking**: Check the status of Windows Firewall profiles
- **Profile Information**: View Domain, Private, and Public profile settings
- **Security Recommendations**: Get firewall configuration suggestions

### 📊 Security Reports
- **Comprehensive Reporting**: Generate detailed security analysis reports
- **System Health Metrics**: CPU, memory, and disk usage analysis
- **Network Statistics**: Complete network activity summary
- **Export Functionality**: Save reports to text files for later review
- **Security Recommendations**: Best practices and security tips

## Screenshots

![BlueHat Security Dashboard](docs/screenshot.png)

## Requirements

- **Operating System**: Windows 11 (or Windows 10)
- **Python**: 3.7 or higher
- **Dependencies**: Listed in `requirements.txt`

## Installation

### Quick Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/GizzZmo/BlueHat-Security.git
   cd BlueHat-Security
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python bluehat_security.py
   ```

### Alternative: Create a Virtual Environment (Recommended)

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python bluehat_security.py
   ```

## Usage Guide

### Starting the Application

Simply run:
```bash
python bluehat_security.py
```

### Dashboard Tab
1. View real-time system information
2. Click "Start Monitoring" to enable continuous security monitoring
3. Click "Refresh Status" to update security status manually

### Security Scanner Tab
1. Enter a file path or directory path in the text field
2. Click "Start Scan" to begin scanning
3. Review the scan results for any suspicious files
4. Note: Executable files (.exe, .dll, .bat, etc.) are flagged for review

### Network Monitor Tab
1. Click "Refresh Network Info" to see current network status
2. View all network interfaces and their IP addresses
3. Monitor active network connections
4. Check network traffic statistics

### Firewall Status Tab
1. Click "Check Firewall Status" to view Windows Firewall settings
2. Review the status of Domain, Private, and Public profiles
3. Ensure firewall is enabled for maximum protection
4. **Note**: Requires administrative privileges on Windows

### Security Reports Tab
1. Click "Generate Security Report" to create a comprehensive report
2. Review system health, process information, and network statistics
3. Click "Export Report" to save the report to a text file
4. Reports are saved with timestamp: `bluehat_security_report_YYYYMMDD_HHMMSS.txt`

## Features in Detail

### Real-time Monitoring
BlueHat Security continuously monitors your system when monitoring is enabled:
- CPU usage per process
- Memory consumption
- Disk activity
- Network connections
- Suspicious process detection

### Security Scanning
The scanner performs multiple checks:
- File type analysis
- File size verification
- Extension checking for potentially dangerous file types
- Path traversal for directory scans
- Detailed reporting of findings

### Network Analysis
Comprehensive network monitoring includes:
- IPv4 and IPv6 address information
- Network interface details
- Active connection tracking
- Data transfer statistics
- Connection status monitoring

### Firewall Integration
Check your Windows Firewall status:
- Domain profile status
- Private profile status
- Public profile status
- Firewall state verification
- Security recommendations

## Security Best Practices

BlueHat Security recommends:

1. ✅ **Keep Windows Defender up to date**
2. ✅ **Enable Windows Firewall for all profiles**
3. ✅ **Install Windows updates regularly**
4. ✅ **Use strong, unique passwords**
5. ✅ **Enable BitLocker disk encryption**
6. ✅ **Perform regular backups**
7. ✅ **Be cautious with email attachments**
8. ✅ **Keep all software updated**
9. ✅ **Use two-factor authentication where possible**
10. ✅ **Regular security scans**

## Troubleshooting

### Application won't start
- Ensure Python 3.7+ is installed: `python --version`
- Install dependencies: `pip install -r requirements.txt`
- Check for error messages in the terminal

### Firewall status shows errors
- Run the application as Administrator (right-click → Run as administrator)
- Ensure Windows Firewall service is running
- Check if `netsh` command is available in your system

### Scanner not working
- Verify the path exists and is accessible
- Check file/folder permissions
- Try scanning a smaller directory first

### High CPU usage
- Stop real-time monitoring when not needed
- Reduce scan frequency
- Close other resource-intensive applications

## Technical Details

### Architecture
- **GUI Framework**: Tkinter (built-in with Python)
- **System Monitoring**: psutil library
- **Platform**: Cross-platform with Windows-specific features
- **Threading**: Asynchronous operations for responsive UI

### File Structure
```
BlueHat-Security/
├── bluehat_security.py    # Main application
├── requirements.txt       # Python dependencies
└── README.md             # Documentation
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available for educational and personal use.

## Disclaimer

⚠️ **Important**: BlueHat Security is designed as a security monitoring tool and educational project. It should not replace professional antivirus software or security solutions. Always use comprehensive security software and follow security best practices.

This tool:
- Provides monitoring and visibility into system security
- Helps identify potential security issues
- Offers security recommendations
- **Does NOT** remove malware or repair infected files
- **Does NOT** provide real-time virus protection
- **Does NOT** replace Windows Defender or professional antivirus

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the troubleshooting section

## Acknowledgments

- Built with Python and Tkinter
- Uses the psutil library for system monitoring
- Designed for Windows 11 security awareness

---

**Stay Secure! 🛡️**

*BlueHat Security - Your Windows 11 Security Companion*