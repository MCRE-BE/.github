# Specification Writing & Planning Mode (Plan First)

Before writing any non-trivial code (3+ changes, architectural additions, or complex bugs), you must follow the **OpenSpec Workflow (OPSX)** detailed in [OpenSpec Workflow (openspec.md)](openspec.md). Never jump straight to writing code.

---

## 🚀 The Planning & Artifact Sequence

1. **Proposal (`openspec/changes/<name>/proposal.md`):**
   * Define intent, business/technical drivers, "Why", and "What".
2. **Design (`openspec/changes/<name>/design.md`):**
   * Define technical approach, file dependencies, interfaces, APIs, and specific Python 3.13 features.
3. **Tasks Checklist (`tasks/todo.md`):**
   * Define a strict, sequential list of testable, checkable items to execute.

---

## 🛑 User Alignment Rule

Once the `tasks/todo.md` tasks list is created:
* **PAUSE immediately.**
* **Present the checklist to the user and request verification/approval.**
* Do not modify source files or execute implementation commands until approval is received.
* Work through the checklist sequentially, verifying each step with the **Critic & Validator** ([openspec-critic.md](openspec-critic.md)) before checking off items `[x]`.
