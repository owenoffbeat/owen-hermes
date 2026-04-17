# 프로젝트: 쇼핑몰 판매/광고 데이터 통합 분석 시스템

created: 2025-04-17
status: 계획 단계

## 배경

Owen은 쿠팡, 스마트스토어, G마켓, 옥션에서 보조배터리/휴대폰충전기 등 전자제품을 판매 중.
각 플랫폼의 판매 데이터와 광고 데이터를 통합해서 분석하고 싶음.

## 목표

- 기간별 통합 매출/광고 KPI 조회
- AI 에이전트가 자동으로 그로스 포인트 제안
- 문제 조기 경보 (재고부족, 광고 적자, 매출 급락 등)
- Telegram으로 일일 리포트 자동 수신

## 아키텍처

```
각 마켓 API → 데이터 수집 스케줄러 → PostgreSQL
                                          ↓
                                    FastAPI 백엔드
                                   ↙            ↘
                           React 대시보드    AI 에이전트 시스템
                                              (Hermes delegate_task)
```

## AI 에이전트 구성

| 에이전트 | 역할 |
|---------|------|
| Data Analyst | 매출 패턴 분석, 이상 감지 |
| Competitor Intel | 경쟁 제품 가격/리뷰 모니터링 |
| Growth Hacker | ROAS 최적화, 전환율 개선 제안 |
| Alert | 재고부족/매출하락/광고적자 경보 |
| Reporter | 결과 취합 → Telegram 리포트 |

## 기술 스택

- Backend: FastAPI (Python)
- DB: PostgreSQL + TimescaleDB
- Frontend: React + Recharts
- Scheduler: APScheduler
- Agent: Hermes delegate_task

## 플랫폼 API 현황

| 플랫폼 | API | 수집 가능 데이터 |
|--------|-----|----------------|
| 쿠팡 | Coupang Wing API | 주문, 정산, 광고(ROAS/클릭/노출) |
| 스마트스토어 | Naver Commerce API | 주문, 정산, 광고 |
| G마켓/옥션 | ESM Plus API | 주문, 정산 (광고 제한적) |

## 진행 단계

- [ ] 1단계: DB 설계 + 각 플랫폼 API 연동 + 데이터 수집
- [ ] 2단계: 기본 대시보드 (KPI 카드 + 차트)
- [ ] 3단계: AI 에이전트 분석 시스템
- [ ] 4단계: 경보 + Telegram 자동 리포트

## 미확인 사항

- [ ] 서버 환경 (Ubuntu/클라우드?)
- [ ] 각 플랫폼 API 키 발급 여부
- [ ] 우선 연동할 플랫폼
