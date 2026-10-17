"""Generate a standalone nginx configuration with absolute frontend path.
Usage: python scripts/configure_nginx.py
Then: nginx -c "$(pwd)/nginx.generated.conf"
"""
from pathlib import Path
base = Path(__file__).resolve().parent.parent
template = (base / "nginx.conf.template").read_text(encoding="utf-8")
config = template.replace("__FRONTEND_DIR__", (base / "frontend").as_posix())
path = base / "nginx.generated.conf"
path.write_text(config, encoding="utf-8")
print(f"Generated: {path}")
print("Check: nginx -t -c", path)
print("Start: nginx -c", path)
