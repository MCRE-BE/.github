# OpenSpec Workflow (OPSX) & Planning Mode

**Description:** Use this skill to structure any non-trivial change (3+ changes, architectural additions, or complex bugs) into trackable artifacts (proposal, design, tasks) before writing code.
**Trigger:** A new feature request, an architectural change, or a bug requiring >3 steps.

---

## 🚀 The Planning & Artifact Sequence

Never jump straight to writing code. Follow this exact sequence of artifact generation:

1. **Proposal (`openspec/changes/<name>/proposal.md`):**
   - Define intent, business/technical drivers, "Why", and "What" (intent, scope).
2. **Design (`openspec/changes/<name>/design.md`):**
   - Define the technical approach, file dependencies, interfaces, APIs, and specific Python 3.10+ features to be used.
3. **Tasks Checklist (`tasks/todo.md`):**
   - Translate the design into a strict, sequential list of testable, checkable items to execute.

---

## 🛑 User Alignment & Implementation Standard

Once the `tasks/todo.md` tasks list is created:
- **PAUSE immediately.**
- **Present the checklist to the user and request verification/approval.**
- Do not modify source files or execute implementation commands until approval is received.
- Work through the checklist sequentially, verifying each step with the **Critic & Validator** ([openspec-critic.md](openspec-critic.md)) before checking off items `[x]`.

---

## 📦 Archiving

Once all tasks are marked complete and validated via the critic-approver skill, summarize the lessons learned in `tasks/lessons.md` (using full/lite Caveman token-saving compression) and archive the OpenSpec change.