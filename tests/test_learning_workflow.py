"""Test contract invariants; never treat synthetic test data as real progress."""
import copy
from pathlib import Path

import yaml

from scripts.build_daily_brief import render
from scripts.validate_learning_state import validate

STATE = yaml.safe_load((Path(__file__).resolve().parents[1] / "learning" / "state.yaml").read_text())


def test_initial_state_is_valid():
    assert validate(STATE) == []


def test_cannot_claim_verified_without_reviewed_commit():
    state = copy.deepcopy(STATE)
    state["mastery"]["current_competency"] = "verified"
    assert any("reviewed commit" in p for p in validate(state))


def test_duplicate_day_detected():
    state = copy.deepcopy(STATE)
    state["mastery"]["verified_completed_days"] = [1, 1]
    assert any("sorted and unique" in p for p in validate(state))


def test_daily_brief_is_transparent_about_evidence():
    brief = render(STATE, "2026-11-18")
    assert "not reviewed" in brief
    assert "not configured" in brief
    assert "not independent code verification" in brief
