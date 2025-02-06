#!/bin/bash

# Check if log directory is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <log_directory>"
    exit 1
fi

LOG_DIR=$1
ARCHIVE_DIR="$LOG_DIR/archive"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
ARCHIVE_FILE="$ARCHIVE_DIR/logs_archive_${TIMESTAMP}.tar.gz"

# Create archive directory if not exists
mkdir -p "$ARCHIVE_DIR"

# Compress logs
tar -czf "$ARCHIVE_FILE" -C "$LOG_DIR" .

# Log the operation
echo "Archived logs to: $ARCHIVE_FILE" | tee -a "$ARCHIVE_DIR/archive_log.txt"

# Output success message
echo "Log archive created: $ARCHIVE_FILE"
