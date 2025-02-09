import os
import platform
import subprocess
import time
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Check if the OS is Linux
def is_linux():
    return platform.system() == "Linux"

# Feature 1: Create Log Directory
def create_log():
    print(Fore.BLUE + "Starting the log creation process, darling. Let’s get this done efficiently.")
    logdir = input(Fore.MAGENTA + "Where would you like to save the log folder? Enter the directory, and I’ll handle the rest: ")
    subprocess.run(["mkdir", "-p", logdir])
    print("Log folder created successfully. You’re welcome, sweetheart.")

# Feature 2: Network Scan
def net_scan():
    print(Fore.BLUE + "Starting The Scan Love..")
    result = subprocess.run(["nmap", "-sn", "192.168.1.0/24"], text=True, capture_output=True)
    print("Scan Complete. Here are the devices that are on the network, Darling..")
    print(result.stdout)

    com = input(Fore.MAGENTA + "Would you like to save the Network Information? (Yes/No): ").lower()

    if com == "yes":
        output_file = "NetScan.txt"
        with open(output_file, "w") as file:
            file.write(result.stdout)
        print(f"Network Scan results saved to {output_file}. Let me know if you need anything else!")
    else:
        print("No problem! The results weren’t saved. Let me know if you need further assistance.")

# Feature 3: Generate Battery Report (Not applicable on Linux)
def generate_battery_report():
    print(Fore.BLUE + "Battery report is not available on Linux systems, darling.")

# Feature 4: Get IP Address
def get_ip_address():
    print(Fore.BLUE + "Let me check your device's IP addresses for you. One moment...")
    result = subprocess.run(["ip", "addr"], capture_output=True, text=True)
    ipv4_addresses = []
    ipv6_addresses = []

    for line in result.stdout.splitlines():
        if "inet " in line and not line.strip().startswith("inet 127."):
            ipv4_addresses.append(line.split()[1].split("/")[0])
        elif "inet6 " in line and not line.strip().startswith("inet6 ::1"):
            ipv6_addresses.append(line.split()[1].split("/")[0])

    if ipv4_addresses:
        print("Here are your IPv4 addresses, darling:")
        for ip in ipv4_addresses:
            print(f"  - {ip}")
    else:
        print(Fore.RED + "No IPv4 addresses found. That’s unusual, but we’ll figure it out.")

    if ipv6_addresses:
        print("And here are your IPv6 addresses:")
        for ip in ipv6_addresses:
            print(f"  - {ip}")
    else:
        print(Fore.RED + "No IPv6 addresses found. Interesting, isn’t it?")

# Feature 5: Update Device (Not applicable on Linux)
def update_device():
    print(Fore.BLUE + "System updates are handled by package managers on Linux. Use 'sudo apt update && sudo apt upgrade' for Debian-based systems, darling.")

# Feature 6: Lookup Website IP
def lookup_website_ip():
    print(Fore.BLUE + "Sure, I can help you find the IP address of a website. Let’s do this.")
    add = input("Please enter the website link (e.g., www.example.com): ")
    subprocess.run(["nslookup", add])
    print(Fore.BLUE + "Here’s the IP address for the website you entered. Easy, right?")

# Feature 7: Disk Repair
def manage_disk():
    print(Fore.RED + "Note that this may alter some information on the disk or corrupt it. Proceed with caution.")
    com = input("Would you still like to proceed? |Yes|OR|No| ").lower()
    com = com.replace(" ", "")
    if com == "yes":
        print(Fore.BLUE + "Let me check your disks for you. This won’t take long...")
        result = subprocess.run(["lsblk"], text=True, capture_output=True)
        print(result.stdout)

        disk_name = input("Which disk would you like to repair? Enter the disk name (e.g., sda1): ")

        print(f"Got it! I’ll check and repair the disk {disk_name} for you. This might take a few minutes, so be patient.")
        repair_command = f"sudo fsck /dev/{disk_name}"
        result = subprocess.run(repair_command, text=True, capture_output=True, shell=True)
        print(result.stdout)
        print("Disk repair complete! Let me know if you need anything else, love.")
    else:
        print("Heading back...")

# Feature 8: Get All Running Processes
def installed_programs():
    print(Fore.BLUE + "Let me show you all the running processes on your device. One moment...")
    subprocess.run(["ps", "aux"])
    print("Here’s the list of running programs. Let me know if you need further details, darling!")

