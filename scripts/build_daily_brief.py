"""Produce a compact, human-reviewed GitHub-readable context snapshot.

This script reads state.yaml but never advances mastery. It does not push commits.
Usage: python scripts/build_daily_brief.py [--as-of YYYY-MM-DD]
"""
from __future__ import annotations

import argparse
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml

ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "learning" / "state.yaml"
BRIEF_PATH = ROOT / "learning" / "daily_brief.md"


def render(state: dict, as_of: str) -> str:
    calendar = state.get("calendar_lessons", {})
    mastery = state.get("mastery", {})
    code = state.get("code_evidence", {})
    def bullets(items):
        return "\n".join("- " + str(x) for x in (items or [])) or "- None recorded"
    return f"""# AI Engineering Mastery — Daily Context Snapshot

> Generated at: {as_of} (America/Phoenix). This is a rendering of learner-approved `learning/state.yaml`, not independent code verification.

## Delivered lessons (calendar only)
- Latest delivered lesson: {calendar.get('latest_received_day') or 'not recorded'}
- Latest delivered date: {calendar.get('latest_received_date') or 'not recorded'}

## Current verified learning state
- Active module: {mastery.get('active_module') or 'unknown'}
- Topic: {mastery.get('active_topic') or 'unknown'}
- Competency: {mastery.get('current_competency') or 'unknown'}
- Module gates passed: {', '.join(mastery.get('passed_module_gates') or []) or 'none'}

## GitHub evidence
- Repository: {code.get('repository_url') or 'not configured'}
- Last reviewed commit: {code.get('last_reviewed_commit_sha') or 'not reviewed'}
- Review outcome: {code.get('last_review_outcome') or 'not recorded'}
- Last verified test result: {code.get('last_verified_test_result') or 'not recorded'}

## Next agreed actions
{bullets(state.get('next_actions'))}

## Open questions
{bullets(state.get('open_questions'))}

## How to use this
Scheduled lessons should read `learning/state.yaml` first when available and treat this as a convenience summary. Check repository access and staleness explicitly. If the file is inaccessible, say so; do not infer progress from the schedule.
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of", default=datetime.now(ZoneInfo("America/Phoenix")).date().isoformat())
    args = parser.parse_args()
    date.fromisoformat(args.as_of)
    state = yaml.safe_load(STATE_PATH.read_text(encoding="utf-8"))
    BRIEF_PATH.write_text(render(state, args.as_of), encoding="utf-8")
    print(f"Rendered {BRIEF_PATH.relative_to(ROOT)} from {STATE_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
