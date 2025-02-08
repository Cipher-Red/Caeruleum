# Caeruleum
 An Open Source Forensics Tool and Command Execution Assistant designed for both forensic analysts and general users seeking simplified and efficient system operations.
 This tool/code may be used and modified freely, provided it adheres to international and local laws within your jurisdiction.
 
<div align="center">
 <img src="CAB.png" alt="Portfolio Screenshot">
 </div>
 
# What is Caeruleum?
 Caeruleum is a lightweight, command-line-based tool designed to function on systems with limited resources. It leverages widely recognized commands to ensure compatibility across a broad range of Windows environments.

# Key Features

 1. Network Scanning
 Scans the local network using the arp -a command to list devices and their IP addresses.

 2. System Logs Collection
 Generates a comprehensive log file containing:
 Event logs
 TCP connections 
 Process details
 User information

 3. Battery Health Report
 Generates a detailed report on battery health for Windows devices with battery functionality.

 4. Fetch Device IP Address
 Retrieves the current device’s IP address.

 5. System Update
 Automates system updates for Windows.

 6. Domain IP Fetcher
 Retrieves the IP address for a specified website domain.

 7. Disk Management & Repair
 Checks and repairs a specified disk.

 8. Running Processes List
 Lists all processes currently running on the system.

 9. Autorun Program Detection
 Identifies all programs registered to launch at system startup.

 10. USB Connection History
 Retrieves the history of all USB devices connected to the system.

 11. File Recovery
 Recovers deleted files by examining shadow copies and retrieving data.
 
 12. File Hash Generator
 Computes file hashes using algorithms such as MD5, SHA-1, and others.

 13. Disk Information & Health Check
 Provides detailed disk information and health status.

 14. Forensic Image Generation
 Creates forensic images of specified disks or drives, with the option to save as .raw or .iso.

 15. Malware Scan Using Windows Defender
 Initiates malware scans via Windows Defender:
 Quick scan
 Full system scan

# Getting Started
* Prerequisites
 - Windows operating system
 - Command-line interface (CLI)
 - 

# Required Libraries

To run this project, make sure you have the following libraries installed:

- `winreg`
- `pytsk3`
- `colorama`
- `subprocess`
- `os`
- `time`

To install the required libraries, use the following pip command:

```bash
pip install pytsk3 colorama
```
Note: `winreg`, `subprocess`, `os`, and `time` are standard Python libraries and do not require installation.

# Usage Instructions
 - Download or clone the repository.
 - Run the program via the provided executable file (.exe), which is ready to be executed.
 
# Contributions
 Contributions are welcome! If you have ideas for enhancements or bug fixes, feel free to fork the repository and submit a pull request.

##License##
 This project is licensed under the Apache License 2.0. See the LICENSE file for more details.

##Legal Disclaimer##
 This tool must be used in compliance with international and local laws. The developers are not responsible for any misuse.

 # Author & Maintainer
 This project was created and is maintained by Qais Mohammad alqaissi.
 # You can reach me at
 * [linkedin](www.linkedin.com/in/qais-alqaissi-1b9295238)
 * [Check out my portfolio](https://qaisalqaissi.netlify.app)
 * Qipher09@proton.me
