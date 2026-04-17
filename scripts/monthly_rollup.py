#!/usr/bin/env python3
"""
월말 롤업: 지난달 일일 로그들을 summary.md로 요약하고 일일 파일 삭제
매월 1일 자정에 크론잡으로 실행
"""
import os, glob, subprocess
from datetime import datetime, timedelta

REPO = os.path.expanduser("~/owen-hermes")
AGENTS = ["orchestrator", "planner", "researcher", "builder", "critic", "reporter"]

def rollup_agent_month(agent, year, month):
    log_dir = f"{REPO}/agents/{agent}/logs/{year}/{month:02d}"
    daily_files = sorted(glob.glob(f"{log_dir}/[0-9]*.md"))
    if not daily_files:
        return

    combined = f"# {agent} — {year}/{month:02d} 월간 요약\n\n"
    for f in daily_files:
        day = os.path.basename(f).replace(".md", "")
        combined += f"## {month:02d}/{day}\n"
        with open(f) as fp:
            combined += fp.read().strip() + "\n\n"

    with open(f"{log_dir}/summary.md", "w") as fp:
        fp.write(combined)

    for f in daily_files:
        os.remove(f)

    print(f"✅ {agent} {year}/{month:02d} 롤업 완료 ({len(daily_files)}개 → summary.md)")

def rollup_daily_month(year, month):
    log_dir = f"{REPO}/daily/{year}/{month:02d}"
    daily_files = sorted(glob.glob(f"{log_dir}/[0-9]*.md"))
    if not daily_files:
        return

    combined = f"# 전체 일지 — {year}/{month:02d} 월간 요약\n\n"
    for f in daily_files:
        day = os.path.basename(f).replace(".md", "")
        combined += f"## {month:02d}/{day}\n"
        with open(f) as fp:
            combined += fp.read().strip() + "\n\n"

    with open(f"{log_dir}/summary.md", "w") as fp:
        fp.write(combined)

    for f in daily_files:
        os.remove(f)

    print(f"✅ daily {year}/{month:02d} 롤업 완료 ({len(daily_files)}개 → summary.md)")

if __name__ == "__main__":
    today = datetime.today()
    last_month = (today.replace(day=1) - timedelta(days=1))
    year, month = last_month.year, last_month.month

    for agent in AGENTS:
        rollup_agent_month(agent, year, month)
    rollup_daily_month(year, month)

    os.chdir(REPO)
    subprocess.run(["git", "add", "-A"])
    subprocess.run(["git", "commit", "-m", f"chore: {year}/{month:02d} 월간 롤업 자동 생성"])
    subprocess.run(["git", "push"])
    print("✅ GitHub 푸시 완료")
