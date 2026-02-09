import os
import re
from datetime import datetime

# -----------Configuration----------
# Set if for True if there is a phone connected, elso False
USE_REAL_DEVICE = False

# Keywords
ERROR_PATTERNS = [
    r"FATAL EXCEPTION",
    r"CRASH",
    r"ANR",  # Application Not Responding
    r"NullPointerException"
]

LOG_FILE = "device_logs.txt"
REPORT_FILE = f"Test_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"


def get_logs():
    """Get logs: catch files from ADB or local"""
    if USE_REAL_DEVICE:
        print("Trying to get logs from phone through ADB...")
        os.system(f"adb logcat -d > {LOG_FILE}")
        print(f"Logs have been saved {LOG_FILE}")
    else:
        print(f"Mocking mode: loading local files {LOG_FILE}...")
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w", encoding="utf-8") as f:
                f.write("10-10 12:00:01.123 D/ViewRoot: ViewRoot's Touch Event\n")
                f.write("10-10 12:00:02.500 E/AndroidRuntime: FATAL EXCEPTION: main\n")
                f.write("10-10 12:00:03.000 I/System.out: Normal processing...\n")
                f.write("10-10 12:00:05.999 E/ActivityManager: ANR in com.xiaomi.camera\n")
            print("Mocking files created.")


def analyze_logs():
    """Analyze logs and form reports."""
    print("Analyzing...")
    found_issues = []

    try:
        with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        for index, line in enumerate(lines):
            for pattern in ERROR_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    found_issues.append(f"Line {index + 1}: {line.strip()}")
                    break

        generate_report(found_issues)

    except FileNotFoundError:
        print("Error: cannot find log file!")


def generate_report(issues):
    """Generate the final report."""
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("=" * 30 + "\n")
        f.write("   AUTOMATED LOG ANALYSIS REPORT   \n")
        f.write("=" * 30 + "\n")
        f.write(f"Date: {datetime.now()}\n")
        f.write(f"Total Lines Scanned: (See raw log)\n")
        f.write(f"Issues Found: {len(issues)}\n")
        f.write("-" * 30 + "\n\n")

        if len(issues) == 0:
            f.write("PASS: No critical errors found in the logs.\n")
            print("Analyze finished. No errors found.")
        else:
            f.write("CRITICAL ERRORS DETECTED:\n")
            for issue in issues:
                f.write(f"[BUG] {issue}\n")
            print(f"Analyze finished. Found {len(issues)} errors. Please check {REPORT_FILE}")


if __name__ == "__main__":
    get_logs()
    analyze_logs()