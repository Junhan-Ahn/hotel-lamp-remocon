# 요청 흐름

1. 스마트폰 브라우저가 Nginx `:8080`에 접속합니다.
2. Nginx가 `frontend/index.html`을 반환합니다.
3. JavaScript가 `ws://호스트:8080/ws`에 연결합니다.
4. Nginx가 WebSocket Upgrade 요청을 Python `127.0.0.1:8765/ws`로 전달합니다.
5. ON/OFF JSON 명령을 Python이 처리하고 SQLite에 저장합니다.
6. Python이 상태 변경을 연결된 모든 WebSocket 클라이언트에 전송합니다.
7. 각 스마트폰 화면이 상태를 갱신합니다.
