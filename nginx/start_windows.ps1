$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$root = (Resolve-Path (Join-Path $here "..")).Path
$exe = Join-Path $here "runtime/nginx-1.31.7/nginx.exe"
if (-not (Test-Path $exe)) { throw "Nginx not installed. Run nginx/install_windows.ps1 first." }
New-Item -ItemType Directory -Force -Path (Join-Path $here "logs") | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $here "temp") | Out-Null
$prefix = $root.Replace("\","/") + "/"
& $exe -p $prefix -c nginx/nginx.windows.conf -t
if ($LASTEXITCODE -ne 0) { throw "Nginx config validation failed" }
& $exe -p $prefix -c nginx/nginx.windows.conf
Write-Host "Nginx started at http://localhost:8080"
Write-Host "Run Python backend separately: python backend/server.py"
