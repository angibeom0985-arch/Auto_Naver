$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$spec = Join-Path $root "Auto_Naver_Blog_V5.1.spec"
$dist = Join-Path $root "dist"
$work = Join-Path $root "build"

pyinstaller $spec --distpath $dist --workpath $work

# 빌드 성공 시 변경사항 자동 커밋/푸시
$changes = git status --porcelain
if ($changes) {
    git add -A
    $msg = "chore: auto-commit after build $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    git commit -m $msg
    git push origin HEAD
}
