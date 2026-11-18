# AI Engineering Mastery

### From first principles to production systems.

**A public, implementation-driven journey through the mathematics, algorithms, engineering practices, and research that power modern AI.**

[![Python checks](https://github.com/briant-becote/ai-engineering-mastery/actions/workflows/ci.yml/badge.svg)](https://github.com/briant-becote/ai-engineering-mastery/actions/workflows/ci.yml)

> **The goal isn't to collect AI demos. It's to understand why systems work, build them from the ground up, measure what they do, and learn how to make them reliable.**

## 👋 Welcome

I'm building this repository as a long-term, evidence-driven portfolio of AI engineering. It documents the full journey: from vectors, gradients, probability, and classical machine learning to neural networks, computer vision, language models, multimodal systems, reinforcement learning, agents, deployment, evaluation, and security.

My starting point includes hands-on experience working with AI systems, but practical familiarity is not a substitute for mathematical intuition or first-principles understanding. This project deliberately starts with the fundamentals and earns its way toward more complex work.

The roadmap contains **19 modules, 88 weeks, and 616 scheduled learning days**. Those numbers describe the *curriculum*, not a claim of completed work. Mastery is established through implementations, experiments, tests, and reviews—not by the passage of time.

**Current progress:** The repository is in its initial foundation stage. For verified milestones, see [`learning/state.yaml`](learning/state.yaml) and the associated source code, tests, and review evidence.

## 🧠 What I'm working toward

By the end of this program, I want to be able to:

- **Explain the math:** derive and reason about the linear algebra, probability, optimization, and learning objectives behind AI models.
- **Implement the fundamentals:** build core algorithms and architectures before depending on high-level frameworks.
- **Train and evaluate models:** design appropriate data splits, baselines, experiments, error analyses, and reproducible comparisons.
- **Engineer complete systems:** integrate models with data pipelines, retrieval, tools, APIs, infrastructure, observability, and deployment workflows.
- **Test the failure modes:** evaluate robustness, data leakage, adversarial behavior, privacy, and security—not just happy-path accuracy.
- **Read and reproduce research:** connect academic claims to executable experiments and clearly report limitations.

This isn't solely an LLM or chatbot project. The portfolio will span tabular machine learning, vision, NLP, audio, generative models, reinforcement learning, multimodal AI, and production engineering.

## 🗺️ The learning roadmap

| Track | Modules | Focus |
| --- | --- | --- |
| **I · Foundations** | M01–M05 | AI foundations, linear algebra, calculus and optimization, probability and statistics, classical ML |
| **II · Deep learning** | M06–M08 | Neural networks and PyTorch, computer vision, NLP foundations |
| **III · Language models** | M09–M11 | Transformers and LLM internals, training systems, fine-tuning and alignment |
| **IV · Intelligent systems** | M12–M15 | Retrieval and RAG, agents and MCP, generative and multimodal AI, reinforcement learning and related methods |
| **V · Engineering and research** | M16–M19 | MLOps and inference, evaluation, AI security and governance, independent research and capstones |

The [curriculum](curriculum/) specifies lesson topics, resources, deliverables, and review checkpoints. Daily lessons provide structure; actual progress can move faster or slower than the calendar.

## 🛠️ The build portfolio

Every major module aims to produce a small but defensible engineering artifact. Examples of the planned work include:

| Engineering challenge | Core questions | Stage |
| --- | --- | --- |
| **Rules vs. learning** | When is a hand-built rule enough? How do we compare it fairly with a learned baseline? | Starter stage |
| **Optimization from scratch** | Why does gradient descent converge—or fail? How do numerical checks expose incorrect derivatives? | Planned |
| **Neural networks and vision** | Can I implement backpropagation, train a vision model, and explain its errors? | Planned |
| **A small language model** | How do tokenization, attention, training objectives, and sampling fit together? | Planned |
| **Retrieval and agent systems** | Can a system find trustworthy evidence, use tools safely, and be evaluated systematically? | Planned |
| **Production AI and security** | Can I deploy, monitor, benchmark, stress-test, and secure an AI service? | Planned |

**The status labels are intentional.** A project moves from *planned* to *implemented* to *reviewed* only when the repository contains appropriate evidence. Explore the [module projects](projects/) and the [learning-state record](learning/state.yaml) for the current picture.

## ⚙️ How I approach the work

I use a repeatable engineering loop:

**Understand → Derive → Implement → Test → Experiment → Review → Improve**

For each substantial project, I aim to preserve:

1. **Problem framing:** purpose, assumptions, baseline, and success criteria.
2. **Original implementation:** clear code that exposes the mechanism rather than hiding it behind a library.
3. **Validation:** unit tests, numerical checks, and edge cases.
4. **Evaluation:** appropriate metrics, controlled comparisons, and error analysis.
5. **Reproducibility:** environment, dependencies, seeds, dataset provenance, and commands.
6. **Engineering reflection:** limitations, tradeoffs, what failed, and what I would change next.

The [experiment template](docs/experiment_template.md) and [review rubric](docs/review_rubric.md) make these expectations explicit.

### Feedback and mastery checks

This portfolio includes structured checkpoints: **weekly reflection**, **substantive code review every 14 days**, **deeper engineering review every 28 days**, and **a competency gate at each module boundary**. Review findings should point to specific code and evidence; a passing test alone does not prove an algorithm is correct.

An AI assistant supports instruction, questioning, and review, but its suggestions are treated as hypotheses until checked against source code, tests, references, or reproducible results. See the [review protocol](docs/review_protocol.md) for the standards.

## 🔎 Explore the repository

| Location | What you'll find |
| --- | --- |
| [`projects/`](projects/) | Module-by-module implementations and experiments as they develop |
| [`src/ai_mastery/`](src/ai_mastery/) | Reusable Python implementation code |
| [`tests/`](tests/) | Automated checks for reusable components |
| [`docs/`](docs/) | Experiment templates, review rubrics, technical notes, and review records |
| [`learning/`](learning/) | Verified progress, open questions, decisions, and concise handoffs |
| [`curriculum/`](curriculum/) | The long-form roadmap and review schedule |
| [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | Configured automated Python checks |

**A good first stop:** [`projects/m01-orientation/`](projects/m01-orientation/) for the foundations, then [`docs/review_protocol.md`](docs/review_protocol.md) to understand how work is evaluated.

## 🚀 Run the starter checks

**Requirements:** Python 3.11+ and Git. The initial checks are CPU-friendly; later experiments may have additional requirements.

```bash
git clone https://github.com/briant-becote/ai-engineering-mastery.git
cd ai-engineering-mastery
python -m venv .venv
```

Activate the virtual environment (`.venv\Scripts\Activate.ps1` on Windows PowerShell or `source .venv/bin/activate` on macOS/Linux), then run:

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
python -m ruff check .
python scripts/validate_learning_state.py
```

The GitHub Actions workflow is configured to run Python checks on pushes and pull requests. A green check indicates only that the configured checks passed for that run; substantive model claims require separate experimental evidence.

## 📚 Learning resources and attribution

The curriculum draws on a combination of original implementations, open educational resources, academic papers, and guided practical labs. Recurring references include:

- [AI Engineering from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch)
- [Introduction to Statistical Learning](https://www.statlearning.com/) and [Dive into Deep Learning](https://d2l.ai/)
- [Sebastian Raschka's *Build a Large Language Model (From Scratch)* companion code](https://github.com/rasbt/LLMs-from-scratch)
- [Stanford CS336](https://cs336.stanford.edu/), [Hugging Face Learn](https://huggingface.co/learn), and [DataTalks.Club](https://github.com/DataTalksClub)

Where an implementation follows an external exercise, paper, or tutorial, I'll identify the source and what I changed or verified independently. Third-party materials and datasets retain their respective licenses; paid course content is not redistributed here.

## 🤝 Why make the process public?

Because the engineering journey is as valuable as the destination. The aim is to show not only polished results, but also the experiments, corrections, design decisions, and evidence that led to them.

**Questions, technical discussion, and constructive feedback are welcome.** This repository is a work in progress—deliberately, transparently, and with a lot left to build. 🔥
