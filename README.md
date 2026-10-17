# 호텔 전등 리모컨 — Nginx + WebSocket + SQLite

폴리텍대학 교수 역량심사용 풀스택 교육 실습입니다. 호텔TV의 Linux 기반 웹서버를 노트북에서 모사합니다.

## 구조

스마트폰 → Nginx (:8080, HTML 제공·WebSocket 프록시) → Python Backend (127.0.0.1:8765) → SQLite → WebSocket 상태 동기화

## Windows 11 실습 (공식 Nginx 1.31.7)

상세한 설명: [nginx/README.md](nginx/README.md)

PowerShell에서 저장소 최상위 폴더를 열고:

```powershell
powershell -ExecutionPolicy Bypass -File nginx/install_windows.ps1
python -m pip install -r requirements.txt
python backend/server.py
```

**새 PowerShell 창**에서:

```powershell
powershell -ExecutionPolicy Bypass -File nginx/start_windows.ps1
```

브라우저: http://localhost:8080

Nginx 종료: `powershell -ExecutionPolicy Bypass -File nginx/stop_windows.ps1`

## Linux / Ubuntu / WSL

1. `sudo apt install nginx python3 python3-venv`
2. `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
3. 터미널 A: `python backend/server.py`
4. 터미널 B: `python scripts/configure_nginx.py` 후 `sudo nginx -t -c "$(pwd)/nginx.generated.conf"` 및 `sudo nginx -c "$(pwd)/nginx.generated.conf"`

## 파일

- `frontend/index.html` — HTML/CSS/JavaScript 전등 리모컨
- `backend/server.py` — Python WebSocket 및 SQLite
- `nginx/` — Windows용 공식 Nginx 다운로드·실행·중지 스크립트와 설정
- `nginx.conf.template` — Linux Nginx 설정 템플릿
- `scripts/configure_nginx.py` — Linux 설정 생성
- `requirements.txt` — Python 의존성

## 교육용 주의사항

인증과 TLS가 없으므로 신뢰할 수 있는 로컬 네트워크에서만 실행하세요. 인터넷 공개 또는 실제 호텔 조명 제어에 사용하지 마세요. 이전 실습 설계를 재구성한 예제입니다.
