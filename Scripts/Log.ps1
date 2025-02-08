# Get-FileLastWriteTime.ps1

param (
    [string]$directory
)

Get-ChildItem -Path $directory -File | Sort-Object LastWriteTime | Select-Object FullName, LastWriteTime > C:\Users\qaisa\Desktop\Logs\LogFile.txt

Echo 'Log Has Been Created,Location: C:\Users\qaisa\Desktop\Logs\LogFile.txt '

