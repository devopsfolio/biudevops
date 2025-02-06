#!/bin/bash

echo "========================================"
echo "        System Resource Usage           "
echo "========================================"

# Get total CPU usage
echo "Total CPU Usage:"
mpstat 1 1 | awk '/Average/ {print 100 - $NF"%"}'

echo "----------------------------------------"

# Get memory usage
echo "Memory Usage:"
free -m | awk 'NR==2{printf "Used: %sMB / %sMB (%.2f%%)\n", $3, $2, $3*100/$2}'

echo "----------------------------------------"

# Get disk usage
echo "Disk Usage:"
df -h / | awk 'NR==2{printf "Used: %s / %s (%.2f%%)\n", $3, $2, $5}'

echo "----------------------------------------"

# Top 5 processes by CPU usage
echo "Top 5 Processes by CPU Usage:"
ps -eo pid,comm,%cpu --sort=-%cpu | head -n 6

echo "----------------------------------------"

# Top 5 processes by memory usage
echo "Top 5 Processes by Memory Usage:"
ps -eo pid,comm,%mem --sort=-%mem | head -n 6

echo "========================================"
