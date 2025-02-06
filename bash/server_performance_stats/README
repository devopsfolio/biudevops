# System Resource Monitoring Script

## Overview
This script provides an overview of system resource usage, including CPU, memory, and disk usage, along with the top 5 processes consuming the most CPU and memory. It is useful for monitoring system performance and identifying resource-intensive processes.

## Features
- Displays total CPU usage percentage.
- Shows memory usage (used vs. free) along with percentage.
- Reports disk usage (used vs. total) with percentage.
- Lists the top 5 processes by CPU usage.
- Lists the top 5 processes by memory usage.

## Requirements
- Linux-based operating system (Ubuntu, CentOS, etc.)
- `mpstat` command (available in the `sysstat` package)
- `awk`, `free`, `df`, and `ps` commands (pre-installed on most Linux systems)

## Installation
1. Clone the repository or create a new script file:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Alternatively, create a new script file manually:
   ```bash
   nano system_stats.sh
   ```
   Copy and paste the script content into the file.

3. Grant execution permissions:
   ```bash
   chmod +x system_stats.sh
   ```

## Usage
Run the script using:
```bash
./system_stats.sh
```

The script will output system resource usage statistics, including:
- CPU usage percentage
- Memory usage in MB with percentage
- Disk usage with percentage
- Top 5 CPU-consuming processes
- Top 5 memory-consuming processes

## Example Output
```
========================================
        System Resource Usage           
========================================
Total CPU Usage:
23.4%
----------------------------------------
Memory Usage:
Used: 2048MB / 4096MB (50.00%)
----------------------------------------
Disk Usage:
Used: 15G / 50G (30%)
----------------------------------------
Top 5 Processes by CPU Usage:
  PID COMMAND %CPU
 1234 firefox 10.5
 5678 chrome 8.7
 9101 java 7.2
 1112 python 6.5
 1314 node 5.9
----------------------------------------
Top 5 Processes by Memory Usage:
  PID COMMAND %MEM
 5678 chrome 12.3
 9101 java 10.1
 1234 firefox 9.5
 1516 mysql 8.2
 1718 postgres 7.8
========================================
```

## Customization
- Modify the number of processes displayed by changing the `head -n 6` values in the script.
- Adjust the monitored disk partition by modifying the `df -h /` command.

## Troubleshooting
- If `mpstat` is not found, install `sysstat` using:
  ```bash
  sudo apt install sysstat   # For Debian/Ubuntu
  sudo yum install sysstat   # For CentOS/RHEL
  ```
- Ensure the script has execution permissions (`chmod +x system_stats.sh`).

## License
This script is open-source and can be modified or distributed freely.

## Author
Sergey Krizhanovsky

