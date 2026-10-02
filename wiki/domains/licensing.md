# Licensing

The stack is not uniformly free. Before anything is sold or published, this is the table that decides it.

| subject | licence | commercial use | blocks us | obligation |
|---|---|---|---|---|
| Tracked-out audio (5 files 无法反查; upstream prose says 6) | unknown | `unknown` | **yes** | must be re-licensed or replaced before any commercial delivery; `audio_asset.commercial_ok = 0` until then |
| video-talkcraft (sibling skill) | PolyForm Noncommercial 1.0.0 | `requires-license` | **yes** | commercial use of the tool requires written authorisation |
| Mixkit SFX + BGM | Mixkit Free License | `free` | no | free for commercial use, no attribution required |
| Remotion (render engine) | Remotion License | `free-for-individuals` | no | free for individuals and companies of up to three people; a company above that needs a paid licence, which is a pricing question at delivery time, not a legal one. platform/render/run.py records the tier it ran under. |
| Shot-recipe provenance (48 cards, 2026-08) | Apache-2.0, techniques re-implemented | `free` | no | no third-party footage or brand assets included; do not claim endorsement |
| video-shotcraft core | Apache-2.0 | `free` | no | keep copyright + NOTICE when redistributing |

## Audio audit

149 SFX across 16 scene categories and 5 BGM tracks, all Mixkit free licence. `assets/audio/ATTRIBUTION.md` records the source of every file at download time (the rule there is: record it when you fetch it, you cannot reverse-look-it-up later).

**5 files are marked untraceable (无法反查) and must not ship in a commercial delivery until re-sourced:**

- `assets/audio/sfx/light/sparkle.mp3`
- `assets/audio/sfx/riser/riser-cine.mp3`
- `assets/audio/sfx/text/keyboard.mp3`
- `assets/audio/sfx/transition/whoosh-big.mp3`
- `assets/audio/sfx/ui/pop.mp3`

## What this means for us

- The **core is Apache-2.0**: fork, modify, sell services built on it. Keep the copyright and add a NOTICE when redistributing.
- **Remotion's paid tier applies to companies above three people, not to individuals.** This repo is rendered by an individual, so the free tier applies and `platform/render/run.py` runs; see `render/out/` and `platform/render/render_report.json`. A client deliverable rendered *for a company* has to price the licence in, or the client buys it — which is a pricing question, not a legal one.
- **The distinction is which kind of fact it is.** A licence term binds whoever ships the code. A free tier is a fact about who is running it. Collapsing the two is how a project refuses to build something it is allowed to build — or, worse, ships something it is not.
- **video-talkcraft is PolyForm Noncommercial.** We can read it for ideas and port techniques (upstream already did: 19 cards were ported across), but we cannot ship it or build a product on it commercially without authorisation. This one *is* a hard constraint.
- **Tracked-out audio** is the quietest risk: 5 files with no traceable source (`commercial_ok = 0`). Replace them before a client-facing delivery rather than arguing about it later.