# Feature 9: Get Startup Programs
def start_up_programs():
    print(Fore.BLUE + "Let’s take a look at the programs that start up with your device. This will be quick...")
    result = subprocess.run(["ls", "/etc/init.d/"], capture_output=True, text=True)
    print(result.stdout)
    print("That’s everything! Let me know if you’d like to manage any of these, sweetheart.")

# Feature 10: USB History
def get_usb_history():
    print(Fore.BLUE + "Let me fetch the USB history for you. This might take a second...")
    result = subprocess.run(["lsusb"], capture_output=True, text=True)
    print("| USB Devices |")
    print(result.stdout)
    print(Fore.BLUE + "That’s all the USB history I could find. Let me know if you need more details, darling!")

# Feature 11: File Recovery Using rsync
def recovery():
    print(Fore.BLUE + "Let’s recover some files using rsync. I’ll guide you through this.")
    source = input("Enter the source directory (e.g., /mnt/backup): ")
    destination = input("Enter the destination directory (e.g., /home/user/recovered_files): ")

    rsync_command = f"rsync -av {source} {destination}"
    result = subprocess.run(rsync_command, capture_output=True, text=True, shell=True)

    if result.returncode != 0:
        print(Fore.RED + "Oops! Something went wrong during recovery:")
        print(result.stderr.strip())
    else:
        print(Fore.BLUE + "File recovery complete! Let me know if you need anything else, love.")

# Feature 12: Hash Generator
def hash():
    print(Fore.BLUE + "Let’s generate a hash for your file. Which algorithm would you like to use?")
    path = input("Please enter the file path and name: ")
    algo = input("Enter the hash algorithm (e.g., sha256, md5): ")

    if " " in path and not path.startswith('"'):
        path = f'"{path}"'

    hash_command = f"{algo}sum {path}"
    result = subprocess.run(hash_command, capture_output=True, text=True, shell=True)
    print(result.stdout)

    com = input(Fore.MAGENTA + "Would you like to save the hash? (Yes/No): ").lower()
    if com == "yes":
        if result.returncode == 0:
            output_file = "Hash.txt"
            with open(output_file, "w") as file:
                file.write(result.stdout)
            print(Fore.WHITE + f"Hash saved to {output_file}. Let me know if you need anything else, darling!")
        else:
            print(Fore.RED + "Oops! Something went wrong:", result.stderr)
    else:
        print(Fore.BLUE + "No problem! The hash wasn’t saved. Let me know if you need further assistance.")

# Feature 13: Get Disk Health/Status
def disk_info():
    print(Fore.BLUE + "Let me check the health and status of your disks. This will just take a moment...")
    result = subprocess.run(["lsblk", "-o", "NAME,SIZE,MOUNTPOINT,STATE"], capture_output=True, text=True)
    print(result.stdout)
    print(Fore.BLUE + "Here’s the disk information, love.")

    com = input("Would you like to save the Disk Information? (Yes/No): ").lower()
    if com == "yes":
        output_file = "DiskInfo.txt"
        with open(output_file, "w") as file:
            file.write(result.stdout)
        print(Fore.BLUE + f"Disk Information results saved to {output_file}. Let me know if you need anything else!")
    else:
        print(Fore.BLUE + "No problem! The results weren’t saved. Let me know if you need further assistance.")

# Feature 14: Create Disk Image
def image_gen():
    print(Fore.BLUE + "Let’s create a forensic image of your disk. First, I’ll list the available disks...")
    result = subprocess.run(["lsblk"], capture_output=True, text=True)
    print(result.stdout)

    disk = input("Please enter the device's path to create the image (e.g., /dev/sda): ").strip()
    output = input("Now, where would you like to save the image? Enter the path and name (e.g., /home/user/image.dd): ").strip()

    print(Fore.BLUE + f"Creating the forensic image at {output}. This might take a while, so be patient...")
    dd_command = f"sudo dd if={disk} of={output} bs=4M status=progress"
    subprocess.run(dd_command, shell=True)
    print(f"Image successfully created at: {output}. Let me know if you need anything else, darling!")

