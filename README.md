# AI Engineering Mastery — implementation portfolio

**Purpose:** turn a long-form AI curriculum into demonstrated capability. This is a starter repository, **not** a completed portfolio. The example baseline is intentionally small so you can expand it yourself.

**New: Start with [`setup/CHATGPT_PROJECT_SETUP.md`](setup/CHATGPT_PROJECT_SETUP.md) to configure the ChatGPT Project, GitHub authorization, and the 5 AM project-aware lesson workflow.** The complete curriculum workbook is now included in [`curriculum/`](curriculum/).

## Learning contract

- For each module, create original implementations before framework-based versions.
- A working notebook is not sufficient: include tests, a baseline, error analysis, reproducible steps and a documented tradeoff.
- Every **7 days**: self-review and update your progress. Every **14 days**: open a PR and invite substantive code review. Every **28 days**: deep review. At each **module boundary**: complete a competency gate before claiming mastery.
- Every **1, 4 and 12 weeks**, revisit prior implementations without notes and confirm you can still explain and change them.
- Publish only material you own or are permitted to share. **Never commit API keys, personal records, private documents, paid course content or model licenses you cannot redistribute.**
- The calendar is a delivery cadence, not a requirement to finish complex lab work on a fixed date.

## Starter requirements

- Python 3.11+ and Git. No GPU is needed for the starter project.
- Create an isolated virtual environment. The optional lint/test dependencies are small.

**Windows PowerShell**

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
python -m pytest -q
python -m ruff check .
```

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
python -m pytest -q
python -m ruff check .
```

## Repository layout

```text
.github/                 Pull-request, review-issue and CI templates
docs/                    Review protocol, research and experiment templates
docs/reviews/            Weekly reflection and review records
projects/m01-...m19-*/   One folder per learning module
src/ai_mastery/          Reusable implementation code
tests/                   Fast unit tests for reusable code
datasets/                Dataset manifests ONLY, not raw private/big data
```

Review the [repository workflow](docs/review_protocol.md), [rubric](docs/review_rubric.md), and [experiment template](docs/experiment_template.md).

## Recommended workflow

```bash
git init
git add .
git commit -m "Initialize AI engineering mastery portfolio"
git branch -M main
# Create an EMPTY repository on GitHub first. Then substitute YOUR URL:
git remote add origin https://github.com/YOUR-USER/ai-engineering-mastery.git
git push -u origin main
git switch -c feature/m01-rule-baseline
# Develop, test, commit and push your work; open a PR on GitHub.
```

GitHub's private/public setting is your choice. Starting **private** is reasonable until you've checked licenses and sanitized data.

## Reviewing work with ChatGPT

At a review checkpoint, give ChatGPT the PR URL or commit SHA and the specific scope. If GitHub is private, connect an authorized GitHub integration if available, or upload a ZIP/diff. **A calendar notification cannot inspect a repository that isn't accessible.** See [`docs/review_request.md`](docs/review_request.md) for the exact feedback request.

## Reliable long-term learning context

See [`learning/README.md`](learning/README.md) for the interactive ChatGPT Project and versioned session/handoff workflow, and copy [`learning/chatgpt_project_instructions.md`](learning/chatgpt_project_instructions.md) into your Project instructions. The 5 AM lessons are calendar-based; only evidence-backed, user-approved updates to `learning/state.yaml` change mastery progress.

## Curriculum

The curriculum progress spreadsheet is delivered separately. Its `Daily Lessons` tab includes per-lesson repo evidence; `GitHub Review Queue` specifies review dates and gates.

## Project-aware daily learning (5:00 AM America/Phoenix)

The scheduled lesson checks authorized GitHub sources when available; it cannot automatically read files uploaded to a ChatGPT Project. Follow [`learning/automation_context_contract.md`](learning/automation_context_contract.md) and keep `learning/state.yaml` current through accepted changes. After state changes, generate a concise status snapshot:

```bash
python scripts/validate_learning_state.py
python scripts/build_daily_brief.py
```

Review the generated `learning/daily_brief.md` and commit it with the state update. This is a read-only snapshot of state, not proof that the models or tests ran.
