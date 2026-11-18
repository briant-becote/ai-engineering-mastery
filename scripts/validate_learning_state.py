"""Validate that the declared learning state is internally consistent.

This does not independently establish that any linked review or SHA exists on GitHub.
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
VALID_STATES = {"not_started", "exploring", "practicing", "review_pending", "revision_needed", "verified"}


def validate(state: dict) -> list[str]:
    problems: list[str] = []
    if not isinstance(state, dict):
        return ["Top-level state must be a YAML mapping"]
    if state.get("timezone") != "America/Phoenix":
        problems.append("timezone must be America/Phoenix")
    if state.get("start_date_local") != "2026-11-19":
        problems.append("start_date_local must be 2026-11-19")
    calendar = state.get("calendar_lessons") or {}
    delivered = calendar.get("latest_received_day")
    if delivered is not None and (type(delivered) is not int or delivered < 1):
        problems.append("latest_received_day must be null or a positive integer")
    mastery = state.get("mastery") or {}
    competency = mastery.get("current_competency")
    if competency not in VALID_STATES:
        problems.append(f"unknown competency: {competency!r}")
    completed = mastery.get("verified_completed_days") or []
    if not isinstance(completed, list) or any(type(x) is not int or x < 1 for x in completed):
        problems.append("verified_completed_days must be a list of positive integers")
    elif completed != sorted(set(completed)):
        problems.append("verified_completed_days must be sorted and unique")
    code = state.get("code_evidence") or {}
    sha = code.get("last_reviewed_commit_sha")
    if sha is not None and (not isinstance(sha, str) or not re.fullmatch(r"[0-9a-fA-F]{7,40}", sha)):
        problems.append("last_reviewed_commit_sha must be a 7–40-character Git SHA or null")
    repo = code.get("repository_url")
    if repo is not None and (not isinstance(repo, str) or not repo.startswith("https://github.com/")):
        problems.append("repository_url must be an https://github.com URL or null")
    if competency == "verified" and not sha:
        problems.append("verified competency needs a reviewed commit SHA; do not claim mastery without evidence")
    if (mastery.get("passed_module_gates") or []) and not sha:
        problems.append("passed module gates require a reviewed commit SHA")
    return problems


def main() -> None:
    state = yaml.safe_load((ROOT / "learning" / "state.yaml").read_text(encoding="utf-8"))
    errors = validate(state)
    if errors:
        print("\n".join("ERROR: " + x for x in errors))
        raise SystemExit(1)
    print("Learning-state structure validated; actual learning mastery not independently verified.")


if __name__ == "__main__":
    main()
