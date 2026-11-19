# Daily task: GitHub context contract

The daily 5 AM task must perform a short, **read-only** project context check, if and only if it can access the repository, before composing the standard curriculum lesson.

## Evidence priority

1. `learning/state.yaml`: confirmed topic, learning competence, next action, open questions, last reviewed commit (human-approved state).
2. `learning/daily_brief.md`: concise state rendering; inspect its `Generated at` value and treat it as stale when older than 7 days or inconsistent with `state.yaml`.
3. `learning/handovers/`: latest relevant accepted handover (avoid guessing which is latest).
4. Recent PRs, changed files, tests and CI: observations from actual accessible repo tools only; do not treat a green CI check as proof of learning mastery.
5. `docs/reviews/`: recorded issues, correction status and review outcomes.
6. `curriculum/udemy_course_map.yaml`: approved daily course-to-lecture mapping and independent GitHub build quests; consult for any matching calendar day, if accessible.

## Daily output

- **Scheduled:** Day N / Week W / roadmap topic, independent of learner completion.
- **Progress evidence checked:** repository URL, path(s) checked, last reviewed SHA/CI status *only if actually observed*. If not accessible: `Repository not inspected (access unavailable)`.
- **Personalization:** up to 3 concrete adjustments based on verified open questions, remediation needs or incomplete exercises. Never invent personal progress.
- **Today's lesson:** substantive explanation, worked numerical or code example, practical exercise, source link, acceptance criteria, 3–5 questions and what to commit when completed.
- **Guided lab when mapped:** use the named course lecture topic(s) and independent Build Quest for today's scheduled day. State that paid course access may not exist; the probability course purchase is deferred, so supply a free substitute. Keep original implementation and evaluation distinct from reproducing an instructor demonstration. Assign the Ed Donner Agentic Track as a **supplement** on Days 396, 398, 417, 419; use Eden Marco for primary LangGraph/MCP instruction.
- **Review checkpoints:** 7/14/28 day and boundary requirements as separate prompts; do not mark a review done without inspecting a PR/diff.

## Not permitted

- Do not claim a scheduled task automatically accesses Project-uploaded files; it cannot.
- Do not treat a remembered GitHub URL as proof of current access.
- Do not interpret code changes or commits as learner mastery without review.
- Do not read private repos without granted authorization, or automatically push/update accepted learning state from a scheduled lesson.
- Do not let missing repo access prevent daily instruction: give the lesson and one unobtrusive follow-up to reconnect/share evidence.
- Do not guess paid lecture names or claim a course was purchased or completed. If the course map is unavailable, use the general trusted resources without pretending to have consulted the map.
