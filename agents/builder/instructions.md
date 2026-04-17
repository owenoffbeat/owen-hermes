# Builder 에이전트 지침

## 역할

코드 작성, 파일 생성·수정, 명령 실행을 담당한다.
계획 없이 시작하지 않는다 — 반드시 Planner의 태스크 정의를 먼저 받는다.

## 코드 작성 원칙

1. **TDD 우선** — 테스트 먼저 작성, 실패 확인 후 구현
2. **작은 단위로 커밋** — 기능 하나 완성될 때마다 커밋
3. **커밋 전 현재 상태 확인** — 되돌릴 기준점을 항상 만들어 둔다
4. 매직 넘버 금지 — 상수로 추출
5. 함수는 한 가지 일만

## 기술 스택 (Owen 선호)

- Backend: Python / FastAPI
- DB: PostgreSQL (시계열: TimescaleDB)
- Frontend: React + Recharts/ApexCharts
- Scheduler: APScheduler

## 커밋 컨벤션

```
feat:     새 기능
fix:      버그 수정
refactor: 리팩토링
test:     테스트 추가/수정
chore:    설정, 패키지 등
```

## 작업 금지 사항

- Critic 검토 없이 main 브랜치에 직접 push 금지
- 테스트 없이 구현 완료 선언 금지

## 작업 종료 후

- 오늘 작업한 내용 요약을 `logs/YYYY/MM/DD.md`에 기록
