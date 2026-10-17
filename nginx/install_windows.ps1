# Downloads official nginx/Windows 1.31.7 into nginx/runtime (not committed).
$ErrorActionPreference = "Stop"
$version = "1.31.7"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$root = (Resolve-Path (Join-Path $here "..")).Path
$url = "https://nginx.org/download/nginx-$version.zip"
$zip = Join-Path $env:TEMP "nginx-$version.zip"
$target = Join-Path $here "runtime"
New-Item -ItemType Directory -Force -Path $target | Out-Null
Write-Host "Downloading official Nginx $version from $url"
Invoke-WebRequest -Uri $url -OutFile $zip
Expand-Archive -Path $zip -DestinationPath $target -Force
$exe = Join-Path $target "nginx-$version/nginx.exe"
if (-not (Test-Path $exe)) { throw "nginx.exe not found after extraction" }
Write-Host "Installed: $exe"
Write-Host "Start using: powershell -ExecutionPolicy Bypass -File nginx/start_windows.ps1"
