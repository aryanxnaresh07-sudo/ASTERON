import logging
import sys
from pathlib import Path

def setup_logging(level=logging.INFO):
    LOGS_DIR = Path("logs")
    LOGS_DIR.mkdir(exist_ok=True)
    
    formatter = logging.Formatter("%(asctime)s | %(levelname)-8s | %(name)s | %(message)s")
    
    root = logging.getLogger()
    root.setLevel(level)
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    root.addHandler(console_handler)
