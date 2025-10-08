"""
BlueHat Security - Command Line Demo
Demonstrates core security features without GUI
"""

import platform
import psutil
import socket
from datetime import datetime

def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def demo_system_info():
    """Demonstrate system information gathering"""
    print_header("SYSTEM INFORMATION")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Hostname: {socket.gethostname()}")
    print(f"\nCPU Cores: {psutil.cpu_count(logical=False)} (Physical)")
    print(f"CPU Threads: {psutil.cpu_count(logical=True)} (Logical)")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    
    memory = psutil.virtual_memory()
    print(f"\nTotal RAM: {memory.total / (1024**3):.2f} GB")
    print(f"Available RAM: {memory.available / (1024**3):.2f} GB")
    print(f"RAM Usage: {memory.percent}%")
    
    disk = psutil.disk_usage('/')
    print(f"\nDisk Total: {disk.total / (1024**3):.2f} GB")
    print(f"Disk Used: {disk.used / (1024**3):.2f} GB")
    print(f"Disk Free: {disk.free / (1024**3):.2f} GB")
    print(f"Disk Usage: {disk.percent}%")

def demo_process_monitoring():
    """Demonstrate process monitoring"""
    print_header("PROCESS MONITORING")
    print(f"Total Running Processes: {len(psutil.pids())}")
    
    print("\nTop 5 CPU-consuming processes:")
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    # Sort by CPU usage
    processes.sort(key=lambda x: x['cpu_percent'] or 0, reverse=True)
    
    for i, proc in enumerate(processes[:5], 1):
        print(f"  {i}. {proc['name']} (PID: {proc['pid']}) - CPU: {proc['cpu_percent']}%")

def demo_network_info():
    """Demonstrate network monitoring"""
    print_header("NETWORK INFORMATION")
    
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(f"Hostname: {hostname}")
        print(f"Local IP: {local_ip}")
    except:
        print("Could not retrieve hostname/IP")
    
    print("\nNetwork Interfaces:")
    net_if_addrs = psutil.net_if_addrs()
    for interface, addrs in list(net_if_addrs.items())[:3]:  # Show first 3 interfaces
        print(f"\n  {interface}:")
        for addr in addrs:
            if addr.family == socket.AF_INET:
                print(f"    IPv4: {addr.address}")
    
    net_io = psutil.net_io_counters()
    print(f"\nNetwork Statistics:")
    print(f"  Bytes Sent: {net_io.bytes_sent / (1024**2):.2f} MB")
    print(f"  Bytes Received: {net_io.bytes_recv / (1024**2):.2f} MB")
    print(f"  Packets Sent: {net_io.packets_sent}")
    print(f"  Packets Received: {net_io.packets_recv}")
    
    # Count active connections
    connections = [c for c in psutil.net_connections(kind='inet') if c.status == 'ESTABLISHED']
    print(f"\nActive Connections: {len(connections)}")

def demo_security_report():
    """Demonstrate security report generation"""
    print_header("SECURITY REPORT")
    print(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"System: {platform.system()} {platform.release()}")
    
    print("\nSystem Health:")
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    print(f"  CPU Usage: {cpu_usage}% ", end="")
    print("✓ Normal" if cpu_usage < 80 else "⚠ High")
    
    print(f"  Memory Usage: {memory.percent}% ", end="")
    print("✓ Normal" if memory.percent < 80 else "⚠ High")
    
    print(f"  Disk Usage: {disk.percent}% ", end="")
    print("✓ Normal" if disk.percent < 90 else "⚠ High")
    
    print("\nSecurity Recommendations:")
    recommendations = [
        "✓ Keep Windows Defender up to date",
        "✓ Enable Windows Firewall",
        "✓ Install latest Windows updates",
        "✓ Use strong passwords",
        "✓ Enable BitLocker disk encryption",
        "✓ Regularly backup important data"
    ]
    for rec in recommendations:
        print(f"  {rec}")

def main():
    """Run the demo"""
    print("\n" + "=" * 70)
    print("  BLUEHAT SECURITY - COMMAND LINE DEMO")
    print("=" * 70)
    print(f"  This demo shows the core features without the GUI")
    print("  For the full experience, run: python bluehat_security.py")
    print("=" * 70)
    
    demo_system_info()
    demo_process_monitoring()
    demo_network_info()
    demo_security_report()
    
    print("\n" + "=" * 70)
    print("  Demo completed successfully!")
    print("  Run 'python bluehat_security.py' for the full GUI version")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
