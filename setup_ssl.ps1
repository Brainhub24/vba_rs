# Install Chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install OpenSSL using Chocolatey
choco install openssl.light -y

# Add OpenSSL to system PATH
[Environment]::SetEnvironmentVariable("Path", "$env:Path;$env:ChocolateyInstall\bin", [EnvironmentVariableTarget]::Machine)

Write-Host "OpenSSL installation completed."
Write-Host "OpenSSL setup completed."
