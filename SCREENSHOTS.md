# BlueHat Security - Application Screenshots

## Main Interface

The BlueHat Security application features a modern, dark-themed interface optimized for Windows 11.

### Color Scheme
- **Background**: Dark navy (#1e1e2e)
- **Secondary**: Darker purple-grey (#2d2d44)
- **Accent**: Cyan blue (#00d4ff)
- **Text**: White (#ffffff)

### Application Window
- **Size**: 1000x700 pixels (resizable)
- **Title**: "BlueHat Security - Windows 11 Protection Suite"
- **Icon**: Shield emoji (🛡️)

## Tab Layout

### 1. Dashboard Tab
```
┌─────────────────────────────────────────────────────────┐
│  🛡️ BlueHat Security                                    │
├─────────────────────────────────────────────────────────┤
│ [Dashboard] [Scanner] [Network] [Firewall] [Reports]   │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌─ System Information ────────────────────────────┐   │
│  │ === SYSTEM INFORMATION ===                       │   │
│  │ OS: Windows 11                                   │   │
│  │ CPU Cores: 4 (Physical)                          │   │
│  │ CPU Usage: 15%                                   │   │
│  │ Total RAM: 16.00 GB                              │   │
│  │ RAM Usage: 45%                                   │   │
│  │ Disk Total: 512.00 GB                            │   │
│  │ Disk Usage: 60%                                  │   │
│  └─────────────────────────────────────────────────┘   │
│                                                          │
│  ┌─ Security Status ───────────────────────────────┐   │
│  │ === SECURITY STATUS ===                          │   │
│  │ Last Updated: 2025-10-08 13:22:16                │   │
│  │ Monitoring Active: Yes                           │   │
│  │ Running Processes: 145                           │   │
│  │ ✓ No unusual CPU activity detected               │   │
│  │ ✓ System Performance: Normal                     │   │
│  │ ✓ Security Checks: Passed                        │   │
│  └─────────────────────────────────────────────────┘   │
│                                                          │
│  [ Start Monitoring ]  [ Refresh Status ]               │
└─────────────────────────────────────────────────────────┘
```

### 2. Security Scanner Tab
```
┌─────────────────────────────────────────────────────────┐
│  [Dashboard] [Scanner] [Network] [Firewall] [Reports]  │
├─────────────────────────────────────────────────────────┤
│                                                          │
│           File/Directory Scanner                         │
│                                                          │
│  ┌────────────────────────────────────────────────┐    │
│  │ C:\Users\YourName\Documents                     │    │
│  └────────────────────────────────────────────────┘    │
│                                                          │
│              [ Start Scan ]                              │
│                                                          │
│  ┌─ Scan Results ──────────────────────────────────┐   │
│  │ Starting scan of: C:\Users\YourName\Documents    │   │
│  │ Scan started at: 2025-10-08 13:25:00             │   │
│  │                                                   │   │
│  │ Scanning: document1.pdf                           │   │
│  │ Scanning: report.xlsx                             │   │
│  │ Scanning: setup.exe                               │   │
│  │                                                   │   │
│  │ ===================================               │   │
│  │ Scan completed at: 2025-10-08 13:25:45            │   │
│  │ Total files scanned: 87                           │   │
│  │ Suspicious files found: 1                         │   │
│  │                                                   │   │
│  │ ⚠️ SUSPICIOUS FILES:                              │   │
│  │   - C:\...\setup.exe                             │   │
│  │     Reason: Executable file type                  │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### 3. Network Monitor Tab
```
┌─────────────────────────────────────────────────────────┐
│  [Dashboard] [Scanner] [Network] [Firewall] [Reports]  │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌─ Network Information ───────────────────────────┐   │
│  │ === NETWORK INFORMATION ===                      │   │
│  │ Hostname: DESKTOP-ABC123                         │   │
│  │ Local IP: 192.168.1.100                          │   │
│  │                                                   │   │
│  │ Network Interfaces:                               │   │
│  │   Ethernet:                                       │   │
│  │     IPv4: 192.168.1.100                          │   │
│  │   Wi-Fi:                                          │   │
│  │     IPv4: 192.168.1.101                          │   │
│  │                                                   │   │
│  │ Network Statistics:                               │   │
│  │   Bytes Sent: 1024.50 MB                         │   │
│  │   Bytes Received: 5123.75 MB                     │   │
│  │   Packets Sent: 45678                            │   │
│  │   Packets Received: 123456                       │   │
│  └─────────────────────────────────────────────────┘   │
│                                                          │
│  ┌─ Active Connections ────────────────────────────┐   │
│  │ === ACTIVE CONNECTIONS ===                       │   │
│  │   192.168.1.100:50234 -> 40.112.72.205:443       │   │
│  │   192.168.1.100:50235 -> 52.96.128.44:443        │   │
│  │   192.168.1.100:50236 -> 13.107.42.14:443        │   │
│  └─────────────────────────────────────────────────┘   │
│                                                          │
│            [ Refresh Network Info ]                      │
└─────────────────────────────────────────────────────────┘
```

### 4. Firewall Status Tab
```
┌─────────────────────────────────────────────────────────┐
│  [Dashboard] [Scanner] [Network] [Firewall] [Reports]  │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌─ Windows Firewall Status ───────────────────────┐   │
│  │ === WINDOWS FIREWALL STATUS ===                  │   │
│  │                                                   │   │
│  │ Domain Profile Settings:                          │   │
│  │   State: ON                                       │   │
│  │   Firewall Policy: BlockInbound,AllowOutbound    │   │
│  │                                                   │   │
│  │ Private Profile Settings:                         │   │
│  │   State: ON                                       │   │
│  │   Firewall Policy: BlockInbound,AllowOutbound    │   │
│  │                                                   │   │
│  │ Public Profile Settings:                          │   │
│  │   State: ON                                       │   │
│  │   Firewall Policy: BlockInbound,AllowOutbound    │   │
│  │                                                   │   │
│  │ ✓ All profiles are protected                     │   │
│  └─────────────────────────────────────────────────┘   │
│                                                          │
│           [ Check Firewall Status ]                      │
└─────────────────────────────────────────────────────────┘
```

### 5. Security Reports Tab
```
┌─────────────────────────────────────────────────────────┐
│  [Dashboard] [Scanner] [Network] [Firewall] [Reports]  │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌─ Security Report ───────────────────────────────┐   │
│  │ ================================================  │   │
│  │ BLUEHAT SECURITY - COMPREHENSIVE SECURITY REPORT │   │
│  │ ================================================  │   │
│  │ Report Generated: 2025-10-08 13:22:16            │   │
│  │ System: Windows 11                                │   │
│  │                                                   │   │
│  │ SYSTEM HEALTH                                     │   │
│  │ CPU Usage: 15%                                    │   │
│  │ Memory Usage: 45%                                 │   │
│  │ Disk Usage: 60%                                   │   │
│  │                                                   │   │
│  │ PROCESS INFORMATION                               │   │
│  │ Total Running Processes: 145                      │   │
│  │                                                   │   │
│  │ NETWORK INFORMATION                               │   │
│  │ Bytes Sent: 1024.50 MB                           │   │
│  │ Active Connections: 12                            │   │
│  │                                                   │   │
│  │ SECURITY RECOMMENDATIONS                          │   │
│  │ ✓ Keep Windows Defender up to date               │   │
│  │ ✓ Enable Windows Firewall                        │   │
│  │ ✓ Install latest Windows updates                 │   │
│  └─────────────────────────────────────────────────┘   │
│                                                          │
│  [ Generate Security Report ]  [ Export Report ]        │
└─────────────────────────────────────────────────────────┘
```

## Button Styles

### Primary Buttons (Cyan)
- Background: #00d4ff
- Text: Black
- Font: Arial 11pt Bold
- Example: "Start Monitoring", "Start Scan", "Generate Security Report"

### Secondary Buttons (Green)
- Background: #4CAF50
- Text: White
- Font: Arial 11pt Bold
- Example: "Refresh Status", "Export Report"

### Warning Buttons (Red)
- Background: #ff4444
- Text: White
- Font: Arial 11pt Bold
- Example: "Stop Monitoring" (when active)

## Text Areas

All scrolled text areas feature:
- Background: #1e1e2e (dark navy)
- Text Color: #ffffff (white)
- Font: Consolas 10pt (monospace)
- Line wrapping enabled
- Scrollbars when content exceeds visible area

## Status Indicators

- ✓ Green checkmarks indicate normal/good status
- ⚠️ Warning symbols indicate potential issues
- ❌ Red X indicates errors or problems

## Window Behavior

- Resizable window
- Minimum size: 800x600
- Tab navigation using keyboard (Tab key)
- Responsive layout adapts to window size
- Dark theme optimized for Windows 11

---

**Note**: The actual application uses tkinter for the GUI. On Windows 11, it integrates seamlessly with the native window manager and supports all Windows 11 visual features including:
- Rounded corners
- Shadow effects
- Snap layouts
- Dark mode compatibility
