# Review protocol

| Cadence | Student evidence | Reviewer action |
|---|---|---|
| Every 7th day | Weekly notes, tests, one recorded failure, next action | Self-review or optional feedback |
| Every 14th day | PR/diff, run commands, new tests, 2–3 focused questions | Review actual changed source for correctness, test quality, reproducibility |
| Every 28th day | All recent PRs, experimental results, failed cases, architecture choices | Deep holistic review, 8-dimension rubric and prioritized fixes |
| Every module end | From-scratch implementation, reference framework, metrics, README, reproducible run | Module competency gate: pass, conditional pass or remediation |

At colliding dates, do one combined review with all applicable criteria. The learning-calendar date is the **review invitation**, not proof that code has been reviewed.

## Review grading

Use the [weighted rubric](review_rubric.md). Reviewer should cite actual files and lines/commit, assign **Critical, High, Medium or Low** issue severity, provide concrete failing tests or reproducible steps, and prioritize the three most valuable fixes. Strong areas should be documented as well.

**Minimum passing quality:** 80/100 for a module, 85/100 for final capstones, with no unresolved critical correctness, data leakage or security issue. A score should never be assigned without examining accessible source and evidence.

## Post-review loop

1. Open actionable issues for high-severity findings.
2. Create a new commit including a regression test.
3. Rerun tests and replicate important metrics.
4. Request a narrow re-review and update the workbook queue.
5. Tag `mXX-complete` only after the mastery gate actually passes.

**Reminder:** A private GitHub repo is not visible to a reviewer by default. Share a public repo and PR URL or use an explicitly authorized GitHub connection/ZIP attachment.
