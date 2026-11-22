#!/usr/bin/env python

"""
This script was developed as a product of the AI Engineering Master Course developed by ChatGPT and Dr. Briant Becote
Prompt: 
Day 003
Python mini-lab: Implement the rule baseline
Today's challenge is to Your task is to write two original pytest tests One should verify the threshold boundary (4, 5, and 6 failures). The other should verify that a negative count raises ValueError.
For the second test, pytest.raises(ValueError) is useful.
"""

def suspicious_login(failed_attempts: int, threshold: int = 5) -> bool:
    """Flag a login when failures reach the threshold."""
    if failed_attempts < 0:
        raise ValueError("failed_attempts cannot be negative")

    if threshold < 1:
        raise ValueError("threshold must be positive")

    return failed_attempts >= threshold


if __name__ == "__main__":
    for attempts in [2, 5, 9]:
        print(attempts, suspicious_login(attempts))
