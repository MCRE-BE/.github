# Centralized AI Agent Skills Index

As an AI agent operating within MCRE-BE repositories, you are required to adhere to the modular engineering skills listed below. 

To conserve tokens and keep your context window highly focused, **do not read the entire skills directory**. Only view and load the specific, relevant markdown files required to fulfill your active task.

> [!NOTE]
> **Path Context Notice:**
> The skills linked below are located in the global brain repository's `skills/` directory. When this repo is consumed as a submodule (e.g. at `.agents/global/`), the paths resolve relative to your active workspace (e.g. `.agents/global/skills/foo.md`).

---

## 1. Core Tooling & Quality Gates
* **[Tooling & Quality Gates Cheatsheet](skills/tooling_cheatsheet.md):** Declarative package installation and runtime execution via `uv`, strict lint checkups/formatting via `ruff`, testing via `pytest`, pre-commit hook runs via `prek`, and external API mocking.
* **[Critic & Validator (openspec-critic.md)](skills/openspec-critic.md):** Strict verification loop ensuring state verification, Ruff formatting, type annotations, and Pytest proofs.

---

## 2. Advanced Diagnostic Skills
* **[Caveman Debugging & Diagnostics](skills/diagnostics_caveman.md):** Strategic print tracing, active state introspection, and sandbox environment analysis.
* **[AST Repository Mapping (grep-ast)](skills/grep_ast.md):** Token-efficient codebase signature mapping and structural search navigation.
  * *Fallback:* **[grep-ast Local Backup](skills/grep_ast_backup.md)** if offline/conserving tokens.

---

## 3. Process Layers & Engineering Discipline
* **[OpenSpec Workflow & Planning (openspec.md)](skills/openspec.md):** Structured proposal, design, and plan checklist artifact sequence before code execution.
  * *Legacy link:* **[Planning Mode (planning.md)](skills/planning.md)** redirect spec.
* **[Agent Superpowers (obra/superpowers)](skills/superpowers.md):** Git branch isolation, brainstorming context exploration, and strict TDD cycles.
* **[Caveman Mode & Token Compression (JuliusBrussee/caveman)](skills/caveman.md):** 65-75% output token savings using high-compression telegraphic communication.
  * *Fallback:* **[Caveman Mode Local Backup](skills/caveman_backup.md)**.
* **[Token-Saving & Context Window Management](skills/token_saving.md):** Guidelines for line-specific viewing, targeted edits, and workspace organization to optimize model performance.

---

## 4. Production Coding Standards
* **[Production-Grade Logging & Exceptions](skills/logging_exceptions.md):** Standard logger setups, custom exception structures, and trace-chaining.
* **[Subprocess Control & OS Introspection](skills/subprocess_control.md):** Platform-agnostic pathing (`pathlib`), system command defensive checks, and UTF-8 encoding boundaries.
* **[Code Simplification & Refactoring (Simplifier)](skills/code_simplification.md):** Applying senior-level code simplification rules based on official Anthropic standards.
