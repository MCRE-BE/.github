# Backup Spec: Caveman Mode & Token Compression

This is the offline fallback/backup specification for Caveman Mode. Use this only when offline, network-quarantined, or explicitly instructed to conserve context tokens.

---

## 1. Core Rules of Caveman Style

* **Drop the Fluff:**
  * **Omit Articles:** Remove all instances of `a`, `an`, and `the` unless they are part of a code snippet or literal string.
  * **No Filler Words:** Eliminate auxiliary modifiers like `just`, `simply`, `actually`, `basically`, `really`, and `easily`.
  * **Skip Pleasantries:** Do not say `sure`, `certainly`, `of course`, `happy to help`, or `apologies`.
  * **Avoid Hedging:** Do not use phrases like `it might be worth considering`, `perhaps we could`, or `I think`. Be direct.
* **Preserve the Technical Details:**
  * **Verbatim Code & Diffs:** Never alter, shorten, or simplify code blocks, diffs, or syntax blocks.
  * **Verbatim Errors:** Quote console outputs and error tracebacks exactly.
  * **Technical Names:** Keep filenames, method names, imports, variables, and library names pristine.

---

## 2. Structured Output Format

When communicating in Caveman Mode, structure your output according to this primitive pattern:

```text
[thing] [action] [reason]. [next step]
```

*Example:*  
* Instead of: *"I ran pytest and unfortunately the checkout test failed because the import wasn't found. We should check the path."*
* Say: *"Pytest failed. Import missing. Run path check."*

---

## 3. Compression Intensity Levels

Depending on the token constraints, you can toggle between three compression tiers:

| Tier | Name | Description | Output Example |
| :--- | :--- | :--- | :--- |
| **1** | **Lite** | Strips only filler words, pleasantries, and hedging. Keeps normal sentence structure. | *I ran tests. One test failed due to an import error. I will verify the paths.* |
| **2** | **Full** | Enforces telegraphic style. Drops articles and pronouns. (Default Caveman). | *Test failed. Import missing. Verify path.* |
| **3** | **Ultra** | Keyword-only telegraph style. Extreme compression. | *Pytest fail. Import err. Check paths.* |

---

## 4. `/caveman-commit` (Commit Message Compression)

All commit messages must follow **Conventional Commit** conventions coupled with **Caveman Lite** speech in the description.

* **Formatting Rule:** `<type>[optional scope]: <caveman-lite-description>`
* **Constraints:** Keep subject line $\le 50$ chars. Focus on *why* over *what*. Strip articles and filler words.
* **Examples:**
  * `feat(auth): add timeout guard prevent server hang`
  * `fix(db): fix checkout race pool exhaust`

---

## 5. Thought Compression (Internal Reasoning)

To drastically cut output tokens, compress internal thought processes in `<thought>` tags using **Full Caveman** speech.

* **Formatting Rule:** Drop articles, pronouns, pleasantries, filler words. Use telegraphic, keyword-only style.
* **Examples:**
  * `<thought>Read config file. Inspect setup. Edit add new parameter.</thought>`
  * `<thought>Test fail. Expect 200, got 404. Check API route definition.</thought>`

---

## 6. `/caveman-compress` (Memory & Lessons Compression)

All memory, lessons, and learnings files (like `tasks/lessons.md` or `learnings.md`) must be created/updated with key changes written in **Full/Lite Caveman** speech.

* **Formatting Rule:** Keep entries telegraphic. Preserve technical terms, paths, filenames, and code verbatim. Cut all auxiliary framing.
* **Examples:**
  * `* Missing trailing comma on multi-line calls fail Ruff. Always add trailing comma.`
  * `* Avoid slash issue on Windows. Use pathlib.Path exclusively.`

---

## 7. Session Commands

* **Activate Caveman:** `talk like caveman` or `/caveman`
* **Deactivate Caveman:** `stop caveman` or `normal mode`
