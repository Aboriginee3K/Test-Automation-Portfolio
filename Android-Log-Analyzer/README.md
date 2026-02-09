# Android Log Analysis Tool

# Overview
Automated script designed to streamline the Mobile QA process by capturing and analyzing Android logs (ADB) for critical defects. 

During my time testing Xiaomi and OPPO devices, I realized that manually scrolling through thousands of log lines to find a "crash" was inefficient. I built this tool to automate the detection of "Errors".

# Tech Stack
Python 3
ADB (Android Debug Bridge)
Libraries: os, re(Regex), datetime

# Key Features
1. Auto-Capture: Connects to device via ADB and dumps current logs ('adb logcat -d').
2. Pattern Recognition: Uses Regular Expressions to scan for predefined error keywords (e.g., 'NullPointerException', 'ANR').
3. Report Generation: Automatically generates a clear '.txt' summary report identifying the exact line numbers of potential bugs.

# How to Run
1.  Ensure Python3 installed.
2.  Connect your Android device (ensure USB Debugging is ON).
3.  Run the script.
4.  Check the generated 'Test_Report_xxxx.txt' file for results.

*(Note: If no device is connected, the script will run in "Mocking Mode" using a dummy log file for demonstration purposes.)*

# Sample Output

==============================
   AUTOMATED LOG ANALYSIS REPORT   
==============================
Date: 2024-02-09 10:30:00
Issues Found: 2
------------------------------

CRITICAL ERRORS DETECTED:
[BUG] Line 2: 10-10 12:00:02.500 E/AndroidRuntime: FATAL EXCEPTION: main
[BUG] Line 4: 10-10 12:00:05.999 E/ActivityManager: ANR in com.xiaomi.camera