#!/usr/bin/env python

"""
This script was developed as a product of the AI Engineering Master Course developed by ChatGPT and Dr. Briant Becote
Prompt: 
Day 003
Python mini-lab: Implement the rule baseline
Today's challenge is to Your task is to write two original pytest tests One should verify the threshold boundary (4, 5, and 6 failures). The other should verify that a negative count raises ValueError.
For the second test, pytest.raises(ValueError) is useful.
"""

from unittest import TestCase

from rule_baseline import suspicious_login


class TestSuspiciousLogin(TestCase):
    def test_threshold_boundary(self):
        self.assertFalse(suspicious_login(4))
        self.assertTrue(suspicious_login(5))
        self.assertTrue(suspicious_login(6))

    def test_negative_count_raises_value_error(self):
        with self.assertRaises(ValueError):
            suspicious_login(0)
            suspicious_login(-1)