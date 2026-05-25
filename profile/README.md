# 🧠 MCRE-BE Organizational Brain

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI Status](https://github.com/MCRE-BE/.github/actions/workflows/ci.yml/badge.svg)](https://github.com/MCRE-BE/.github/actions)

Welcome to the centralized brain and standard configuration repository for the **MCRE-BE** organization. This repository hosts global settings, AI instructions, CI/CD templates, and engineering standards enforced across all organization codebases.

---

## 🏛️ Architecture & Integration Flow

Our development environments utilize git submodules to bridge individual workspaces with this centralized brain, feeding uniform configurations directly to local AI agents and linters.

```mermaid
graph TD
    subgraph Central ["Centralized Brain (.github)"]
        A[AGENTS.md: Persona & Workflow]
        B[GEMINI.md: AI Orchestration]
        C[ruff.toml: Style Rules]
    end
    subgraph Repo ["Consumer Repository (e.g. pyRobocopy)"]
        D[.agents/global/ Submodule] -->|Symlink / Reference| E[.cursorrules / .windsurfrules]
        D -->|Extend| F[ruff.toml]
    end
    A -->|Mirrors| D
    C -->|Mirrors| D
```

---

## 📂 Repository Layout

- **`AGENTS.md`**: Persona, engineering discipline, and the core workflow state-machine for IDE agents.
- **`GEMINI.md`**: Specialized guidelines and orchestrations designed specifically for Gemini agent models.
- **`skills/`**: A library of modular, token-saving engineering skills loaded dynamically by agents as needed.
- **`scripts/verify.py`**: Programmatic verification pipeline run by agents locally before completing tasks.
- **`ruff.toml`**: Shared styling rules and import sorting conventions.

---

## 🚀 Workspace Setup

To bootstrap a new or existing repository under the MCRE-BE umbrella to consume this centralized brain, follow the step-by-step instructions in the:

👉 **[AI Agent Workspace Setup Guide (SETUP.md)](SETUP.md)**

---

## 📦 Active Consumer Repositories

This brain coordinates and enforces standards across the following repositories:
1. **`dll-danda-ibp-scripts`**: Monorepo orchestrating ETL, IBPM, and Argos synchronization.
2. **`pyRobocopy`**: Premium Windows-specific Robocopy wrapper.
3. **`ntfy_lite`**: Minimalist Python API and CLI for ntfy.sh notifications.
4. **`becse-adp-dllgsc`**: Databricks ADP data product utilizing dbt and SQL.
