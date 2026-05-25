# Caveman Mode & Token Compression (JuliusBrussee/caveman)

**Official Repository:** [github.com/JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)  
**Primary Installation & Spec Source:** [github.com/JuliusBrussee/caveman/blob/main/INSTALL.md](https://github.com/JuliusBrussee/caveman/blob/main/INSTALL.md)

---

## 🚀 Execution Priority & Version Integrity

1. **First Priority (Web Reference):** If online, you **must** try to read the latest operational rules and run installation commands directly from the official [JuliusBrussee/caveman GitHub Repository](https://github.com/JuliusBrussee/caveman).
2. **Second Priority (Local Fallback):** If offline, network-quarantined, or explicitly instructed to conserve active context tokens, load and execute the optimized local specification:
   * **[JuliusBrussee/caveman Local Backup Specification](caveman_backup.md)**

---

## 1. `/caveman-commit` (Commit Message Compression)

All commit messages must follow **Conventional Commit** conventions (`feat:`, `fix:`, `docs:`, etc.) coupled with **Caveman Lite** speech in the description.

* **Formatting Rule:** `<type>[optional scope]: <caveman-lite-description>`
* **Constraints:**
  * Keep the subject line $\le 50$ characters.
  * Focus on *why* over *what*.
  * Strip articles (`a`, `an`, `the`) and filler words (`just`, `simply`, `actually`, `basically`).
* **Examples:**
  * ❌ `feat(auth): add a new timeout guard to prevent hanging the server`
  *   `feat(auth): add timeout guard prevent server hang`
  * ❌ `fix(db): resolve the race condition in checkout because connection pool was exhausted`
  *   `fix(db): fix checkout race pool exhaust`

---

## 2. Thought Compression (Internal Reasoning)

To drastically cut output tokens, compress internal thought processes in `<thought>` tags using **Full Caveman** speech.

* **Formatting Rule:** Drop articles, pronouns, pleasantries, filler words. Use telegraphic, keyword-only style.
* **Examples:**
  * ❌ `<thought>I need to read the config file first to see if there is any existing setup. Then I will edit it to include the new parameter.</thought>`
  *   `<thought>Read config file. Inspect setup. Edit add new parameter.</thought>`
  * ❌ `<thought>The test failed because the expected value was 200 but got 404. I will check the API route definition to see why it is returning 404.</thought>`
  *   `<thought>Test fail. Expect 200, got 404. Check API route definition.</thought>`

---

## 3. `/caveman-compress` (Memory & Lessons Compression)

All memory, lessons, and learnings files (like `tasks/lessons.md` or `learnings.md`) must be created/updated with key changes written in **Full/Lite Caveman** speech.

* **Formatting Rule:** Keep entries telegraphic. Preserve technical terms, paths, filenames, and code verbatim. Cut all auxiliary framing.
* **Examples:**
  * ❌ `* We found that when the trailing comma is missing on multi-line calls, ruff check fails. We should make sure we always add trailing commas to multi-line lists.`
  *   `* Missing trailing comma on multi-line calls fail Ruff. Always add trailing comma.`
  * ❌ `* It is really important to use pathlib.Path because standard strings can cause cross-platform slash issues on Windows.`
  *   `* Avoid slash issue on Windows. Use pathlib.Path exclusively.`
