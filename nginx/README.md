# Nginx Windows 실행환경 (v1.31.7)

이 폴더는 공식 [nginx.org](https://nginx.org/en/download.html)에서 Windows 실행파일을 받는 설치 스크립트와 실습용 설정을 담습니다. **nginx.exe 바이너리는 GitHub에 직접 포함되지 않습니다.**

## Windows 11 PowerShell에서 실행

저장소 최상위 폴더에서:

```powershell
powershell -ExecutionPolicy Bypass -File nginx/install_windows.ps1
python -m pip install -r requirements.txt
python backend/server.py
```

다른 PowerShell 창에서:

```powershell
powershell -ExecutionPolicy Bypass -File nginx/start_windows.ps1
```

브라우저에서 `http://localhost:8080`에 접속합니다. 종료하려면 `powershell -ExecutionPolicy Bypass -File nginx/stop_windows.ps1`를 실행하세요.

Nginx는 정적 HTML/CSS/JS를 제공하고, `/ws` 및 `/api/`를 Python 서버(127.0.0.1:8765)로 프록시합니다. 두 프로세스를 모두 실행해야 ON/OFF가 작동합니다.

## 버전
- Nginx 1.31.7 (2026-10-14, mainline)
- 공식 배포 URL: https://nginx.org/download/nginx-1.31.7.zip

Windows용 Nginx는 공식 문서에서 베타로 설명됩니다. 이 프로젝트는 로컬 교육용으로만 사용하세요.
