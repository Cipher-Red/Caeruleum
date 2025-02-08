import subprocess
import os
import winreg
import pytsk3
import time
from colorama import Fore, Back, Style, init

init(autoreset=True)

def create_log():
    print(Fore.BLUE +"Starting the log creation process, darling. Let’s get this done efficiently.")
    Logdir = input(Fore.MAGENTA +"Where would you like to save the log folder? Enter the directory, and I’ll handle the rest: ")
    subprocess.run(["powershell", "-File", "Scripts\\DFB.ps1", Logdir])
    print("Log folder created successfully. You’re welcome, sweetheart.")

def net_scan():
    print(Fore.BLUE +"Starting The Scan Love..")
    result = subprocess.run(["powershell", "-File", "Scripts\\netscan.ps1"], text=True, capture_output=True, shell=True)
    print("Scan Complete Here are the devices that are on the network Darling..")
    print(result.stdout)

    com = input(Fore.MAGENTA +"Would you like to save the Network Information ? (Yes/No): ").lower()

    if com == "yes":
        output_file = "NetScan.txt"
        with open(output_file, "w") as file:
            file.write(result.stdout)
        print(f"Net Work Scan results saved to {output_file}. Let me know if you need anything else!")
    else:
        print("No problem! The results weren’t saved. Let me know if you need further assistance.")

# From the name generates a Battery Report
def generate_battery_report():
    print(Fore.BLUE +"Let me gather some battery data for you. This will just take a moment, so sit tight...")
    cmd_command = "powercfg /batteryreport"
    subprocess.run(["cmd", "/C", cmd_command])
    report_path = os.path.join(os.getcwd(), "battery-report.html")
    if os.path.exists(report_path):
        os.startfile(report_path)
        print(Fore.BLUE +"Your battery report is ready, love. Opening it now...")
    else:
        print(Fore.RED +"Hmm, I couldn’t find the battery report. Let’s try that again, shall we?")

# Gets The IP address Using CMD
def get_ip_address():
    print(Fore.BLUE +"Let me check your device's IP addresses for you. One moment...")
    cmd_command = "ipconfig"
    result = subprocess.run(["cmd", "/C", cmd_command], capture_output=True, text=True)
    ipv4_addresses = []
    ipv6_addresses = []

    for line in result.stdout.splitlines():
        if "IPv4 Address" in line:
            ipv4_addresses.append(line.split(":")[1].strip())
        elif "IPv6 Address" in line:
            ipv6_addresses.append(line.split(":")[1].strip())

    if ipv4_addresses:
        print("Here are your IPv4 addresses, darling:")
        for ip in ipv4_addresses:
            print(f"  - {ip}")
    else:
        print(Fore.RED +"No IPv4 addresses found. That’s unusual, but we’ll figure it out.")

    if ipv6_addresses:
        print("And here are your IPv6 addresses:")
        for ip in ipv6_addresses:
            print(f"  - {ip}")
    else:
        print(Fore.RED +"No IPv6 addresses found. Interesting, isn’t it?")

# Updates The Device
def update_device():
    print(Fore.BLUE +"Let’s make sure your device is up to date. Opening Windows Update for you...")
    cmd_command = "start ms-settings:windowsupdate-action"
    subprocess.run(["cmd", "/C", cmd_command])
    print("You’re all set, love. Check for updates in the Windows Update settings.")

# Gets a Websites IP address Using CMD
def lookup_website_ip():
    print(Fore.BLUE +"Sure, I can help you find the IP address of a website. Let’s do this.")
    Add = input(Fore.MAGENTA +"Please enter the website link (e.g., www.example.com): ")
    cmd_command = "nslookup"
    subprocess.run(["cmd", "/C", cmd_command + " " + Add])
    print(Fore.BLUE +"Here’s the IP address for the website you entered. Easy, right?")

