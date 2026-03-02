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
- This protection is mandatory because buyer distribution must preserve both the `1인1PC` restriction and license period enforcement.
- If a task request conflicts with this policy, explicitly refuse that part and proceed only with allowed changes.

## Machine ID Standard (Apply to all future `.py`)
- Goal: enforce `1인1PC` and `사용 기간` while preventing machine-id file artifacts in distributed builds.
- Machine ID format must be fixed as: `NAVER-` + 32 lowercase hex characters.
- Machine ID source priority must be:
  1. valid `registered_machine_id` in license data (if already issued),
  2. saved registry value (`HKCU\\Software\\Auto_Naver\\MachineId`) on Windows,
  3. deterministic hardware fingerprint hash (MachineGuid / SMBIOS UUID / system drive serial / stable MAC).
- Machine ID must never be persisted to text files. Registry persistence is allowed; `machine_id.txt` is always forbidden.
- On every app start (including `.exe` run), silently scan and delete machine-id text artifacts (`machine_id.txt`, `machine-id.txt`, `machineid.txt`, and machine+id named `.txt`) under:
  - exe base folder and all subfolders,
  - project `setting` tree,
  - runtime state dir and its subfolders,
  - Windows `APPDATA/LOCALAPPDATA/PROGRAMDATA` `Auto_Naver` trees.
- Cleanup must be silent: no popup, no console log, no user-facing message.
- License storage must keep period-check fields and buyer mapping data; do not remove license validity/expiry checks for convenience.
- If refactoring license code, preserve behavioral compatibility first:
  - existing valid buyers continue to pass,
  - expired buyers continue to fail,
  - unregistered machines continue to fail.
- Before release, run a recursive check from exe folder and confirm no machine-id artifact file is included in source, dist, or package output.
