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
$stats = python platform/query.py stats
$cards = [regex]::Match($stats, '"cards":\s*(\d+)').Groups[1].Value
$styles = [regex]::Match($stats, '"styles":\s*(\d+)').Groups[1].Value
$params = [regex]::Match($stats, '"motion_params":\s*(\d+)').Groups[1].Value
$techs = [regex]::Match($stats, 'techniques\s*:\s*(\d+)').Groups[1].Value
Step ("db: {0} cards / {1} styles / {2} motion params / {3} techniques" -f $cards, $styles, $params, $techs)

# 3. the wiki -- generated from the database, never hand-edited
python platform/wiki/build_wiki.py | Out-Null
if ($LASTEXITCODE -ne 0) { throw "wiki build failed" }
Step ("wiki: " + (Get-ChildItem wiki/cards/*.md).Count + " card pages + llms-full.txt")

# 3b. recipe briefs -- also generated from the database. This was missing from
# the chain and deleting prompts/generated/ silently lost it: nothing rebuilt the
# tree and nothing said so.
python platform/prompts/build_prompts.py | Out-Null
if ($LASTEXITCODE -ne 0) { throw "prompt briefs failed; see platform/prompts/build_prompts.py" }
Step ("prompts: " + (Get-ChildItem prompts/generated/*.json -ErrorAction SilentlyContinue).Count + " briefs")

# 4. the localized site -- extraction is the source of truth, then the build.
#    Skipped when the upstream gallery is absent, so this stays a *fast* command.
if (Test-Path "upstream/video-shotcraft/gallery/library.html") {
    python platform/site/extract_locales.py | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "locale extraction failed" }
    python platform/site/build_site.py | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "site build failed" }
    python platform/site/prerender.py | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "site prerender failed" }
    $locales = (Get-ChildItem site/dist -Directory | Where-Object { Test-Path (Join-Path $_.FullName "library.html") }).Count
    Step ("site: " + $locales + " locales built to site/dist/")
} else {
    Step "site: skipped (no upstream gallery)"
}

# 5. the catalog corpus (ADR 0007). Absent is a WARN, not a failure: either
#    corpus must build alone.
if (Test-Path "data/cinematic") {
    python platform/catalog/selftest.py | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "catalog selftest failed; see platform/catalog/selftest.py" }
    Step "catalog: invariants hold"
}

Write-Host "ok -- query with: python platform/query.py cards --energy high"