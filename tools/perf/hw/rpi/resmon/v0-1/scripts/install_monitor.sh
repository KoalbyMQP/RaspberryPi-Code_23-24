#!/bin/bash

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$(dirname "$(dirname "$(dirname "$(dirname "$(dirname "$(dirname "$SCRIPT_DIR")")")")")")")"

# Install Python dependencies
pip install psutil pandas matplotlib click pyyaml jinja2

# Install LaTeX dependencies
sudo apt-get update
sudo apt-get install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended

# Create desktop entry with correct paths
cat > ~/.local/share/applications/depthai-monitor.desktop << EOL
[Desktop Entry]
Name=DepthAI Monitor
Exec=python3 ${PROJECT_ROOT}/tools/perf/hw/rpi/resmon/v0-1/monitoring/cli.py
Type=Application
Categories=Development;
EOL

chmod +x ~/.local/share/applications/depthai-monitor.desktop

# Ensure log directory exists
mkdir -p "${PROJECT_ROOT}/tools/perf/hw/rpi/resmon/v0-1/logs"