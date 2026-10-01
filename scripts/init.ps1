# Init: make the environment runnable. Nothing else.
# One command, idempotent, fast, and silent on success.
# NOTE: keep this file ASCII-only. Windows PowerShell 5.1 reads .ps1 as ANSI
# without a BOM and will fail to parse non-ASCII characters in strings.

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$env:PYTHONIOENCODING = "utf-8"

function Step($msg) { Write-Host "  $msg" }

Write-Host "shotcraft :: init"

# 1. upstream clone -- the source of truth for every index we build
if (-not (Test-Path "upstream/video-shotcraft/.git")) {
    Write-Host "  cloning upstream (44 MB, a few minutes on a slow link)..."
    git clone --depth 1 --single-branch --branch main `
        https://github.com/Vincentwei1021/video-shotcraft.git upstream/video-shotcraft
    if ($LASTEXITCODE -ne 0) { throw "upstream clone failed" }
} else {
    Step ("upstream present (" + (git -C upstream/video-shotcraft rev-parse --short HEAD) + ")")
}

# 2. the database -- a pure function of the pinned tree
python platform/ingest/run.py | Out-Null
if ($LASTEXITCODE -ne 0) { throw "ingest failed; see platform/ingest/run.py" }
$stats = python platform/query.py stats | ConvertFrom-Json
Step ("db: {0} cards / {1} styles / {2} motion params" -f $stats.cards, $stats.styles, $stats.motion_params)

# 3. the wiki -- generated from the database, never hand-edited
python platform/wiki/build_wiki.py | Out-Null
if ($LASTEXITCODE -ne 0) { throw "wiki build failed" }
Step ("wiki: " + (Get-ChildItem wiki/cards/*.md).Count + " card pages + llms-full.txt")

Write-Host "ok -- query with: python platform/query.py cards --energy high"