"""AI Agent Verification Script.

This script programmatically validates that the AI agent has completed all planned
tasks in `tasks/todo.md` and that all code quality gates (ruff linting, formatting,
and pytest) are met before the agent concludes its work.
"""

import sys
import subprocess
import pathlib


def verify_todo() -> None:
    """Validate that tasks/todo.md exists and contains no pending tasks."""
    todo_path = pathlib.Path("tasks/todo.md")
    if not todo_path.exists():
        print(
            "❌ Verification Error: `tasks/todo.md` not found! Please create a plan before executing."
        )
        sys.exit(1)

    content = todo_path.read_text(encoding="utf-8")
    lines = content.splitlines()

    pending_tasks = []
    in_progress_tasks = []

    for line_num, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("- [ ]") or stripped.startswith("* [ ]"):
            pending_tasks.append(f"Line {line_num}: {stripped[5:].strip()}")
        elif stripped.startswith("- [/]") or stripped.startswith("* [/]"):
            in_progress_tasks.append(f"Line {line_num}: {stripped[5:].strip()}")

    if pending_tasks or in_progress_tasks:
        print("❌ Verification Error: Pending items found in `tasks/todo.md`!")
        if pending_tasks:
            print("\nPending tasks `[ ]`:")
            for task in pending_tasks:
                print(f"  - {task}")
        if in_progress_tasks:
            print("\nIn-progress tasks `[/]`:")
            for task in in_progress_tasks:
                print(f"  - {task}")
        sys.exit(1)

    print("✅ `tasks/todo.md` fully completed (no pending tasks).")


def run_command(args: list[str], label: str) -> None:
    """Run a shell command using uv run and print status."""
    print(f"🔄 Running {label}: {' '.join(args)}...")
    try:
        # Run under uv to ensure isolated tool versions are used
        result = subprocess.run(
            ["uv", "run"] + args, capture_output=True, text=True, check=True
        )
        print(f"✅ {label} passed.")
        if result.stdout.strip():
            print(result.stdout)
    except subprocess.CalledProcessError as err:
        print(f"❌ {label} failed!")
        if err.stdout:
            print("Stdout:")
            print(err.stdout)
        if err.stderr:
            print("Stderr:")
            print(err.stderr)
        sys.exit(err.returncode)


def main() -> None:
    """Orchestrate the programmatic AI verification pipeline."""
    print("========================================")
    print("🤖 Starting Programmatic AI Verification")
    print("========================================")

    # 1. Verify tasks list is clean
    verify_todo()

    # 2. Verify Ruff Linting
    run_command(["ruff", "check", "."], "Ruff Linter")

    # 3. Verify Ruff Formatting
    run_command(["ruff", "format", "--check", "."], "Ruff Formatter")

    # 4. Verify Type Checking
    run_command(["ty", "check", "."], "Ty Type Checker")

    # 5. Verify Pytest Suite (if tests directory exists)
    if pathlib.Path("tests").is_dir():
        run_command(["pytest", "-v"], "Pytest Suite")
    else:
        print("⚠️ No `tests/` directory found. Skipping unit tests.")

    print("========================================")
    print("🎉 Verification Successful! Clean to commit.")
    print("========================================")


if __name__ == "__main__":
    main()
