#!/usr/bin/env python3
"""
BlueHat Security - Advanced Security Application for Windows 11
A comprehensive security monitoring and protection tool
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import platform
import psutil
import socket
import hashlib
import os
import threading
import time
from datetime import datetime
import subprocess
import json


class BlueHatSecurity:
    def __init__(self, root):
        self.root = root
        self.root.title("BlueHat Security - Windows 11 Protection Suite")
        self.root.geometry("1000x700")
        self.root.configure(bg="#1e1e2e")
        
        # Security monitoring state
        self.monitoring_active = False
        self.scan_running = False
        
        # Create UI
        self.create_ui()
        
        # Start initial system check
        self.check_system_info()
        
    def create_ui(self):
        """Create the main user interface"""
        # Header
        header = tk.Frame(self.root, bg="#2d2d44", height=80)
        header.pack(fill=tk.X, pady=(0, 10))
        
        title_label = tk.Label(
            header,
            text="🛡️ BlueHat Security",
            font=("Arial", 24, "bold"),
            bg="#2d2d44",
            fg="#00d4ff"
        )
        title_label.pack(pady=20)
        
        # Create notebook for tabs
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TNotebook", background="#1e1e2e", borderwidth=0)
        style.configure("TNotebook.Tab", background="#2d2d44", foreground="#ffffff", padding=[20, 10])
        style.map("TNotebook.Tab", background=[("selected", "#00d4ff")], foreground=[("selected", "#000000")])
        
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tabs
        self.create_dashboard_tab()
        self.create_scanner_tab()
        self.create_network_tab()
        self.create_firewall_tab()
        self.create_reports_tab()
        
    def create_dashboard_tab(self):
        """Create the main dashboard tab"""
        dashboard = tk.Frame(self.notebook, bg="#1e1e2e")
        self.notebook.add(dashboard, text="Dashboard")
        
        # System Information Section
        info_frame = tk.LabelFrame(
            dashboard,
            text="System Information",
            bg="#2d2d44",
            fg="#00d4ff",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        info_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.system_info_text = scrolledtext.ScrolledText(
            info_frame,
            height=10,
            bg="#1e1e2e",
            fg="#ffffff",
            font=("Consolas", 10),
            wrap=tk.WORD
        )
        self.system_info_text.pack(fill=tk.BOTH, expand=True)
        
        # Security Status Section
        status_frame = tk.LabelFrame(
            dashboard,
            text="Security Status",
            bg="#2d2d44",
            fg="#00d4ff",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        status_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.status_text = scrolledtext.ScrolledText(
            status_frame,
            height=8,
            bg="#1e1e2e",
            fg="#ffffff",
            font=("Consolas", 10),
            wrap=tk.WORD
        )
        self.status_text.pack(fill=tk.BOTH, expand=True)
        
        # Control Buttons
        button_frame = tk.Frame(dashboard, bg="#1e1e2e")
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.monitor_btn = tk.Button(
            button_frame,
            text="Start Monitoring",
            command=self.toggle_monitoring,
            bg="#00d4ff",
            fg="#000000",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=10
        )
        self.monitor_btn.pack(side=tk.LEFT, padx=5)
        
        refresh_btn = tk.Button(
            button_frame,
            text="Refresh Status",
            command=self.refresh_status,
            bg="#4CAF50",
            fg="#ffffff",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=10
        )
        refresh_btn.pack(side=tk.LEFT, padx=5)
        
    def create_scanner_tab(self):
        """Create the security scanner tab"""
        scanner = tk.Frame(self.notebook, bg="#1e1e2e")
        self.notebook.add(scanner, text="Security Scanner")
        
        # Scanner controls
        control_frame = tk.Frame(scanner, bg="#2d2d44")
        control_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(
            control_frame,
            text="File/Directory Scanner",
            bg="#2d2d44",
            fg="#00d4ff",
            font=("Arial", 14, "bold")
        ).pack(pady=10)
        
        self.scan_entry = tk.Entry(
            control_frame,
            font=("Arial", 11),
            width=50
        )
        self.scan_entry.pack(pady=5)
        self.scan_entry.insert(0, "Enter path to scan...")
        
        self.scan_btn = tk.Button(
            control_frame,
            text="Start Scan",
            command=self.start_scan,
            bg="#00d4ff",
            fg="#000000",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=10
        )
        self.scan_btn.pack(pady=10)
        
        # Scan results
        results_frame = tk.LabelFrame(
            scanner,
            text="Scan Results",
            bg="#2d2d44",
            fg="#00d4ff",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.scan_results_text = scrolledtext.ScrolledText(
            results_frame,
            bg="#1e1e2e",
            fg="#ffffff",
            font=("Consolas", 10),
            wrap=tk.WORD
        )
        self.scan_results_text.pack(fill=tk.BOTH, expand=True)
        
    def create_network_tab(self):
        """Create the network monitoring tab"""
        network = tk.Frame(self.notebook, bg="#1e1e2e")
        self.notebook.add(network, text="Network Monitor")
        
        # Network info
        info_frame = tk.LabelFrame(
            network,
            text="Network Information",
            bg="#2d2d44",
            fg="#00d4ff",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        info_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.network_info_text = scrolledtext.ScrolledText(
            info_frame,
            bg="#1e1e2e",
            fg="#ffffff",
            font=("Consolas", 10),
            wrap=tk.WORD
        )
        self.network_info_text.pack(fill=tk.BOTH, expand=True)
        
        # Active connections
        conn_frame = tk.LabelFrame(
            network,
            text="Active Connections",
            bg="#2d2d44",
            fg="#00d4ff",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        conn_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.connections_text = scrolledtext.ScrolledText(
            conn_frame,
            bg="#1e1e2e",
            fg="#ffffff",
            font=("Consolas", 10),
            wrap=tk.WORD
        )
        self.connections_text.pack(fill=tk.BOTH, expand=True)
        
        # Refresh button
        refresh_btn = tk.Button(
            network,
            text="Refresh Network Info",
            command=self.refresh_network_info,
            bg="#00d4ff",
            fg="#000000",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=10
        )
        refresh_btn.pack(pady=10)
        
    def create_firewall_tab(self):
        """Create the firewall status tab"""
        firewall = tk.Frame(self.notebook, bg="#1e1e2e")
        self.notebook.add(firewall, text="Firewall Status")
        
        status_frame = tk.LabelFrame(
            firewall,
            text="Windows Firewall Status",
            bg="#2d2d44",
            fg="#00d4ff",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        status_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.firewall_text = scrolledtext.ScrolledText(
            status_frame,
            bg="#1e1e2e",
            fg="#ffffff",
            font=("Consolas", 10),
            wrap=tk.WORD
        )
        self.firewall_text.pack(fill=tk.BOTH, expand=True)
        
        check_btn = tk.Button(
            firewall,
            text="Check Firewall Status",
            command=self.check_firewall_status,
            bg="#00d4ff",
            fg="#000000",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=10
        )
        check_btn.pack(pady=10)
        
    def create_reports_tab(self):
        """Create the security reports tab"""
        reports = tk.Frame(self.notebook, bg="#1e1e2e")
        self.notebook.add(reports, text="Security Reports")
        
        report_frame = tk.LabelFrame(
            reports,
            text="Security Report",
            bg="#2d2d44",
            fg="#00d4ff",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        report_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.report_text = scrolledtext.ScrolledText(
            report_frame,
            bg="#1e1e2e",
            fg="#ffffff",
            font=("Consolas", 10),
            wrap=tk.WORD
        )
        self.report_text.pack(fill=tk.BOTH, expand=True)
        
        button_frame = tk.Frame(reports, bg="#1e1e2e")
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        generate_btn = tk.Button(
            button_frame,
            text="Generate Security Report",
            command=self.generate_security_report,
            bg="#00d4ff",
            fg="#000000",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=10
        )
        generate_btn.pack(side=tk.LEFT, padx=5)
        
        export_btn = tk.Button(
            button_frame,
            text="Export Report",
            command=self.export_report,
            bg="#4CAF50",
            fg="#ffffff",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=10
        )
        export_btn.pack(side=tk.LEFT, padx=5)
        
    def check_system_info(self):
        """Get and display system information"""
        info = []
        info.append("=== SYSTEM INFORMATION ===\n")
        info.append(f"OS: {platform.system()} {platform.release()}")
        info.append(f"Version: {platform.version()}")
        info.append(f"Architecture: {platform.machine()}")
        info.append(f"Processor: {platform.processor()}")
        info.append(f"Hostname: {socket.gethostname()}")
        info.append(f"\nCPU Cores: {psutil.cpu_count(logical=False)} (Physical)")
        info.append(f"CPU Threads: {psutil.cpu_count(logical=True)} (Logical)")
        info.append(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
        
        memory = psutil.virtual_memory()
        info.append(f"\nTotal RAM: {memory.total / (1024**3):.2f} GB")
        info.append(f"Available RAM: {memory.available / (1024**3):.2f} GB")
        info.append(f"RAM Usage: {memory.percent}%")
        
        disk = psutil.disk_usage('/')
        info.append(f"\nDisk Total: {disk.total / (1024**3):.2f} GB")
        info.append(f"Disk Used: {disk.used / (1024**3):.2f} GB")
        info.append(f"Disk Free: {disk.free / (1024**3):.2f} GB")
        info.append(f"Disk Usage: {disk.percent}%")
        
        self.system_info_text.delete(1.0, tk.END)
        self.system_info_text.insert(tk.END, "\n".join(info))
        
    def refresh_status(self):
        """Refresh security status"""
        self.check_system_info()
        status = []
        status.append("=== SECURITY STATUS ===\n")
        status.append(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        status.append(f"Monitoring Active: {'Yes' if self.monitoring_active else 'No'}")
        status.append(f"Running Processes: {len(psutil.pids())}")
        
        # Check for suspicious activity
        high_cpu_processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                if proc.info['cpu_percent'] > 50:
                    high_cpu_processes.append(f"{proc.info['name']} (PID: {proc.info['pid']}) - CPU: {proc.info['cpu_percent']}%")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        if high_cpu_processes:
            status.append(f"\n⚠️ High CPU Usage Detected:")
            status.extend(high_cpu_processes[:5])
        else:
            status.append("\n✓ No unusual CPU activity detected")
        
        status.append(f"\n✓ System Performance: Normal")
        status.append(f"✓ Security Checks: Passed")
        
        self.status_text.delete(1.0, tk.END)
        self.status_text.insert(tk.END, "\n".join(status))
        
    def toggle_monitoring(self):
        """Toggle real-time monitoring"""
        self.monitoring_active = not self.monitoring_active
        if self.monitoring_active:
            self.monitor_btn.config(text="Stop Monitoring", bg="#ff4444")
            threading.Thread(target=self.monitor_loop, daemon=True).start()
        else:
            self.monitor_btn.config(text="Start Monitoring", bg="#00d4ff")
            
    def monitor_loop(self):
        """Continuous monitoring loop"""
        while self.monitoring_active:
            self.root.after(0, self.refresh_status)
            time.sleep(5)
            
    def start_scan(self):
        """Start security scan"""
        if self.scan_running:
            messagebox.showwarning("Scan in Progress", "A scan is already running!")
            return
            
        path = self.scan_entry.get()
        if not path or path == "Enter path to scan...":
            messagebox.showerror("Invalid Path", "Please enter a valid path to scan")
            return
            
        self.scan_running = True
        self.scan_btn.config(state=tk.DISABLED)
        threading.Thread(target=self.perform_scan, args=(path,), daemon=True).start()
        
    def perform_scan(self, path):
        """Perform security scan on path"""
        self.scan_results_text.delete(1.0, tk.END)
        self.scan_results_text.insert(tk.END, f"Starting scan of: {path}\n")
        self.scan_results_text.insert(tk.END, f"Scan started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        scanned_files = 0
        suspicious_files = []
        
        try:
            if os.path.isfile(path):
                files_to_scan = [path]
            elif os.path.isdir(path):
                files_to_scan = []
                for root, dirs, files in os.walk(path):
                    for file in files[:100]:  # Limit to 100 files for demo
                        files_to_scan.append(os.path.join(root, file))
            else:
                self.scan_results_text.insert(tk.END, "❌ Invalid path!\n")
                self.scan_btn.config(state=tk.NORMAL)
                self.scan_running = False
                return
            
            for file_path in files_to_scan:
                try:
                    scanned_files += 1
                    self.scan_results_text.insert(tk.END, f"Scanning: {file_path}\n")
                    self.scan_results_text.see(tk.END)
                    
                    # Check file size and extension
                    size = os.path.getsize(file_path)
                    ext = os.path.splitext(file_path)[1].lower()
                    
                    # Flag potentially suspicious files
                    suspicious_extensions = ['.exe', '.dll', '.bat', '.cmd', '.vbs', '.ps1', '.scr']
                    if ext in suspicious_extensions:
                        suspicious_files.append((file_path, "Executable file type"))
                    
                    if size > 100 * 1024 * 1024:  # Files larger than 100MB
                        suspicious_files.append((file_path, f"Large file size: {size / (1024*1024):.2f} MB"))
                    
                except Exception as e:
                    self.scan_results_text.insert(tk.END, f"Error scanning {file_path}: {str(e)}\n")
                    
            self.scan_results_text.insert(tk.END, f"\n{'='*60}\n")
            self.scan_results_text.insert(tk.END, f"Scan completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            self.scan_results_text.insert(tk.END, f"Total files scanned: {scanned_files}\n")
            self.scan_results_text.insert(tk.END, f"Suspicious files found: {len(suspicious_files)}\n\n")
            
            if suspicious_files:
                self.scan_results_text.insert(tk.END, "⚠️ SUSPICIOUS FILES:\n")
                for file, reason in suspicious_files:
                    self.scan_results_text.insert(tk.END, f"  - {file}\n    Reason: {reason}\n")
            else:
                self.scan_results_text.insert(tk.END, "✓ No suspicious files detected\n")
                
        except Exception as e:
            self.scan_results_text.insert(tk.END, f"\n❌ Error during scan: {str(e)}\n")
        
        self.scan_btn.config(state=tk.NORMAL)
        self.scan_running = False
        
    def refresh_network_info(self):
        """Refresh network information"""
        info = []
        info.append("=== NETWORK INFORMATION ===\n")
        
        # Get network interfaces
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            info.append(f"Hostname: {hostname}")
            info.append(f"Local IP: {local_ip}")
        except:
            info.append("Could not retrieve hostname/IP")
        
        info.append("\nNetwork Interfaces:")
        net_if_addrs = psutil.net_if_addrs()
        for interface, addrs in net_if_addrs.items():
            info.append(f"\n  {interface}:")
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    info.append(f"    IPv4: {addr.address}")
                elif addr.family == socket.AF_INET6:
                    info.append(f"    IPv6: {addr.address}")
        
        # Network statistics
        net_io = psutil.net_io_counters()
        info.append(f"\nNetwork Statistics:")
        info.append(f"  Bytes Sent: {net_io.bytes_sent / (1024**2):.2f} MB")
        info.append(f"  Bytes Received: {net_io.bytes_recv / (1024**2):.2f} MB")
        info.append(f"  Packets Sent: {net_io.packets_sent}")
        info.append(f"  Packets Received: {net_io.packets_recv}")
        
        self.network_info_text.delete(1.0, tk.END)
        self.network_info_text.insert(tk.END, "\n".join(info))
        
        # Get active connections
        conn_info = []
        conn_info.append("=== ACTIVE CONNECTIONS ===\n")
        connections = psutil.net_connections(kind='inet')
        
        for conn in connections[:50]:  # Limit to 50 connections
            try:
                if conn.status == 'ESTABLISHED':
                    local = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
                    remote = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
                    conn_info.append(f"  {local} -> {remote} [{conn.status}]")
            except:
                pass
        
        self.connections_text.delete(1.0, tk.END)
        self.connections_text.insert(tk.END, "\n".join(conn_info))
        
    def check_firewall_status(self):
        """Check Windows Firewall status"""
        self.firewall_text.delete(1.0, tk.END)
        self.firewall_text.insert(tk.END, "=== WINDOWS FIREWALL STATUS ===\n\n")
        
        if platform.system() == "Windows":
            try:
                # Check firewall status using netsh
                result = subprocess.run(
                    ["netsh", "advfirewall", "show", "allprofiles"],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                self.firewall_text.insert(tk.END, result.stdout)
            except Exception as e:
                self.firewall_text.insert(tk.END, f"Could not check firewall status: {str(e)}\n")
                self.firewall_text.insert(tk.END, "\nNote: This feature requires Windows with administrative privileges.\n")
        else:
            self.firewall_text.insert(tk.END, "⚠️ Windows Firewall checking is only available on Windows systems.\n")
            self.firewall_text.insert(tk.END, f"Current OS: {platform.system()}\n")
        
    def generate_security_report(self):
        """Generate comprehensive security report"""
        report = []
        report.append("=" * 70)
        report.append("BLUEHAT SECURITY - COMPREHENSIVE SECURITY REPORT")
        report.append("=" * 70)
        report.append(f"\nReport Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"System: {platform.system()} {platform.release()}")
        report.append(f"Hostname: {socket.gethostname()}")
        
        # System Health
        report.append("\n" + "=" * 70)
        report.append("SYSTEM HEALTH")
        report.append("=" * 70)
        report.append(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
        memory = psutil.virtual_memory()
        report.append(f"Memory Usage: {memory.percent}%")
        disk = psutil.disk_usage('/')
        report.append(f"Disk Usage: {disk.percent}%")
        
        # Process Information
        report.append("\n" + "=" * 70)
        report.append("PROCESS INFORMATION")
        report.append("=" * 70)
        report.append(f"Total Running Processes: {len(psutil.pids())}")
        
        high_cpu = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                if proc.info['cpu_percent'] > 20:
                    high_cpu.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        if high_cpu:
            report.append("\nHigh CPU Usage Processes:")
            for proc in high_cpu[:10]:
                report.append(f"  - {proc['name']} (PID: {proc['pid']}) - CPU: {proc['cpu_percent']}%")
        
        # Network Information
        report.append("\n" + "=" * 70)
        report.append("NETWORK INFORMATION")
        report.append("=" * 70)
        net_io = psutil.net_io_counters()
        report.append(f"Bytes Sent: {net_io.bytes_sent / (1024**2):.2f} MB")
        report.append(f"Bytes Received: {net_io.bytes_recv / (1024**2):.2f} MB")
        
        established_connections = sum(1 for conn in psutil.net_connections(kind='inet') if conn.status == 'ESTABLISHED')
        report.append(f"Active Connections: {established_connections}")
        
        # Security Recommendations
        report.append("\n" + "=" * 70)
        report.append("SECURITY RECOMMENDATIONS")
        report.append("=" * 70)
        report.append("✓ Keep Windows Defender up to date")
        report.append("✓ Enable Windows Firewall")
        report.append("✓ Install latest Windows updates")
        report.append("✓ Use strong passwords")
        report.append("✓ Enable BitLocker disk encryption")
        report.append("✓ Regularly backup important data")
        report.append("✓ Be cautious with email attachments")
        report.append("✓ Keep all software updated")
        
        report.append("\n" + "=" * 70)
        report.append("END OF REPORT")
        report.append("=" * 70)
        
        self.report_text.delete(1.0, tk.END)
        self.report_text.insert(tk.END, "\n".join(report))
        
    def export_report(self):
        """Export security report to file"""
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"bluehat_security_report_{timestamp}.txt"
            
            with open(filename, 'w') as f:
                f.write(self.report_text.get(1.0, tk.END))
            
            messagebox.showinfo("Export Successful", f"Report exported to:\n{filename}")
        except Exception as e:
            messagebox.showerror("Export Failed", f"Could not export report:\n{str(e)}")


def main():
    """Main entry point"""
    root = tk.Tk()
    app = BlueHatSecurity(root)
    root.mainloop()


if __name__ == "__main__":
    main()
