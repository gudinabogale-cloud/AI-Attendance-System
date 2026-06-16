#!/usr/bin/env python3
"""
Test script to verify AI Attendance System installation
"""

import sys
import subprocess

def check_python_version():
    """Check if Python version is 3.8+"""
    print("Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor}.{version.micro} - Too old (Need 3.8+)")
        return False

def check_packages():
    """Check if required packages are installed"""
    print("\nChecking required packages...")
    
    required_packages = [
        ('flask', 'Flask'),
        ('cv2', 'OpenCV'),
        ('numpy', 'NumPy'),
        ('pandas', 'Pandas'),
        ('PIL', 'Pillow')
    ]
    
    all_installed = True
    
    for import_name, display_name in required_packages:
        try:
            __import__(import_name)
            print(f"✓ {display_name} - Installed")
        except ImportError:
            print(f"✗ {display_name} - Not installed")
            all_installed = False
    
    return all_installed

def check_opencv_contrib():
    """Check if OpenCV has face recognition module"""
    print("\nChecking OpenCV face recognition module...")
    try:
        import cv2
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        print("✓ OpenCV face module - Available")
        return True
    except AttributeError:
        print("✗ OpenCV face module - Missing (install opencv-contrib-python)")
        return False

def check_directories():
    """Check if required directories exist"""
    print("\nChecking directory structure...")
    
    from pathlib import Path
    
    base_dir = Path(__file__).parent
    required_dirs = ['dataset', 'trainer', 'attendance', 'templates', 'static']
    
    all_exist = True
    
    for dir_name in required_dirs:
        dir_path = base_dir / dir_name
        if dir_path.exists():
            print(f"✓ {dir_name}/ - Exists")
        else:
            print(f"✗ {dir_name}/ - Missing")
            all_exist = False
    
    return all_exist

def check_templates():
    """Check if HTML templates exist"""
    print("\nChecking HTML templates...")
    
    from pathlib import Path
    
    base_dir = Path(__file__).parent
    templates_dir = base_dir / 'templates'
    required_templates = ['index.html', 'register.html', 'attendance.html', 'reports.html']
    
    all_exist = True
    
    for template in required_templates:
        template_path = templates_dir / template
        if template_path.exists():
            print(f"✓ {template} - Exists")
        else:
            print(f"✗ {template} - Missing")
            all_exist = False
    
    return all_exist

def check_camera():
    """Check if camera is accessible"""
    print("\nChecking camera access...")
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, frame = cap.read()
            cap.release()
            if ret:
                print("✓ Camera - Accessible")
                return True
            else:
                print("⚠ Camera opened but couldn't read frame")
                return False
        else:
            print("✗ Camera - Cannot open (may be in use)")
            return False
    except Exception as e:
        print(f"✗ Camera - Error: {e}")
        return False

def main():
    print("=" * 60)
    print("AI Attendance System - Installation Test")
    print("=" * 60)
    print()
    
    results = []
    
    results.append(("Python Version", check_python_version()))
    results.append(("Required Packages", check_packages()))
    results.append(("OpenCV Face Module", check_opencv_contrib()))
    results.append(("Directory Structure", check_directories()))
    results.append(("HTML Templates", check_templates()))
    results.append(("Camera Access", check_camera()))
    
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status} - {name}")
    
    print("\n" + "-" * 60)
    print(f"Total: {passed}/{total} checks passed")
    print("-" * 60)
    
    if passed == total:
        print("\n🎉 All checks passed! System is ready to use.")
        print("Run 'python app.py' to start the server.")
    else:
        print("\n⚠ Some checks failed. Please fix the issues above.")
        print("Run 'pip install -r requirements.txt' to install missing packages.")
    
    return passed == total

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n✗ Error running tests: {e}")
        sys.exit(1)