# Disk Repair
def manage_disk():
    print(Fore.RED +"Note that this may alter some information on the disk or corrupt it. Proceed with caution.")
    com = input(Fore.MAGENTA +"Would you still like to proceed? |Yes|OR|No| ").lower()
    com = com.replace(" ", "")
    if com == "yes":
        print(Fore.BLUE +"Let me check your disks for you. This won’t take long...")
        cmd_command = "list disk\n"
        result = subprocess.run(["diskpart"], input=cmd_command, text=True, capture_output=True)
        print(result.stdout)

        result = subprocess.run("wmic logicaldisk get name", text=True, capture_output=True, shell=True)
        drives = result.stdout.splitlines()
        available_drives = [drive.strip() for drive in drives if drive.strip() and drive.strip() != "Name" and ":" in drive]

        if available_drives:
            print("Here are the available drives, darling:", available_drives)
        else:
            print("Hmm, I couldn’t find any available drives. Let’s double-check.")
            return

        disk_letter = input(Fore.MAGENTA +"Which drive would you like to repair? Enter the drive letter (e.g., C): ")

        if disk_letter not in available_drives:
            print(Fore.RED +f"Oops! That drive letter isn’t valid. Available drives are: {', '.join(available_drives)}")
            return

        print(f"Got it! I’ll check and repair the disk {disk_letter} for you. This might take a few minutes, so be patient.")
        repair_command = f"chkdsk {disk_letter} /f /r"
        result = subprocess.run(repair_command, text=True, capture_output=True, shell=True)
        print(result.stdout)
        print("Disk repair complete! Let me know if you need anything else, love.")
    else:
        print("Heading back...")

# Gets All Running Programs
def installed_programs():
    print(Fore.BLUE +"Let me show you all the running processes on your device. One moment...")
    cmd_command = "tasklist"
    subprocess.run(["cmd", "/C", cmd_command])
    print("Here’s the list of running programs. Let me know if you need further details, darling!")

# Gets the Device Startup programs or AutoRun
def start_up_programs():
    print(Fore.BLUE +"Let’s take a look at the programs that start up with your device. This will be quick...")
    result = subprocess.run(["wmic", "startup", "get", "caption,command"], capture_output=True, text=True)
    print(result.stdout)
    print("That’s everything! Let me know if you’d like to manage any of these, sweetheart.")

# USB History
def get_usb_history():
    print(Fore.BLUE +"Let me fetch the USB history for you. This might take a second...")
    usb_path = r"SYSTEM\CurrentControlSet\Enum\USBSTOR"
    reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, usb_path)
    print(Fore.WHITE +"| USB History Table |")
    i = 0

    while True:
        try:
            subkey_name = winreg.EnumKey(reg_key, i)
            print(f"  Device: {subkey_name}")
            i += 1
        except OSError as e:
            if e.winerror == 259:
                break
            else:
                print(Fore.RED +f"Oops! Something went wrong: {e}")
                break

    print(Fore.BLUE +"That’s all the USB history I could find. Let me know if you need more details, darling!")

