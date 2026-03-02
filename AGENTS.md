# Codex Working Rules

## Git Auto-Commit
- At the end of every completed coding task, run `git add -A`, create a commit, and push to `origin`.
- Do not skip commit/push unless the user explicitly says not to push.
- Use clear commit messages that summarize the implemented fix.

## Machine ID Protection
- The existing machine ID behavior in any executable (`.exe`) must remain unchanged, even when rebuilding the executable or updating Python (`.py`) features.
- Do not modify, refactor, replace, or regenerate any machine ID logic in any file.
- Never create new machine ID-related code, functions, variables, classes, modules, scripts, resources, or configuration.
- Never create machine ID-related files in any location, including root, subfolders, build outputs, temp folders, or packaged artifacts.
- Do not add or generate any machine ID-related code/files in Python (`.py`), executable (`.exe`), or any folder under this project.
- Never create `machine_id.txt`; if it exists in any folder, delete it before continuing work or distribution.
- Before shipping to buyers, verify no `machine_id.txt` is included in source, build output, or packaged deliverables.
- If a task request conflicts with this policy, explicitly refuse that part and proceed only with allowed changes.
