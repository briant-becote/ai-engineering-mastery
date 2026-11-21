#!/usr/bin/env python

"""
This script was developed as a product of the AI Engineering Master Course developed by ChatGPT and Dr. Briant Becote
Prompt: 
Day 002
Python mini-lab: build a taxonomy classifier
Today's challenge is to classify systems using structured evidence rather than matching an entire description string.
Your mission is to add two original tests:
- A hybrid system with both uses_deep_network=True and autonomous_actions=True should receive both DL and Agentic, along with their implied labels.
- A system with generates_content=True and no learning evidence should receive Generative without automatically receiving ML or DL.
"""

from formal_taxonomy import classify


def test_symbolic_ai():
    chess_master = {"symbolic_reasoning":True}
    assert classify(chess_master) == {"AI", "Symbolic"}

def test_trained_on_data():
    agentic_AI = {"uses_deep_network":True, "autonomous_actions":True}
    assert classify(agentic_AI) == {"AI", "ML", "DL", "Agentic"}