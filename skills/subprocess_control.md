# OS Introspection & Subprocess Control

Because our scripts manage system-level operations (like robocopy execution or system calls), handle subprocesses defensively:

- **Strict Environment Path Safety:** Always use `pathlib.Path` exclusively to manage folder and file operations. Never hardcode backslashes (`\`) or forward slashes (`/`) as strings; let `pathlib` handle platform-specific OS resolutions.
- **Checked Subprocesses:** When invoking OS utilities or shell commands, use `subprocess.run(..., check=True)` to guarantee that errors raise immediately instead of failing silently:
  ```python
  import subprocess
  # Enforce strict subprocess execution
  result = subprocess.run(
      ["robocopy", src, dest, "/E"],
      capture_output=True,
      text=True,
      check=False  # Robocopy uses custom non-zero return codes; handle manually
  )
  ```
- **Encoding Safety:** Always declare UTF-8 encoding when reading or writing system files to prevent Windows-default ANSI/cp1252 parsing errors:
  ```python
  content = path.read_text(encoding="utf-8")
  ```
