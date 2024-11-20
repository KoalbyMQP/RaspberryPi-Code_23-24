import logging
from pathlib import Path
from datetime import datetime

class Logger:
    @staticmethod
    def setup(log_dir: Path):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_dir / 'monitor.log'),
                logging.StreamHandler()
            ]
        )