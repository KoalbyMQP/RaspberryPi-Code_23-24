#!/bin/bash

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$(dirname "$(dirname "$(dirname "$(dirname "$(dirname "$(dirname "$SCRIPT_DIR")")")")")")")"

# Activate virtual environment
cd ~/vdepthai || exit 1
source bin/activate || exit 1

# Install Python dependencies
pip install psutil pandas matplotlib click pyyaml jinja2

# Install LaTeX dependencies
sudo apt-get update
sudo apt-get install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended

# Create desktop shortcut 
cat > ~/Desktop/depthai-monitor.desktop << EOL
[Desktop Entry]
Name=DepthAI Monitor
Exec=/home/finley/Desktop/RaspberryPi-Code_24-25/tools/perf/hw/rpi/resmon/v0-1/monitoring/run_monitor.sh
Type=Application
Categories=Development;
EOL

# Make the desktop entry executable
chmod +x ~/Desktop/depthai-monitor.desktop

# Deactivate virtual environment
deactivate
