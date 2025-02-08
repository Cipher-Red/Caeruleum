
$OP="C:\\SecurityLog"

if(-not (Test-Path -Path $OP)){
New-Item -ItemType Directory -Path $OP
}

$currentDate= Get-Date -Format "yyyy-MM-dd"

$StartTime = (Get-Date).Date
$EndTime = (Get-Date).Date.AddDays(1).AddSeconds(-1)

$Filter = @{ 
	LogName ="Security"
	ID 	= 4624
	StartTime = $StartTime
	EndTime = $EndTime 
}

$ELog = Get-WinEvent -FilterHashtable $Filter


if($ELog){
	$ELog | Export-CliXml -Path "$OP\\$currentDate-SecurityLogs.xml"
Write-Host "Security Log Taken Date $currentDate"

}

else {
Write-Host "An Error Has Occurred"
}