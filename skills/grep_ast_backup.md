# Backup Spec: AST Repository Mapping & Codebase Navigation

This is the offline fallback/backup specification for AST Repository Mapping and Codebase Navigation. Use this only when offline, network-quarantined, or explicitly instructed to conserve context tokens.

---

## 1. Core Concepts of AST Mapping

Rather than reading full source implementations, you only inspect the structural signatures of the codebase:
* **Classes:** Class names, parent inheritance classes, and class docstrings.
* **Methods & Functions:** Method names, parameters, strict type annotations, return types, and public method docstrings.
* **Imports:** Inter-module dependencies and external third-party library imports.

*Rationale:* This gives you 100% accurate context regarding *where* classes and methods are defined and *how* they interface with each other, without loading the actual helper logic or inner loops.

---

## 2. Dynamic AST Outlining & Command Suite

If the repository utilizes `aider` or has `grep-ast` configured, leverage the following skills:

### A. Generating a Local Codebase Skeleton
When starting a task or analyzing module boundaries, use Python's built-in `ast` module or command-line utilities to output a concise declaration map of a target module:

```bash
# Get a structural map of the python files (Signatures only, no code blocks)
uv run python -c "
import ast, sys, pathlib
path = pathlib.Path(sys.argv[1])
tree = ast.parse(path.read_text(encoding='utf-8'))
for node in ast.walk(tree):
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        args = [a.arg for a in node.args.args]
        print(f'  func: {node.name}({', '.join(args)}) -> line {node.lineno}')
    elif isinstance(node, ast.ClassDef):
        print(f'class: {node.name} -> line {node.lineno}')
" <target_file.py>
```

### B. AST-Aware Searching (`grep-ast`)
If `grep-ast` is installed globally or in the active virtual environment, use it to perform structural searches that locate precise function definitions rather than simple string occurrences:

```bash
# Search for functions or classes by name rather than matching random comments
grep-ast "class ArgosSync" .
```

---

## 3. Workflow Integration

Always employ the AST Repository Map during **Step 1 (Review Context)** and **Step 2 (Plan)** of your development loop:

1. **Orientation:** Before modifying a consumer package (e.g., `ntfy_lite`), run a quick AST outline over the main module files to identify helper methods and core classes.
2. **Import Integrity:** Verify signature parameters (such as positional vs keyword arguments) using the AST map before calling functions in other files to prevent compilation or runtime exceptions.
3. **Refactoring Reviews:** During simplification or refactoring steps, inspect the module's AST map to confirm that no public class or method signatures were accidentally altered or removed, keeping public API compatibility at 100%.
