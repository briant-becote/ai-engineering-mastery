# ChatGPT Project setup — AI Engineering Mastery

This repository is ready for GitHub. **A ChatGPT Project and a GitHub repository have not been created by this ZIP.** Their creation requires actions in your accounts.

## Set up the ChatGPT Project

1. In ChatGPT, choose **New project** in the sidebar, name it `AI Engineering Mastery` and pick a project icon of your choice.
2. Choose **Default memory** initially if you want conversations to reference relevant outside context and use ChatGPT Work. If you want a strictly isolated project, switch to **Project-only memory** in settings; it cannot use Work. These settings are personal and can be changed later.
3. Open the project's instructions and paste the entire contents of `setup/PROJECT_INSTRUCTIONS.txt`. They refer to `learning/state.yaml` in your GitHub repository, not to an automatically synchronized Project upload.
4. Upload `curriculum/AI_Engineering_Mastery_v2_GitHub_Reviews.xlsx` as the **initial curriculum reference**. Optionally upload `setup/CONVERSATION_MAP.md` as a static source. Do **not** rely on Project-file uploads as the source of up-to-date progress; they are snapshots.
5. Start a conversation `00 — Course HQ` to handle schedules, curriculum adjustments, and high-level decisions. Start `M01 — Orientation & AI Foundations` for initial interactive lessons. Create the other module chats as you reach them rather than pre-creating 19 empty chats.
6. If useful, move prior curriculum-design conversations into the Project through their menu's **Move to project** option, if offered. Leave the existing 5:00 AM task associated with its current conversation unless you intentionally reconfigure it.

## Publish the GitHub repository

1. Unzip this bundle. Open a terminal in the `ai-engineering-mastery/` folder and follow its `README.md` for installing Python, running tests and publishing to GitHub.
2. Create an empty private (recommended initially) GitHub repository called `ai-engineering-mastery`.
3. Push files; record the resulting URL in `learning/state.yaml` under `code_evidence.repository_url`.
4. In ChatGPT's apps/plugin settings, connect the GitHub app and authorize the repository. The connector must be authorized to read the repo to inspect a private repository or its pull requests.
5. After initial setup and when your learning state changes, run `python scripts/build_daily_brief.py`, review `learning/daily_brief.md`, and commit both that file and the updated `learning/state.yaml`. This creates a stable short status document for the daily task to consult.

## How daily lessons use the repository

The existing daily task runs at **5:00 AM America/Phoenix**, starting **November 19, 2026**. It follows the fixed 616-day instructional sequence but *must not* infer completion from the calendar. When GitHub access works, it should first read the current repository's `learning/state.yaml`, `learning/daily_brief.md`, and relevant recent review information, then adapt the suggested exercises and mention any unresolved questions. 

The scheduled task can use supported connected apps but **cannot directly read project-uploaded files**. Therefore do not upload your changing state file solely into ChatGPT Project and expect the task to see updates. The source of truth is the GitHub repository. If GitHub is unavailable, the task should explicitly say that progress wasn't verified and give the curriculum lesson plus a simple step to restore access. It must never claim to have inspected code or run tests without doing so.

## Daily workflow

- **5 AM:** receive today's curriculum lesson and any verified context adjustments.
- **Whenever convenient:** continue in the current module's ChatGPT Project conversation, exploring examples and asking questions freely.
- **At the end of substantial sessions:** approve changes to `learning/state.yaml` and add new code/tests and handoff notes.
- **Every 7 days:** self-review. **Every 14 days:** submit a pull request for a substantive mentor review. **Every 28 days:** deep review. **At module boundaries:** competency assessment.
- **Only after actual evidence-based review:** mark a module mastered.

**A GitHub connector does not automatically create a repository, start a task, push commits, or guarantee a valid code review.** Authorization and repo permissions are required.
