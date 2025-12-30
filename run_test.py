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
    "tests",                      # 👈 IMPORTANT
    "-v",
    "--html", report_path,
    "--self-contained-html"
]

subprocess.run(command)
print(f"Test report generated at: {report_path}")


# Run for CI/CD pipelines without HTML report
# python -m pytest tests -v --html=reports/TestReport.html --self-contained-html --alluredir=allure-results
# allure generate allure-results -o allure-report --clean