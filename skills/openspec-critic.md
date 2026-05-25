# Critic & Validator

Description: A strict validation loop to prevent hallucinations, false successes, and regressions.
Trigger: Must be run before marking any item in tasks/todo.md as complete.

## Execution Rules

Do not trust your own previous output. You must assume the implementation is flawed until proven otherwise.

### Verify State:

- Did the code actually change? Run git diff or read the file.
- Does it strictly adhere to Python 3.10+ type annotations (typing.Self, standard collections)?
- Are NumPy docstrings present on all new public methods?

### Execute Proof:

- You MUST run uv run ruff check --fix and uv run ruff format.
- You MUST run the relevant test suite via uv run pytest.
- Do not hallucinate the test output. Read the actual stderr/stdout.

### Evaluate:

- If tests fail, or Ruff complains, the validation FAILED. Do not apologize. Go fix the root cause.
- If a fix feels "hacky", reject it. Ask yourself: "Would a staff engineer approve this?"
- If validation passes, you may mark the task complete.