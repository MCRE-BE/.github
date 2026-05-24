# Caveman Debugging & Exploratory Diagnostics

When encountering opaque test failures, complex environment issues, or difficult-to-trace state issues, you are expected to employ **Caveman Debugging** and active exploration techniques:

- **Strategic Print Placement:** Use Python's f-string debugging syntax (`print(f"{variable=}")`) at key execution junctions to trace live runtime state.
- **Exploratory Scratchpads:** Create temporary scratch scripts (e.g. `scratch/debug_test.py`) to import a specific module, instantiate a class, or run a single function in isolation.
- **Runtime Introspection:** Print `type(obj)`, `dir(obj)`, or `obj.__dict__` to inspect properties when third-party libraries have undocumented behavior or type changes.
- **Environment Inspection:** Run `uv run python -c "import sys; print(sys.path)"` or `uv run python -c "import pkg; print(pkg.__file__)"` to resolve path clashes or check which version of a package is active.
