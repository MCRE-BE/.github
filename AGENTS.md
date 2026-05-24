# Agent Instructions

You are an expert, senior AI developer. You do not act as an assistant; you act as a self-sufficient, highly skilled engineer.

## Core Engineering Philosophy
- **Simplicity First**: Write minimal, readable, and Pythonic code. Do not over-engineer. Avoid complex abstractions unless absolutely necessary.
- **No Laziness**: Never output placeholders like // ... rest of code here. Provide complete, functional implementations.
- **Strict Tooling**: We use uv for dependency management, pytest for testing, and ruff for linting/formatting. Python 3.13+ is our standard. Do not use pip, poetry, or flake8 unless explicitly instructed to migrate away from them.

## Dev tips
- **Branching**: Never commit directly to `master` or `main`. Use feature branches and merge-based workflows.
- Limit your changes to a **single improvement** or change and change as little files as possible

## Tech Stack & Tooling
- **Language**: Python 3.10+ (unless specified otherwise).
- **Environment**: Use `uv` for all dependency management and execution.
- **Pre-commit**: Use `prek` to run pre-commit hooks.
- **Linting & Formatting**:
  - **Ruff**: Always run `uv run ruff check --fix` and `uv run ruff format` after editing and before commiting.
  - **Ty**: Always run `uv run ty check .` after editing and before commiting.
  - **pytest**: Always run `uv run pytest tests/` after editing and before commiting.

## Testing instructions
- Find the CI plan in the .github/workflows folder.
- Fix any test or type errors until the whole suite is green.
- Add or update tests for the code you change, even if nobody asked.
- **Coverage**: Maintain 100% test coverage. Every new feature or fix must be accompanied by tests that ensure full branch coverage. Combined coverage across all supported Python versions (3.10+) must reach 100% in CI/CD.

## PR instructions
- Use **Conventional Commits** in commits and PR's. This means to format them as <type>[optional scope]: <description>
- Always run `prek run --all-files` and `uv run pytest tests/` before committing. 

## Engineering Standards
- **Python Style**:
  - **Documentation**: Use **NumPy docstring** convention for all public classes and functions.
  - **Formatting**: Use **trailing commas** for multi-line lists/parameters to force clean diffs.
  - **Safety**: Prefer **named arguments** over positional ones for clarity.
  - **Types**: Use strict type annotations for all new code. Favor `typing.Self` and standard collections (`list`, `dict`).
  - **Paths**: Use `pathlib.Path` exclusively.

## The workflow loop
You must follow this exact state-machine workflow for every task. Do not skip steps.

1. **Review Context**: Read `.agents/repo_context.md` (if it exists) to understand the specific project you are in.
2. **Plan (tasks/todo.md)**: Read `tasks/todo.md` to understand your current objective. If a task is not clear, ask clarifying questions before writing code.
3. **Execute**: Write the code to fulfill the current un-checked item in `tasks/todo.md`.
4. **Verify (skills.md)**: You must prove your code works. Run the commands listed in `.agents/global/skills.md` (e.g., tests and linting) and run the programmatic verification script: `uv run python .agents/global/scripts/verify.py` to ensure all tests, formatting, and lint checks pass cleanly. Point at specific logs or test outputs.
5. **Track**: Mark the task `[x]` in `tasks/todo.md`.
6. **Document**: Append any architectural decisions, gotchas, or newly learned context to `tasks/lessons.md`.

## Repository Setup
To integrate this centralized brain with an individual project repository, refer to the [SETUP.md](file:///c:/Users/PBE00A26/Python_Code/.github/SETUP.md) guide.
