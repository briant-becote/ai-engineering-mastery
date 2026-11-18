# Durable learning context

The purpose of this folder is **reliable continuity**, not exhaustive logging. Keep a few short, human-reviewable files that can be understood without access to 616 chat histories.

| File | Purpose | Update cadence |
|---|---|---|
| `state.yaml` | Current *verified* progress and next steps | End of substantial session and after each assessment |
| `open_questions.md` | Questions, misconceptions and unresolved experiments | As questions arise |
| `decisions.md` | Curriculum and architecture decisions with reasoning | When decisions change |
| `handovers/` | Short module or chat rollover handoffs | At every module boundary or when a chat becomes unwieldy |
| `weekly_review_template.md` | Evidence-based 7-day summary | Weekly |
| `session_protocol.md` | Operational rules for interactive instruction and continuity | Stable; revise deliberately |
| `chatgpt_project_instructions.md` | Suggested instructions for a single ChatGPT Project | When teaching protocol changes |

## What is authoritative?

1. Repository source code and immutable Git commit SHA: what exists.
2. Tests, experiment outputs, review notes tied to that SHA: what was verified.
3. `learning/state.yaml`, manually accepted or confirmed by the learner: curriculum progress.
4. Current dialogue: goals, questions, emerging ideas, but not evidence of completed work.
5. ChatGPT memories and prior chat summaries: helpful leads, **never sufficient proof**.

**Scheduling is separate from mastery.** The 5 AM lesson may say Day N, but it must not silently advance `verified_completed_days` or `module_gate_status`.

## Minimal cycle

1. Open the ChatGPT Project's chat for the current module.
2. Share the current repository/commit and `learning/state.yaml` if it is not already accessible through an authorized connection.
3. Choose **Explore**, **Practice**, **Review code**, **Assess mastery** or **Resume**.
4. Work interactively until the session naturally concludes. You may spend days on one concept.
5. End with `Session handoff`: a small proposed update for `state.yaml`, `open_questions.md`, and any commit/review request.
6. **Review and approve** before the changes enter the repository. A chat response never constitutes a Git commit.
