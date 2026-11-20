#!/usr/bin/env python

"""
This script was developed as a product of the AI Engineering Master Course developed by ChatGPT and Dr. Briant Becote
Prompt: 
Python mini-lab: build a taxonomy classifier
Your mission is to create a defensible taxonomy of six real or hypothetical systems and put the first original implementation into GitHub.
- Build the classifier
- Create six case studies
- Write three tests
- Document limitations
"""

from ai_taxonomy import SoftwareSystem


def test_symbolic_ai():
    chess_master = SoftwareSystem("ChessMaster", "symbolic AI")
    assert chess_master.AI_classifications == {"AI"}

def test_trained_on_data():
    xray_classifier = SoftwareSystem("XrayClassifier", "trained on data")
    assert xray_classifier.AI_classifications == {"AI", "ML"}

def test_uses_deep_neural_network():
    grammerly = SoftwareSystem("Grammerly", "uses deep neural network")
    assert grammerly.AI_classifications == {"AI", "ML", "DL"}