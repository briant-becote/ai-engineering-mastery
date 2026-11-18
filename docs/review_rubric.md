# Weighted engineering code-review rubric

| Dimension | Weight | Evidence |
|---|---:|---|
| Conceptual correctness | 20% | Formula / algorithm validity; reference numerical comparison |
| Tests and robustness | 15% | Unit, integration, edge-case and failure-mode tests |
| Experimental validity | 15% | Honest baseline, leakage controls, suitable metrics |
| Reproducibility and provenance | 10% | Seeds, versions, data source, run commands |
| Code quality | 10% | Modular and readable code, useful names and typing |
| Error analysis | 10% | Bad examples, uncertainty, alternative hypotheses |
| Safety and security | 10% | No secrets/private data; justified trust boundaries |
| Communication | 10% | README, tradeoffs, honest limitations |

Every dimension receives 0–4: 0 absent, 1 partial, 2 adequate, 3 strong, 4 excellent. Weighted total = sum(weight * (dimension_score / 4)). A reviewer may mark **Not reviewed** when source isn't available; don't invent scores.

A critical flaw blocks a pass regardless of numeric total. Core modules target 80/100; capstones 85/100. Severity and exact lines must accompany feedback.
