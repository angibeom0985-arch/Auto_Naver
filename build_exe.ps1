$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$spec = Join-Path $root "Auto_Naver_Blog_V5.1.spec"
$dist = Join-Path $root "dist"
$work = Join-Path $root "build"

# Ensure clean build so latest .py changes are reflected in the exe
if (Test-Path $work) {
    Remove-Item $work -Recurse -Force
}
if (Test-Path $dist) {
    Remove-Item $dist -Recurse -Force
}
Get-ChildItem -Path $root -Filter "__pycache__" -Directory -Recurse -ErrorAction SilentlyContinue |
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

python -m PyInstaller $spec --distpath $dist --workpath $work --clean --noconfirm

# Build success: auto-commit and push local changes
$changes = git status --porcelain
if ($changes) {
    git add -A
    $msg = "chore: auto-commit after build $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    git commit -m $msg
    git push origin HEAD
}
