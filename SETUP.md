# AI Agent Workspace Setup Guide

This guide explains how to bootstrap an individual repository (e.g., `ntfy_lite` or `pyRobocopy`) to consume this centralized organizational "brain" repository as an external dependency.

By using this setup, you ensure that local AI agents have immediate access to standard personas, instructions, and verification scripts while keeping the global config read-only and robust against developer workspace pollution.

---

## 1. Adding the Central Brain Submodule

Run the following command at the root of the consumer repository to add the centralized `.github` repository as a Git Submodule located at `.agents/global/`:

```bash
git submodule add https://github.com/MCRE-BE/.github.git .agents/global
```

---

## 2. Preventing Submodule Dirty State Confusion

Because AI agents frequently write temporary files or make exploratory edits, we must isolate the submodule status so it does not pollute the consumer repo's `git status` or break agent committing routines.

Open or create the `.gitmodules` file at the root of your consumer repository and append the `ignore = dirty` configuration:

```ini
[submodule ".agents/global"]
    path = .agents/global
    url = https://github.com/MCRE-BE/.github.git
    ignore = dirty
```

*Rationale:* This prevents local edits or uncommitted logs inside `.agents/global/` from showing up as modified files in the consumer repo's git history, ensuring smooth commits and preventing AI agent retry loops.


---

## 3. Standardizing Ruff Linting & Formatting

To ensure consistent enforcement of linting rules, NumPy docstrings, and trailing commas without copy-pasting code or maintaining duplicate setups, you can extend the organization's centralized `ruff.toml` directly.

Choose **one** of the following methods in the root of your consumer repository:

### Method A: Extending via a local `ruff.toml`
Create a `ruff.toml` file at your repository's root containing:

```toml
extend = ".agents/global/ruff.toml"
```

### Method B: Extending via a local `pyproject.toml`
If you already use a `pyproject.toml` file, append the following block to it:

```toml
[tool.ruff]
extend = ".agents/global/ruff.toml"
```

*Rationale:* This tells Ruff to inherit all organization-wide standards (like rules, quote styles, and NumPy docstring conventions). You can still override specific settings locally in your extending file if needed, keeping your workspace configuration clean while staying fully aligned.

---

## 4. Bootstrapping IDE AI Agents (Symlinking)

Editor-native AI tools (like Cursor, Windsurf, or Clinch) scan the workspace root for custom rules. To feed the centralized instructions directly to the IDE's built-in agents without duplicating code:

Create a bootstrap script (e.g., `bootstrap.sh` or `bootstrap.bat`) at the root of the repository, or run the following symlink commands manually:

### Linux / macOS
```bash
ln -sf .agents/global/AGENTS.md .cursorrules
ln -sf .agents/global/AGENTS.md .windsurfrules
ln -sf .agents/global/PULL_REQUEST_TEMPLATE.md .github/PULL_REQUEST_TEMPLATE.md
```

### Windows (PowerShell - run as Administrator)
```powershell
New-Item -ItemType SymbolLink -Path ".cursorrules" -Target ".agents/global/AGENTS.md" -Force
New-Item -ItemType SymbolLink -Path ".windsurfrules" -Target ".agents/global/AGENTS.md" -Force
New-Item -ItemType SymbolLink -Path ".github/PULL_REQUEST_TEMPLATE.md" -Target ".agents/global/PULL_REQUEST_TEMPLATE.md" -Force
```

---

## 5. Programmatic Verification Loop (AI Agents Only)

To prevent AI agents from "marking tasks as complete" without actually verifying their code, we utilize a centralized verification engine. This check is run programmatically by the AI agent during the verification stage, and does not block human developers locally.

### Executing Verification

During **Step 4 (Verify)** of the agent workflow, the agent must run:

```bash
uv run python .agents/global/scripts/verify.py
```

This script programmatically validates:
1. **Task Completeness:** Parses `tasks/todo.md` to ensure zero pending `[ ]` or in-progress `[/]` tasks remain.
2. **Linting Gates:** Ensures `uv run ruff check .` passes without errors.
3. **Formatting Gates:** Ensures `uv run ruff format --check .` is clean.
4. **Test Gates:** Runs `uv run pytest -v` (if a `tests/` directory exists).

If any check fails, the script returns a non-zero exit code, raising an immediate error in the agent's workflow and forcing it to self-correct before presenting the code to the user or making a commit.

