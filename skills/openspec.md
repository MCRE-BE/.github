# OpenSpec Workflow (OPSX)

Description: Use this skill to structure any non-trivial change into trackable artifacts (proposal, design, tasks) before writing code.
Trigger: A new feature request, an architectural change, or a bug requiring >3 steps.

## Execution Rules

Never jump straight to code. Follow this exact artifact sequence:

- **Proposal** (openspec/changes/<name>/proposal.md): Define the "Why" and "What" (intent, scope).
- **Design** (openspec/changes/<name>/design.md): Define the technical approach, file structure, and specific Python 3.13 features to be used.
- **Tasks** (tasks/todo.md): Translate the design into a strict checklist.

## Implementation Standard

- Once tasks/todo.md is generated, PAUSE. Request user verification before proceeding.
- Work through tasks/todo.md sequentially.
- Mark items [x] as you complete them.

## Archiving

Once all tasks are marked complete and validated via the critic-approver skill, summarize the lessons learned in tasks/lessons.md and archive the OpenSpec change.