# AI Agent Superpowers: Process-Layer & Discipline (obra/superpowers)

We adopt the core principles of **`obra/superpowers`** to guarantee engineering discipline, prevent "short-circuiting" verification, and enforce structural safety across active projects:

- **Git Worktree & Feature Isolation:** Never commit directly to parent production branches. Always perform modifications in clean, dedicated feature branches. If doing parallel research, utilize isolated `git worktree` structures to isolate active changes.
- **Interactive Goal Alignment (Brainstorming):** Do not immediately start editing files upon receiving a task. You must first perform a "Brainstorming and Context Exploration" step—asking clarifying questions, performing local searches, and reviewing `.agents/repo_context.md`.
- **Test-Driven Development (TDD) Loop:** Emphasize the "Red-Green-Refactor" cycle. If fixing a bug or adding a feature, write the regression test *first* to verify failure (Red), write the minimal code to satisfy the test (Green), and only then refactor for styling and linting requirements.
- **Fail-Safe Verification Gates:** You must produce objective log outputs or successful exit statuses before declaring any task complete. No task may be marked `[x]` in `tasks/todo.md` based purely on parametric assumptions.
