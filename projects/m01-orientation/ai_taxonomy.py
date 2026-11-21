#!/usr/bin/env python

"""
This script was developed as a product of the AI Engineering Master Course developed by ChatGPT and Dr. Briant Becote
Prompt: 
Day 001
Python mini-lab: build a taxonomy classifier
Your mission is to create a defensible taxonomy of six real or hypothetical systems and put the first original implementation into GitHub.
- Build the classifier
- Write three tests
"""

class SoftwareSystem:   
    def __init__(self, name, description):
        self.name = name
        self.AI_classifications = self.classify_system(description)
        
    def classify_system(self, description):
        if description == "symbolic AI":
            return {"AI"}
        if description == "trained on data":
            return {"AI", "ML"}
        if description == "uses deep neural network":
            return {"AI", "ML", "DL"}
        if description == "evaluates and independently executes functions":
            return {"AI", "Agentic-AI"}
        if description == "generates content":
            return {"AI", "Generative-AI"}
        if description == "evaluates and generates language based on model training":
            return {"AI", "Generative-AI", "LLM"}   
        else:
            return {"Bro - do you even AI?"}