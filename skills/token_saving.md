# Token-Saving & Context Window Management

To prevent context window bloating, minimize API latency, and avoid LLM performance degradation, follow these strict token-saving tactics:

- **Targeted Line Reading:** When inspecting large files, specify exact start and end line ranges (e.g., lines 100 to 140) rather than reading whole files top-to-bottom.
- **Targeted Block-Replacements:** Do **not** rewrite or output unchanged blocks of code. Use narrow, targeted replacements or standard unified diff syntax to alter only the affected lines.
- **AST / Module Outlining:** Use lightweight CLI tools or simple grep commands to scan module structures and imports rather than opening every file in a package.
- **Scratch Space Offloading:** Dump temporary exploratory files, trace logs, or debugger outputs into the `scratch/` directory. Do not load them into active conversation context unless summarizing critical tracebacks.
