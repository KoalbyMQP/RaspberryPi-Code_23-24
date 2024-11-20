import psutil
from typing import Dict, Any

class CPUCollector:
    @staticmethod
    def collect() -> Dict[str, Any]:
        return {
            'cpu_percent_per_core': psutil.cpu_percent(percpu=True),
            'cpu_freq': psutil.cpu_freq().current,
            'cpu_temp': CPUCollector._get_cpu_temp(),
            'load_avg': psutil.getloadavg()
        }
    
    @staticmethod
    def _get_cpu_temp() -> float:
        try:
            with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
                return float(f.read().strip()) / 1000.0
        except:
            return 0.0