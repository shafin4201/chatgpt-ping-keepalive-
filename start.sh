#!/bin/bash
Xvfb :99 -screen 0 1024x768x16 &  # Start virtual display
sleep 2
python3 main.py