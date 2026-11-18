"""Minimal first tests. Add boundaries and a learned comparison yourself."""

import pytest

from ai_mastery.baselines import classify_message


@pytest.mark.parametrize(
    ("message", "label"),
    [
        ("Password reset required", "security"),
        ("Reported malware on laptop", "security"),
        ("Meeting at noon", "other"),
        ("", "other"),
    ],
)
def test_rule_based_examples(message: str, label: str) -> None:
    assert classify_message(message) == label


def test_bad_input_fails_explicitly() -> None:
    with pytest.raises(TypeError):
        classify_message(None)  # type: ignore[arg-type]
