# owen-hermes

Owen의 Hermes Agent 자산 저장소.

이 레포는 특정 프로젝트의 코드가 아니라, **Hermes Agent 그 자체**에 대한 기록입니다.

- 에이전트에게 내린 지침과 역할 정의
- 중요한 의사결정과 그 이유
- 프로젝트별 컨텍스트 & 진행 현황
- 에이전트가 기억해야 할 규칙과 선호도
- 트러블슈팅 히스토리

**목적**: 어느 시점으로든 되돌릴 수 있고, 히스토리를 자산으로 쌓는 것.

---

## 디렉토리 구조

```
owen-hermes/
├── README.md                 ← 이 파일
├── agent/
│   ├── identity.md           ← 에이전트 역할 & 행동 원칙
│   └── preferences.md        ← Owen의 작업 스타일 & 선호도
├── projects/
│   └── market-analytics/     ← 쇼핑몰 분석 시스템 프로젝트
│       └── plan.md
├── daily/                    ← 일일 작업 일지 (YYYY-MM-DD.md)
├── decisions/                ← 주요 의사결정 로그 (날짜별)
└── troubleshooting/          ← 오류 & 해결 히스토리
```

---

## 커밋 컨벤션

```
setup:    초기 설정, 환경 구성
plan:     계획 수립 또는 변경
decision: 중요 의사결정 기록
fix:      오류 해결 기록
update:   기존 내용 업데이트
```
