# Production-Grade Logging & Exception Handling

We strictly adhere to robust, high-availability error management:

- **Declarative Logging:** Do not use `print()` statements in production code. Always use Python's built-in `logging` module with standardized configuration:
  ```python
  import logging
  logger = logging.getLogger(__name__)
  logger.info("Structured event log.")
  ```
- **Explicit Exception Raising:** Never raise vanilla exception classes (e.g., `raise Exception(...)` or empty `raise`). Always declare a descriptive custom exception or use precise subclassed exception types (e.g., `ValueError`, `RuntimeError`, `KeyError`):
  ```python
  class ArgosSynchronizationError(Exception):
      """Raised when Argos sync fails."""
  ```
- **Context-Preserving Exception Chaining:** When catching and re-raising exceptions, use `raise ... from` to preserve the original traceback context:
  ```python
  try:
      execute_sync()
  except NetworkError as err:
      raise ArgosSynchronizationError("Sync failed due to network issue.") from err
  ```
