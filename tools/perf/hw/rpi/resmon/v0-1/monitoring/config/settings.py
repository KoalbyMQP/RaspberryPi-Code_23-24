from pathlib import Path
from typing import Dict, Any
import yaml

from pathlib import Path

class Settings:
    def __init__(self):
        desktop_path = Path.home() / 'Desktop'
        
        self.project_root = desktop_path / 'RaspberryPi-Code_24-25'
        self.depthai_path = self.project_root / 'test/io/inputs/camera/oak-d-lite/vdepthai/depthai'
        self.venv_path = self.depthai_path.parent.parent  # vdepthai folder
        
        self.config = {
            'pre_run_duration': 30,
            'post_run_duration': 30,
            'sampling_interval': 1,
            'depthai_path': self.depthai_path,
            'venv_path': self.venv_path,
            'log_base_dir': self.project_root / 'tools/perf/hw/rpi/resmon/v0-1/logs'
        }
    
    def update_from_cli(self, cli_args: Dict[str, Any]):
        for key, value in cli_args.items():
            if value is not None:
                self.config[key] = value
    
    def get(self, key: str) -> Any:
        return self.config.get(key)

    def validate_paths(self) -> bool:
        """Validate that all required paths exist"""
        required_paths = [
            (self.project_root, "Project root"),
            (self.depthai_path, "DepthAI path"),
            (self.venv_path, "Virtual environment path")
        ]
        
        for path, name in required_paths:
            if not path.exists():
                raise FileNotFoundError(f"{name} not found at: {path}")
        return True