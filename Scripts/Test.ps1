param (
    [string]$directory
)

$CINFO = Get-ComputerInfo 
$CINFO | Out-File -FilePath $directory\Test3.txt