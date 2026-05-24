# Specification Writing & Planning Mode (Plan First)

Before writing any non-trivial code (3+ changes or architectural additions), you must draft an **Implementation Plan** or **Technical Specification** at `tasks/todo.md` or a dedicated `design_spec.md` to align on requirements.

- **Component Architecture Mapping:** Map out the exact files to be created (`[NEW]`), modified (`[MODIFY]`), or deleted (`[DELETE]`) and order them logically (dependencies first).
- **Interface & API Definitions:** Define expected class signatures, public function signatures, parameter names, and strict type annotations *before* writing the implementation.
- **Requirement Verification Matrix:** Map each requirement to a specific verification command or unit test to guarantee complete test coverage of all edge cases.
