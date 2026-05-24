# Welcome

This is the centralized brain and default configuration for my organization. It's a trial reposority for the AI stuff I coded.

## What lives here?

- **AI Agent Configurations**: Global prompts (agents.md) and standard commands (skills.md) that dictate how our AI tooling interacts with our repositories.

- **Reusable Workflows**: Standardized CI/CD pipelines (like reusable-uv-ci.yml) used across all projects.

- **Community Health Files**: Organization-wide PR and Issue templates.

Our repositories rely on a "Simplicity First" architecture, heavily utilizing uv for lightning-fast Python tooling.

## Setup design

- **Local Bridge**: Individual repositories (like ntfy_lite) will pull this in via Git Submodule (e.g., git submodule add https://github.com/MCRE-BE/.github .agents/global).
- **Standardization**: Each repo maintains its own local .github/ profile directory to override or extend global defaults locally. This ensures changes take effect immediately for any agent instance without needing to update the remote submodule first.