# Feature 15: Malware Scan Using ClamAV
def malware_scan():
    try:
        ans = input("Would you like to run a Quick Scan or a Full Scan? ").lower()
        ans = ans.replace(" ", "")

        if ans in ["quick", "quickscan"]:
            print(Fore.BLUE + "Quick Scan selected. Let’s get started, darling.")
            print("Preparing the scanner. This will just take a moment...")
            result = subprocess.run(["clamscan", "-r", "--quiet", "/"], capture_output=True, text=True)
            print("Scan complete! Fetching the results...")
            print(result.stdout)
        elif ans in ["full", "fullscan"]:
            print(Fore.BLUE + "Full Scan selected. This might take a while, so please be patient, darling.")
            print("Preparing the scanner. This will just take a moment...")
            result = subprocess.run(["clamscan", "-r", "/"], capture_output=True, text=True)
            print("Scan complete! Fetching the results...")
            print(result.stdout)
        else:
            print("No problem! Let me know if you’d like to run a scan later, darling.")
    except subprocess.CalledProcessError as e:
        print(f"Oops! Something went wrong during the scan: {e}")

# Feature 16: Get System Information
def system_info():
    print(Fore.BLUE + "Let me fetch some system information for you. One moment...")
    result = subprocess.run(["uname", "-a"], capture_output=True, text=True)
    print(result.stdout)
    print(Fore.BLUE + "Here’s your system information, love.")

def he_lp():
    print("Roger That Here is the Full Command List to Use")
    print("1 : Exit Program")
    print("2 : Scan The Network")
    print("3 : System Log")
    print("4 : Battery Health")
    print("5 : Get The IP Address For the Device")
    print("6 : Update The Device")
    print("7 : Get A Websites IP Address")
    print("8 : Manage A Specific Disk")
    print("9 : Get All Running Process")
    print("10 : Gets All AutoRun Programs")
    print("11 : Fetch USB History")
    print("12 : Recover Deleted Files")
    print("13 : Get A Hash")
    print("14 : Get Disk Info and Health Status")
    print("15 : Generate A Forensic Image")
    print("16 : Malware Scan Using Windows Defender")

# Main Function
def main():
    print(Fore.CYAN +"Hello, darling! I’m Caeruleum, your personal assistant. How can I help you today?")

    while True:
        In = input(Fore.CYAN + "What would you like me to do? "+Fore.BLUE).lower()
        In = In.replace(" ", "")

        if In in ["exit", "stop", "thatsall", "thatsit", "1"]:
            print("Shutting down... Have a wonderful day, love!")
            break

        elif In in ["networkscan", "scanthenetwork", "2"]:
            net_scan()

        elif In in ["createalog", "createlog", "3"]:
            create_log()

        elif In in ["battery", "batterylife", "whatsmybatterylife", "howsmybattery", "batteryhealth", "4"]:
            generate_battery_report()

        elif In in ["myip", "deviceip", "whatsmyipaddress", "ip", "5"]:
            get_ip_address()

        elif In in ["updatedevice", "update", "getlatest", "6"]:
            update_device()

        elif In in ["websiteaddress", "lookupwebsiteaddress", "checkip", "7"]:
            lookup_website_ip()

        elif In in ["disk", "storage", "managedisk", "8"]:
            manage_disk()

        elif In in ["runningprograms", "whataretherunningprogramsonthisdevice", "programs", "program", "9"]:
            installed_programs()

        elif In in ["autorun", "whatarethebootupprograms", "bootup", "startup", "10"]:
            start_up_programs()

        elif In in ["usb", "usbhistory", "historyusb", "history", "11"]:
            get_usb_history()

        elif In in ["deletedfiles", "deleted", "recover", "recoverfiles", "12", "recovery", "filerecovery", "recoveryfile", "getbackafile"]:
            recovery()

        elif In in ["gethash", "hash", "filehash", "whatsthehash", "13"]:
            hash()

        elif In in ["diskhealth", "healthdisk", "diskstatus", "statusdisk", "diskinfo", "diskinformation", "14"]:
            disk_info()

        elif In in ["createimage", "image", "createaimage", "createanimage", "15"]:
            image_gen()

        elif In in ["scan", "scanthispc", "malwarescan", "scanformalware", "malware", "16"]:
            malware_scan()

        elif In in ["help", "-help", "--help", "help-", "-h", "--h", "h"]:
            he_lp()

        else:
            print("Hmm, I didn’t quite catch that. Could you try again?")

if __name__ == "__main__":
    main()