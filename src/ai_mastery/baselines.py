"""A deterministic Day-3 baseline to refactor and benchmark later.

This is an example *rule-based* classifier, NOT a trained machine-learning model.
It is purposely tiny: expand categories, define evaluation data, and test failures
yourself instead of using this as a finished exercise solution.
"""

def classify_message(message: str) -> str:
    """Classify messages with a deterministic keyword rule.

    Args:
        message: Input text (must be a string).

    Returns:
        One of "security" or "other".
    """
    if not isinstance(message, str):
        raise TypeError("message must be a string")
    lowered = message.casefold()
    if any(keyword in lowered for keyword in ("phishing", "password", "malware")):
        return "security"
    return "other"
