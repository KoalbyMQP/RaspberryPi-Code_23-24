import psutil
import subprocess
from typing import Dict, Any

class SystemCollector:
    @staticmethod
    def collect() -> Dict[str, Any]:
        disk = psutil.disk_io_counters()
        net = psutil.net_io_counters()
        
        try:
            decoder = subprocess.check_output(['vcgencmd', 'codec_enabled', 'H264']).decode()
            vulkan = subprocess.check_output(['vulkaninfo'], stderr=subprocess.DEVNULL).decode()
        except:
            decoder = "unavailable"
            vulkan = "unavailable"
            
        return {
            'disk_read': disk.read_bytes,
            'disk_write': disk.write_bytes,
            'net_sent': net.bytes_sent,
            'net_recv': net.bytes_recv,
            'process_count': len(psutil.pids()),
            'context_switches': psutil.cpu_stats().ctx_switches,
            'hw_decoder': decoder.strip(),
            'vulkan_support': 'available' if 'Vulkan Instance Version' in vulkan else 'unavailable'
        }