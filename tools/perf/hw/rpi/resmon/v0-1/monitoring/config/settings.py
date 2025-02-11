from pathlib import Path
from typing import Dict, Any
import yaml

class Settings:
    def __init__(self):
        self.config = {
            'pre_run_duration': 30,
            'post_run_duration': 30,
            'sampling_interval': 1,
            'depthai_path': Path.home() / 'vdepthai' / 'depthai',
            'log_base_dir': Path.cwd() / 'logs'
        }
    
    def update_from_cli(self, cli_args: Dict[str, Any]):
        for key, value in cli_args.items():
            if value is not None:
                self.config[key] = value
    
    def get(self, key: str) -> Any:
        return self.config.get(key)