from datetime import datetime
import logging
import os


def get_logger():
    os.makedirs('logs', exist_ok = True)
    log_file = f"logs/automation_logger-{datetime.now().strftime('%Y-%m-%d,%H%M')}.log"
    logging.basicConfig(
        filename = log_file,
        level = logging.INFO,
        format = '%(asctime)s | %(levelname)s : %(message)s'
    )
    return logging.getLogger()