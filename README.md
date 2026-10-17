# 호텔 전등 리모컨 (Hotel Lamp Remocon)

한국폴리텍대학 풀스택 실습을 위한 교육용 프로젝트입니다. **투숙객 스마트폰(Frontend) → 호텔TV를 모사한 노트북 서버(Backend) → SQLite**의 동작을 구현합니다. 실제 호텔의 IoT 전등과 연동하지 않고 웹 화면의 전등 상태를 제어합니다.

## 구성

- `frontend/index.html`: HTML/CSS/JavaScript 전등 ON/OFF 리모컨
- `backend/server.py`: Python aiohttp HTTP/WebSocket 서버, SQLite 상태 저장
- `requirements.txt`: 실행 의존성

## 실행

```bash
python -m pip install -r requirements.txt
python backend/server.py
```

- 노트북 브라우저에서 `http://localhost:8080` 접속
- 같은 Wi-Fi에 연결한 스마트폰에서 `http://노트북_IP:8080` 접속 (방화벽 허용 필요)
- ON/OFF 버튼을 누르면 WebSocket 메시지가 서버에 도착하고, SQLite `lamp` 테이블에 저장됩니다.
- 연결된 다른 브라우저에도 상태가 실시간으로 동기화됩니다.

## 실습 단계

1. Frontend / Backend 개념 이해
2. Python 서버 실행
3. HTTP로 리모컨 UI 제공
4. JavaScript로 ON/OFF 버튼 만들기
5. WebSocket 연결하기
6. 버튼 이벤트를 JSON 메시지로 전송
7. 서버에서 명령 처리
8. SQLite에 상태 저장
9. 변경된 상태를 접속한 화면에 반영
10. 스마트폰에서 제어 확인

## 주의

실습 편의를 위해 **인증 없이 로컬 네트워크에서 실행**합니다. 인터넷 공개 서버로 배포하거나 실제 객실 조명에 연결하지 마세요. 이 저장소 코드는 이전 실습 설계를 바탕으로 재구성한 교육용 예제이며, 과거 개발했던 원본 프로젝트와 완전히 동일한 코드임을 의미하지 않습니다.
