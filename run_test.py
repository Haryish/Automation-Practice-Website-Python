import subprocess
import sys
from datetime import datetime
import os

os.makedirs("reports", exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
report_path = f"reports/TestReport-{timestamp}.html"

command = [
    sys.executable,
    "-m",
    "pytest",
    "--html", report_path,
    "--self-contained-html",
    "-v"
]

subprocess.run(command)



# pytest --html=reports/TestReport-%DATE:~-4%%DATE:~4,2%%DATE:~7,2%-%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%.html --self-contained-html
