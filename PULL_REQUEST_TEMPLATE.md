## PR Type
What kind of change does this PR introduce? (Select at least one)
- [ ] `feat`: A new feature
- [ ] `fix`: A bug fix
- [ ] `docs`: Documentation only changes
- [ ] `style`: Changes that do not affect the meaning of the code (formatting, linting)
- [ ] `refactor`: A code change that neither fixes a bug nor adds a feature
- [ ] `perf`: A code change that improves performance
- [ ] `test`: Adding missing tests or correcting existing tests
- [ ] `chore`: Changes to the build process or auxiliary tools

## Description
Please include a brief summary of the change, target problem, and motivation.

## Proposed Changes
List the key changes introduced in this PR:
1. 
2. 

## AI Agent / Developer Verification Checklists

### 1. Verification Script
- [ ] I have run the programmatic verification script and all checks pass successfully:
  ```bash
  uv run python .agents/global/scripts/verify.py
  ```

### 2. Code Quality & Standards
- [ ] **Formatting:** Trailing commas are used on all multi-line lists/parameters.
- [ ] **Linting & Types:** `uv run ruff check .` and `uv run ty check .` run without errors.
- [ ] **Documentation:** NumPy docstring style is used for all public classes and functions.
- [ ] **Explicit Arguments:** Named arguments are preferred over positional arguments for clarity and safety.
- [ ] **Paths:** `pathlib.Path` is used exclusively (no string path operations).

### 3. Testing & Coverage
- [ ] I have added/updated unit tests covering all new logic paths.
- [ ] Combined code coverage reaches **100%** in the local test suite.

### 4. Git Workflow
- [ ] The commit message follows **Conventional Commits** format (`type(scope): description`).
- [ ] Changes are confined to a single logical improvement (no unrelated side effects).
