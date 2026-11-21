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

def classify(evidence: dict) -> set[str]:
    labels = set()

    if evidence.get("learns_from_data", False):
        labels.update({"AI", "ML"})

    if evidence.get("uses_deep_network", False):
        labels.update({"AI", "ML", "DL"})

    if evidence.get("symbolic_reasoning", False):
        labels.update({"AI", "Symbolic"})

    if evidence.get("generates_content", False):
        labels.update({"AI", "Generative"})

    if evidence.get("autonomous_actions", False):
        labels.update({"AI", "Agentic"})

    return labels