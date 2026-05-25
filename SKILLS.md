# Centralized AI Agent Skills Index

As an AI agent operating within MCRE-BE repositories, you are required to adhere to the modular engineering skills listed below. 

To conserve tokens and keep your context window highly focused, **do not read the entire skills directory**. Only view and load the specific, relevant markdown files required to fulfill your active task.

---

## 1. Core Tooling & Quality Gates
* **[Dependency Management (uv)](skills/dependency_management.md):** Declarative package installation and runtime execution via `uv`.
* **[Linting & Formatting (Ruff)](skills/linting_formatting.md):** Strict lint checkups, formatting, and import organization.
* **[Testing (Pytest)](skills/testing.md):** Executing unit tests and maintaining quality gates.
* **[Git & Local Verification](skills/git_verification.md):** Safe pre-commit diff checks and verification requirements.
* **[Pre-commit (prek)](skills/precommit.md):** Orchestrating local hook execution.
* **[Critic & Validator (openspec-critic.md)](skills/openspec-critic.md):** Strict verification loop ensuring state verification, Ruff formatting, type annotations, and Pytest proofs.

---

## 2. Advanced Diagnostic Skills
* **[Caveman Debugging & Diagnostics](skills/diagnostics_caveman.md):** Strategic print tracing, active state introspection, and sandbox environment analysis.
* **[Mocking & Test Isolation](skills/mocking_testing.md):** Safe external API mocking and call assertions.
* **[AST Repository Mapping (grep-ast)](skills/grep_ast.md):** Token-efficient codebase signature mapping and structural search navigation.

---

## 3. Process Layers & Engineering Discipline
* **[Planning & Spec Writing (Plan First)](skills/planning.md):** Designing implementation specifications and component maps before typing code.
* **[OpenSpec Workflow (openspec.md)](skills/openspec.md):** Structured proposal, design, and plan checklist artifact sequence before code execution.
* **[Agent Superpowers (obra/superpowers)](skills/superpowers.md):** Git branch isolation, brainstorming context exploration, and strict TDD cycles.
* **[Caveman Mode & Token Compression (JuliusBrussee/caveman)](skills/caveman.md):** 65-75% output token savings using high-compression telegraphic communication.

---

## 4. Production Coding Standards
* **[Production-Grade Logging & Exceptions](skills/logging_exceptions.md):** Standard logger setups, custom exception structures, and trace-chaining.
* **[Subprocess Control & OS Introspection](skills/subprocess_control.md):** Platform-agnostic pathing (`pathlib`), system command defensive checks, and UTF-8 encoding boundaries.
* **[Code Simplification & Refactoring (Simplifier)](skills/code_simplification.md):** Applying senior-level code simplification rules based on official Anthropics standards.
