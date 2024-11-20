#!/bin/bash
pip install psutil pandas matplotlib click pyyaml

# create desktop shortcut 
cat > ~/.local/share/applications/depthai-monitor.desktop << EOL
[Desktop Entry]
Name=DepthAI Monitor
Exec=python3 -m monitoring.cli
Type=Application
Categories=Development;
EOL

chmod +x ~/.local/share/applications/depthai-monitor.desktop