# 호텔 전등 리모컨 — Nginx + WebSocket + SQLite

한국폴리텍대학 교수 역량심사용 **풀스택 교육 실습**입니다. 호텔TV의 Linux 기반 웹서버 구조를 노트북에서 모사합니다.

## 아키텍처

```text
투숙객 스마트폰 / 노트북 브라우저
       │ HTTP / WebSocket :8080
       ▼
Nginx (정적 웹 페이지 제공 / 리버스 프록시)
       ├── /           → frontend/index.html (HTML/CSS/JS)
       ├── /ws         → Python WebSocket 서버 127.0.0.1:8765
       └── /api/state  → Python API 서버 127.0.0.1:8765
                                │
                                ▼
                        SQLite (lamp.sqlite3)
```

## 파일 구성
- `frontend/index.html`: 스마트폰 전등 ON/OFF 화면 (HTML/CSS/JS)
- `backend/server.py`: WebSocket 메시지 처리 및 SQLite 저장
- `nginx.conf.template`: Nginx 설정 템플릿 (정적 파일 / WebSocket 프록시)
- `scripts/configure_nginx.py`: 경로를 반영한 Nginx 설정 생성
- `requirements.txt`: Python 백엔드 의존성

## 실행 (Linux / Ubuntu / WSL Ubuntu)

1. Nginx와 Python 준비 (Ubuntu 예시):
   ```bash
   sudo apt update
   sudo apt install nginx python3 python3-pip python3-venv
   ```
2. 저장소 폴더에서 Python 환경 준비:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. **터미널 A** — Backend 시작:
   ```bash
   python backend/server.py
   ```
4. **터미널 B** — Nginx 설정 생성, 검사, 시작:
   ```bash
   python scripts/configure_nginx.py
   sudo nginx -t -c "$(pwd)/nginx.generated.conf"
   sudo nginx -c "$(pwd)/nginx.generated.conf"
   ```
5. 노트북 브라우저에서 `http://localhost:8080` 접속. 같은 네트워크의 스마트폰은 `http://노트북_IP:8080` 사용 (방화벽 및 WSL 포트 전달 설정에 따라 추가 구성이 필요할 수 있음).

Nginx 중지: `sudo nginx -s stop -c "$(pwd)/nginx.generated.conf"`.

## 수업 흐름
1. Frontend / Backend / Database 구분
2. Nginx 설치 및 웹서버 역할 이해
3. Nginx로 HTML 리모컨 제공
4. JavaScript ON/OFF 버튼과 이벤트 처리
5. WebSocket 메시지 전송
6. Nginx WebSocket 리버스 프록시
7. Python 서버에서 명령 처리
8. SQLite 상태 저장
9. 접속한 브라우저들에 상태 동기화
10. 스마트폰에서 최종 실습

## 주의
실습용으로 인증·TLS가 생략되어 있습니다. 신뢰할 수 있는 로컬 네트워크에서만 실행하세요. 외부 인터넷에 공개하거나 실제 호텔 객실 제어에 사용하지 마세요. 실제 호텔TV 원본 코드가 아니라 수업용 재구성 예제입니다.
