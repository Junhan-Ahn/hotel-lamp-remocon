# 5단계 — WebSocket으로 Nginx·Python·SQLite 연동하기

## 학습 목표
Nginx가 제공한 웹페이지에서 WebSocket을 연결하고 Python 서버가 SQLite에 상태를 저장하게 합니다.

## 실습 파일
- [index.html](index.html)

## 실행 방법
- 1~4단계: `index.html`을 브라우저에서 직접 열어도 됩니다.
- 5단계: Python Backend와 Nginx를 모두 실행한 다음 `http://localhost:8080/5th/`로 접속하세요.
- Nginx를 실행한 경우 각 단계는 `http://localhost:8080/5th/`에서 확인할 수 있습니다.

## 예상 결과
ON/OFF를 누르면 서버에 저장되고, 동시에 접속한 다른 브라우저 화면에도 반영됩니다.

## 학생 확인 질문
브라우저 새로고침 뒤에도 상태가 유지되는 이유는 무엇인가요?

## 다음 단계
전체 시스템에서 Nginx, WebSocket, SQLite 역할을 정리합니다.
