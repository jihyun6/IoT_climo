#!/bin/bash
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
mkdir -p /home/pi/Desktop/climo/humidSensor/logs
sleep 20
python3 -u /home/pi/Desktop/climo/humidSensor/humidSensorTest.py >> /home/pi/Desktop/climo/humidSensor/logs/humid_$timestamp.log 2>&1
