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
- If a task request conflicts with this policy, explicitly refuse that part and proceed only with allowed changes.
