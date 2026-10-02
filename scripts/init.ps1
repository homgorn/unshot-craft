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
    # seo runs LAST on purpose. build_site regenerates the pages, prerender bakes
    # translated card text into the body, and seo rewrites the head, creates the
    # 471 per-card pages and regenerates the sitemap to match. Any earlier and the
    # head is rebuilt underneath it; any later and the card pages and the sitemap
    # describe a tree that no longer exists.
    python platform/site/seo.py --build | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "seo build failed; see platform/site/seo.py" }
    python platform/site/icons.py | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "icon generation failed" }
    $locales = (Get-ChildItem site/dist -Directory | Where-Object { Test-Path (Join-Path $_.FullName "library.html") }).Count
    $cards = (Get-ChildItem site/dist/*/card/*.html -ErrorAction SilentlyContinue).Count
    Step ("site: " + $locales + " locales, " + $cards + " card pages")
} else {
    Step "site: skipped (no upstream gallery)"
}

# 5. the catalog corpus (ADR 0007). Absent is a WARN, not a failure: either
#    corpus must build alone.
if (Test-Path "data/cinematic") {
    python platform/catalog/build_briefs.py | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "catalog briefs failed; see platform/catalog/build_briefs.py" }
    python platform/catalog/selftest.py | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "catalog selftest failed; see platform/catalog/selftest.py" }
    Step "catalog: invariants hold"
}

# 6. the gates. Every one of these has caught a real defect; running the pipeline
#    without them is how a broken build gets committed.
$gate = @(
    @{ name = "doctor";       cmd = "platform/doctor.py" },
    @{ name = "doc numbers";  cmd = "platform/docs_freshness.py" },
    @{ name = "wiki audit";   cmd = "platform/wiki/audit_quality.py" },
    @{ name = "card briefs";  cmd = "platform/prompts/build_prompts.py --lint" },
    @{ name = "cat briefs";   cmd = "platform/catalog/build_briefs.py --lint" },
    @{ name = "coverage";     cmd = "platform/site/check_coverage.py" },
    @{ name = "seo";          cmd = "platform/site/check_seo.py" }
)
foreach ($g in $gate) {
    # Splat the argv array. Indexing a split with `[1..(len-1)]` on a one-element
    # command hands python an empty argument list, which it reads as "usage".
    $argv = @($g.cmd -split " ")
    $out = & python @argv 2>&1
    if ($LASTEXITCODE -ne 0) {
        $out | Select-Object -Last 6 | ForEach-Object { Write-Host "    $_" }
        throw ("gate failed: " + $g.name)
    }
    Step ("gate ok: " + $g.name)
}

# 7. the gates that need a browser or a port. Kept out of the loop above because
#    they take minutes, not seconds, and a slow gate trains people to skip the
#    fast ones. Run them before a commit, not on every rebuild.
$deep = @(
    "platform/catalog/selftest.py",
    "platform/catalog/layer_gate.py",
    "platform/api/selftest.py",
    "platform/site/selftest.py"
)
Write-Host "  slow gates, not run here:"
foreach ($s in $deep) { Write-Host "     python $s" }

Write-Host "ok -- query with: python platform/query.py cards --energy high"
Write-Host "     gates: platform/doctor.py, platform/docs_freshness.py, platform/catalog/layer_gate.py, platform/api/selftest.py, platform/site/selftest.py"