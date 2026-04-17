# 트러블슈팅 히스토리

오류 발생 및 해결 내용을 기록합니다.

---

## 2025-04-17: gh CLI 설치 실패

**상황**: sudo 권한 없어서 gh CLI apt 설치 불가

**해결**: git credential.helper store + curl + GitHub API 토큰 방식으로 대체
- `~/.git-credentials`에 토큰 저장
- API 호출은 `curl -H "Authorization: token $TOKEN"` 사용
- gh CLI 없이도 레포 생성, 커밋, 푸시 모두 가능

**교훈**: sudo 없는 환경에서는 gh CLI 대신 git + curl 조합으로 충분히 GitHub 작업 가능
