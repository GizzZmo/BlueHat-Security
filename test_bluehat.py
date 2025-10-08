#!/usr/bin/env python3
"""
Test script for BlueHat Security
Tests core functionality without GUI
"""

import sys
import platform
import socket
import psutil
from datetime import datetime

def test_system_info():
    """Test system information gathering"""
    print("Testing System Information...")
    try:
        assert platform.system() is not None
        assert platform.release() is not None
        assert socket.gethostname() is not None
        assert psutil.cpu_count() is not None
        assert psutil.virtual_memory() is not None
        assert psutil.disk_usage('/') is not None
        print("✓ System information test passed")
        return True
    except Exception as e:
        print(f"✗ System information test failed: {e}")
        return False

def test_network_info():
    """Test network information gathering"""
    print("\nTesting Network Information...")
    try:
        hostname = socket.gethostname()
        assert hostname is not None
        
        net_if_addrs = psutil.net_if_addrs()
        assert net_if_addrs is not None
        
        net_io = psutil.net_io_counters()
        assert net_io is not None
        
        print("✓ Network information test passed")
        return True
    except Exception as e:
        print(f"✗ Network information test failed: {e}")
        return False

def test_process_monitoring():
    """Test process monitoring"""
    print("\nTesting Process Monitoring...")
    try:
        pids = psutil.pids()
        assert len(pids) > 0
        
        # Test accessing a process
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            assert proc.info['pid'] is not None
            break  # Just test one process
        
        print("✓ Process monitoring test passed")
        return True
    except Exception as e:
        print(f"✗ Process monitoring test failed: {e}")
        return False

def test_file_operations():
    """Test file scanning capabilities"""
    print("\nTesting File Operations...")
    try:
        import os
        import tempfile
        
        # Create a temporary test file
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            test_file = f.name
            f.write("Test content for BlueHat Security")
        
        # Test file operations
        assert os.path.exists(test_file)
        assert os.path.isfile(test_file)
        size = os.path.getsize(test_file)
        assert size > 0
        
        # Clean up
        os.remove(test_file)
        
        print("✓ File operations test passed")
        return True
    except Exception as e:
        print(f"✗ File operations test failed: {e}")
        return False

def test_imports():
    """Test that all required modules can be imported"""
    print("\nTesting Module Imports...")
    try:
        import tkinter
        import psutil
        import socket
        import hashlib
        import threading
        import time
        import subprocess
        import json
        print("✓ All modules imported successfully")
        return True
    except Exception as e:
        print(f"✗ Module import test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("BlueHat Security - Core Functionality Tests")
    print("=" * 60)
    print(f"Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Python Version: {sys.version}")
    print(f"Platform: {platform.system()} {platform.release()}")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_system_info,
        test_network_info,
        test_process_monitoring,
        test_file_operations
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"Tests Passed: {passed}/{total}")
    
    if passed == total:
        print("✓ All tests passed!")
        return 0
    else:
        print(f"✗ {total - passed} test(s) failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
