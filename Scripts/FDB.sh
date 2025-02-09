#!/bin/bash

# Check if directory argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

directory="$1"

# Create the directory if it doesn't exist
mkdir -p "$directory"

echo "Gathering Information About The Computing Device, Please Wait"

echo "Getting Device Information"
uname -a > "$directory/CINFO.txt"

echo "Getting User Information"
cat /etc/passwd > "$directory/UINFO.txt"

echo "Getting Processes Information"
ps aux > "$directory/PINFO.txt"

echo "Getting TCP Connections"
netstat -tunap > "$directory/TCPINFO.txt"

echo "Getting Event Logs"
journalctl -n 100 > "$directory/LINFO.txt"

echo "Date Folder Has been Written"
date > "$directory/DateOfScan.txt"

echo "Operation Finished. Please Open The Log Folder For The Text File Containing the Logs. Location: $directory"