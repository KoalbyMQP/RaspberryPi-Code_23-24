#!/bin/bash
export PYTHONPATH="/home/finley/Desktop/RaspberryPi-Code_24-25/tools/perf/hw/rpi/resmon/v0-1:$PYTHONPATH"
python3 cli.py "$@"