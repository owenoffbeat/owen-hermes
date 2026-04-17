# owen-hermes

Owen(박윤기)의 Hermes Agent 자산 저장소.

이 레포는 특정 프로젝트 코드가 아니라, **Hermes Agent 자체**에 대한 기록입니다.

- 에이전트별 역할 지침
- 중요한 의사결정과 이유
- 프로젝트별 컨텍스트 & 진행 현황
- 에이전트 일일 작업 로그 (자동 롤업)
- 트러블슈팅 히스토리

**목적**: 어느 시점으로든 되돌릴 수 있고, 히스토리를 자산으로 쌓는 것.

---

## 디렉토리 구조

```
owen-hermes/
├── README.md
│
├── agents/                              ← 에이전트별 독립 공간
│   ├── orchestrator/
│   │   ├── instructions.md              ← 역할 지침
│   │   ├── identity.md                  ← 에이전트 정체성
│   │   ├── preferences.md               ← Owen 작업 스타일
│   │   └── logs/YYYY/MM/
│   │       ├── DD.md                    ← 일일 작업 기록
│   │       └── summary.md              ← 월말 자동 롤업
│   ├── planner/
│   │   ├── instructions.md
│   │   └── logs/YYYY/MM/
│   ├── researcher/
│   │   ├── instructions.md
│   │   └── logs/YYYY/MM/
│   ├── builder/
│   │   ├── instructions.md
│   │   └── logs/YYYY/MM/
│   ├── critic/
│   │   ├── instructions.md
│   │   └── logs/YYYY/MM/
│   └── reporter/
│       ├── instructions.md
│       └── logs/YYYY/MM/
│
├── daily/                               ← 전체 세션 종합 일지 (Owen 시점)
│   └── YYYY/MM/
│       ├── DD.md
│       └── summary.md                  ← 월말 자동 롤업
│
├── projects/
│   └── market-analytics/
│       └── plan.md
│
├── decisions/log.md                     ← 주요 의사결정 히스토리
├── troubleshooting/log.md               ← 오류 & 해결 히스토리
└── scripts/
    └── monthly_rollup.py                ← 월말 자동 롤업 스크립트
```

---

## 로그 롤업 구조

```
매일      → DD.md 생성 (에이전트가 직접 기록)
월말 자동  → DD.md들 → summary.md 로 압축 후 일일 파일 삭제
           (git history에는 영구 보존)
```

파일 수 비교:
- 롤업 없이: 연간 ~2,500개
- 롤업 적용: 연간 ~90개

---

## 커밋 컨벤션

```
setup:     초기 설정, 환경 구성
plan:      계획 수립 또는 변경
decision:  중요 의사결정 기록
fix:       오류 해결 기록
update:    기존 내용 업데이트
chore:     자동화, 롤업 등 유지보수
```
