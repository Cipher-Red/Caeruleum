#!/bin/bash

# Check if directory argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

directory="$1"

# Ensure script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

# Create the directory if it doesn't exist
mkdir -p "$directory"

echo "Gathering Information About The Computing Device, Please Wait..."

echo "Getting Device Information..."
uname -a > "$directory/CINFO.txt" || echo "Failed to get device information"

echo "Getting User Information..."
awk -F: '$3 >= 1000' /etc/passwd > "$directory/UINFO.txt" || echo "Failed to get user information"

echo "Getting Processes Information..."
ps aux > "$directory/PINFO.txt" || echo "Failed to get processes information"

echo "Getting TCP Connections..."
ss -tunap > "$directory/TCPINFO.txt" || echo "Failed to get TCP connections"

echo "Getting Event Logs..."
journalctl -n 100 > "$directory/LINFO.txt" || echo "Failed to get event logs"

echo "Writing Date Folder..."
date > "$directory/DateOfScan.txt" || echo "Failed to write date"

echo "Operation Finished. Please Open The Log Folder For The Text Files Containing the Logs. Location: $directory"