# File Recovery using shadow copies
def recovery():
    print(Fore.BLUE +"Let’s recover some files from shadow copies. I’ll guide you through this.")
    result = subprocess.run(["vssadmin", "list", "shadows"], capture_output=True, text=True)

    if result.returncode != 0:
        print(Fore.RED +"Hmm, I couldn’t list the shadow copies. Here’s the error:")
        print(result.stderr)
        return

    shadow_copy_volumes = {}
    shadow_copy_id = None
    original_volume = None
    shadow_copy_volume = None

    for line in result.stdout.splitlines():
        line = line.strip()

        if line.startswith("Shadow Copy ID:"):
            shadow_copy_id = line.split(":")[1].strip()
        elif line.startswith("Original Volume:"):
            original_volume = line.split(":")[1].strip()
        elif line.startswith("Shadow Copy Volume:"):
            shadow_copy_volume = line.split(":")[1].strip()

            if shadow_copy_id and original_volume and shadow_copy_volume:
                shadow_copy_volumes[shadow_copy_volume] = (shadow_copy_id, original_volume)
                shadow_copy_id = None
                original_volume = None
                shadow_copy_volume = None

    if not shadow_copy_volumes:
        print(Fore.BLUE +"No shadow copies found. Let’s try something else, darling.")
        return

    print(Fore.GREEN +f"Found {len(shadow_copy_volumes)} shadow copy(ies). Let’s proceed!")

    for volume_path, (copy_id, disk_letter) in shadow_copy_volumes.items():
        shadow_path = f"\\\\?\\{volume_path[4:]}\\"
        print(f"\nListing files in Shadow Copy ({copy_id}) for volume {disk_letter}: {shadow_path}")

        robocopy_command = f"robocopy {shadow_path} {shadow_path} /L"
        robocopy_result = subprocess.run(robocopy_command, capture_output=True, text=True, shell=True)

        if robocopy_result.returncode != 0:
            print(Fore.RED +f"Oops! Something went wrong while listing files in shadow copy {copy_id}:")
            print(robocopy_result.stderr.strip())
        else:
            print(robocopy_result.stdout.strip())

    shadow = input(Fore.MAGENTA +"Please enter the shadow directory path (e.g., \\\\.\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy1\\path\\to\\file): ")
    destination = input(Fore.MAGENTA +"Where would you like to save the recovered file? Enter the destination path (e.g., C:\\RecoveredFiles\\file.txt): ")

    shadow_path = f"\\\\?\\{shadow[4:]}\\"
    robocopy_command = f"robocopy {shadow_path} {destination} /S"
    robocopy_result = subprocess.run(robocopy_command, capture_output=True, text=True, shell=True)

    if robocopy_result.returncode != 0:
        print(Fore.RED +"Oops! Something went wrong during recovery:")
        print(robocopy_result.stderr.strip())
    else:
        print(Fore.BLUE +"File recovery complete! Let me know if you need anything else, love.")

# Hash Generator Uses any of the know Hash algorithms MD5,SHA1,ETC...
def hash():
    print(Fore.BLUE +"Let’s generate a hash for your file. Which algorithm would you like to use?")
    path = input("Please enter the file path and name: ")
    algo = input("Enter the hash algorithm (e.g., SHA256, MD5): ")

    if " " in path and not path.startswith('"'):
        path = f'"{path}"'

    p_command = f"Get-FileHash {path} -Algorithm {algo}"
    result = subprocess.run(["powershell", "-Command", p_command], capture_output=True, text=True)
    print(result.stdout)

    com = input(Fore.MAGENTA +"Would you like to save the hash? (Yes/No): ").lower()
    if com == "yes":
        if result.returncode == 0:
            output_file = "Hash.txt"
            with open(output_file, "w") as file:
                file.write(result.stdout)
            print(Fore.WHITE +f"Hash saved to {output_file}. Let me know if you need anything else, darling!")
        else:
            print(Fore.RED +"Oops! Something went wrong:", result.stderr)
    else:
        print(Fore.BLUE +"No problem! The hash wasn’t saved. Let me know if you need further assistance.")

# Gets All the disks Health / Status
def disk_info():
    print(Fore.BLUE +"Let me check the health and status of your disks. This will just take a moment...")
    cmd_command = "wmic diskdrive get model,serialnumber,status"
    result = subprocess.run(["cmd", "/C", cmd_command], capture_output=True, text=True)
    print(result.stdout)
    print(Fore.BLUE +"Here’s the disk information, love.")

    com = input(Fore.MAGENTA +"Would you like to save the Disk Information? (Yes/No): ").lower()
    if com == "yes":
        output_file = "DiskInfo.txt"
        with open(output_file, "w") as file:
            file.write(result.stdout)
        print(Fore.BLUE +f"Disk Information results saved to {output_file}. Let me know if you need anything else!")
    else:
        print(Fore.BLUE +"No problem! The results weren’t saved. Let me know if you need further assistance.")

