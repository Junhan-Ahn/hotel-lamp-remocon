# Frontend 단계별 실습 — 호텔 전등 리모컨

OpenCV 얼굴인식 단계별 실습처럼 **각 단계의 완성된 `index.html`**을 별도 폴더에 보관합니다. 앞 단계 파일을 덮어쓰지 않고 변화 과정을 비교할 수 있습니다.

| 단계 | 학습 주제 | 결과 |
|---|---|---|
| [1st](1st/README.md) | HTML 기본 | 제목과 전등 아이콘 |
| [2nd](2nd/README.md) | HTML 버튼·CSS | ON/OFF 버튼 배치 |
| [3rd](3rd/README.md) | JavaScript DOM 이벤트 | 브라우저 안에서 전등 상태 변경 |
| [4th](4th/README.md) | JSON 메시지 설계 | 서버로 보낼 명령 확인 |
| [5th](5th/README.md) | WebSocket 통신 | Nginx → Python → SQLite 연동 |

## 실행

1~4단계는 각 폴더의 `index.html`을 직접 열어도 됩니다. 5단계는 [프로젝트 README](../README.md)를 따라 Nginx와 Python Backend를 실행한 뒤 `http://localhost:8080/5th/`로 접속하세요.

기존 `frontend/index.html`은 최종 데모로 그대로 유지합니다.
