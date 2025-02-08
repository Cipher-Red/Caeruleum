param (
    [string]$directory
)

Write-Output "Gathering Information About The Computing Device, Please Wait"

Write-Output "Getting Device Information"
$CINFO = Get-ComputerInfo 
$CINFO | Out-File -FilePath $directory\CINFO.txt

Write-Output "Getting User Information"
$UINFO = Get-LocalUser
$UINFO | Out-File -FilePath $directory\UINFO.txt

Write-Output "Getting Processes Information"
$PINFO = Get-Process 
$PINFO | Out-File -FilePath $directory\PINFO.txt

Write-Output "Getting TCP Connections"
$TCPINFO = Get-NetTCPConnection 
$TCPINFO | Out-File -FilePath $directory\TCPINFO.txt 

Write-Output "Getting Event Logs"
$LINFO =  Get-Eventlog -LogName System -Newest 100 
$LINFO | Out-File -Filepath $directory\LINFO.txt

Write-Output "Date Folder Has been Written"
$DS = Get-Date  
$DS | Out-File -FilePath $directory\DateOfScan.txt

Write-Output "Operation Finished Please Open The Log Folder For The Text File Containing the Logs Location:$directory"