# Creates A Image of a specific Drive
def image_gen():
    print(Fore.BLUE +"Let’s create a forensic image of your disk. First, I’ll list the available disks...")
    cmd_command = "wmic diskdrive list brief"
    result = subprocess.run(["cmd", "/C", cmd_command])
    print(result.stdout)

    dp = input(Fore.MAGENTA +"Please enter the device's path to create the image (e.g., \\\\.\\PhysicalDrive1): ").strip()
    op = input(Fore.MAGENTA +"Now, where would you like to save the image? Enter the path and name (e.g., C:\\usb_image.dd): ").strip()

    if not dp.startswith("\\\\.\\PhysicalDrive"):
        print(Fore.RED +"Oops! That device path doesn’t look right. Make sure it’s in the format \\\\.\\PhysicalDriveX (e.g., \\\\.\\PhysicalDrive1).")
        return

    try:
        img = pytsk3.Img_Info(dp)
        with open(op, 'wb') as f:
            print(Fore.BLUE +f"Creating the forensic image at {op}. This might take a while, so be patient...")
            for offset in range(0, img.get_size(), 4096):
                data = img.read(offset, 4096)
                if not data:
                    break
                f.write(data)

        print(f"Image successfully created at: {op}. Let me know if you need anything else, darling!")
    except Exception as e:
        print(f"Oops! Something went wrong: {e}")

# Malware Scan Using Windows Defender
def malware_scan():
    try:
        ans = input(Fore.MAGENTA +"Would you like to run a Quick Scan or a Full Scan? ").lower()
        ans = ans.replace(" ", "")

        if ans in ["quick", "quickscan"]:
            print(Fore.BLUE +"Quick Scan selected. Let’s get started, darling.")
            print("Preparing the scanner. This will just take a moment...")
            subprocess.run(["powershell", "Start-MpScan -ScanType QuickScan"], check=True)
            print("Scanning your system now. Please wait...")
            time.sleep(60)
            print("Scan complete! Fetching the results...")
            result = subprocess.run(["powershell", "Get-MpThreatDetection"], capture_output=True, text=True)

            if result.returncode == 0:
                print("Here are the scan results:")
                print(result.stdout)
                com = input("Would you like to save the scan results? (Yes/No): ").lower()
                if com == "yes":
                    output_file = "ScanResult.txt"
                    with open(output_file, "w") as file:
                        file.write(result.stdout)
                    print(f"Scan results saved to {output_file}. Let me know if you need anything else!")
                else:
                    print("No problem! The results weren’t saved. Let me know if you need further assistance.")
            else:
                print(Fore.RED +"Oops! Something went wrong while retrieving the scan results.")
                print(result.stderr)

        elif ans in ["full", "fullscan"]:
            print(Fore.BLUE +"Full Scan selected. This might take a while, so please be patient, darling.")
            print("Preparing the scanner. This will just take a moment...")
            subprocess.run(["powershell", "Start-MpScan -ScanType FullScan"], check=True)
            print("Scanning your system now. Please wait...")
            time.sleep(60)
            print("Scan complete! Fetching the results...")
            result = subprocess.run(["powershell", "Get-MpThreatDetection"], capture_output=True, text=True)

            if result.returncode == 0:
                print("Here are the scan results:")
                print(result.stdout)
                com = input("Would you like to save the scan results? (Yes/No): ").lower()
                if com == "yes":
                    output_file = "ScanResult.txt"
                    with open(output_file, "w") as file:
                        file.write(result.stdout)
                    print(f"Scan results saved to {output_file}. Let me know if you need anything else!")
                else:
                    print("No problem! The results weren’t saved. Let me know if you need further assistance.")
            else:
                print("Oops! Something went wrong while retrieving the scan results.")
                print(result.stderr)
        else:
            print("No problem! Let me know if you’d like to run a scan later, darling.")

    except subprocess.CalledProcessError as e:
        print(f"Oops! Something went wrong during the scan: {e}")

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

def main():
    print(Fore.CYAN +"Hello, darling! I’m Caeruleum, your personal assistant. How can I help you today?")

    while True:
        In = input(Fore.CYAN + "What would you like me to do? "+Fore.GREEN).lower()
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