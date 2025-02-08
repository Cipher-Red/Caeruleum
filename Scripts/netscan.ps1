arp -a | Select-String "dynamic" | ForEach-Object {
    $ip = ($_ -split "\s+")[1]
    $hostname = [System.Net.Dns]::GetHostEntry($ip).HostName
    Write-Output "$ip - $hostname"
}