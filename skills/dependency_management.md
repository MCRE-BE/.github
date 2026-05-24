# Dependency Management (uv)

Always use `uv` for dependency management and execution. Do not use standard pip, pipenv, or poetry unless explicitly instructed.

- **Install dependencies:** `uv sync`
- **Add a package:** `uv add <package_name>`
- **Add a dev package:** `uv add --dev <package_name>`
- **Run a script or tool:** `uv run <command>`
