$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$root = (Resolve-Path (Join-Path $here "..")).Path
$exe = Join-Path $here "runtime/nginx-1.31.7/nginx.exe"
$prefix = $root.Replace("\","/") + "/"
& $exe -p $prefix -c nginx/nginx.windows.conf -s stop
