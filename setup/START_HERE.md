# Start Here: AI Engineering Mastery v4

Your course plan is comprehensive; the learning system must be reliable.

**What this bundle contains:** a 616-day curriculum workbook, a Python/GitHub repository starter with passing baseline examples, project instructions, a durable learning-state file, validation/testing tools, and a daily-context snapshot mechanism.

**What this bundle does not do:** create a ChatGPT Project in your account, create/push a GitHub repository, connect a private GitHub account, or verify your personal learning progress. Those steps require your action and authorization.

1. Follow `setup/CHATGPT_PROJECT_SETUP.md`.
2. Install requirements and run `python -m pytest -q`, `python -m ruff check .`, `python scripts/validate_learning_state.py`.
3. Push the repository to GitHub, configure authorized access, and update `learning/state.yaml` with your actual URL.
4. On substantial changes, run `python scripts/build_daily_brief.py`, review and commit the generated brief.
5. Use `setup/PROJECT_INSTRUCTIONS.txt` in the ChatGPT Project and open the interactive `00 — Course HQ` and M01 chats.
6. The existing daily automation has separately been updated to 5 AM Arizona time. It should read the GitHub source if connected; otherwise it must indicate that code review was not possible.
