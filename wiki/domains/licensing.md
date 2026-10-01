# Licensing

The stack is not uniformly free. Before anything is sold or published, this is the table that decides it.

| subject | licence | commercial use | blocks us | obligation |
|---|---|---|---|---|
| Remotion (render engine) | Remotion License | `restricted` | **yes** | free for individuals and small companies; companies may need a paid licence |
| Tracked-out audio (6 files 无法反查) | unknown | `unknown` | **yes** | must be re-licensed or replaced before any commercial delivery |
| video-talkcraft (sibling skill) | PolyForm Noncommercial 1.0.0 | `requires-license` | **yes** | commercial use of the tool requires written authorisation |
| Mixkit SFX + BGM | Mixkit Free License | `free` | no | free for commercial use, no attribution required |
| Shot-recipe provenance (48 cards, 2026-08) | Apache-2.0, techniques re-implemented | `free` | no | no third-party footage or brand assets included; do not claim endorsement |
| video-shotcraft core | Apache-2.0 | `free` | no | keep copyright + NOTICE when redistributing |

## Audio audit

149 SFX across 16 scene categories and 5 BGM tracks, all Mixkit free licence. `assets/audio/ATTRIBUTION.md` records the source of every file at download time (the rule there is: record it when you fetch it, you cannot reverse-look-it-up later).

## What this means for us

- The **core is Apache-2.0**: fork, modify, sell services built on it. Keep the copyright and add a NOTICE when redistributing.
- **Remotion is the real commercial gate.** Free for individuals and small companies; companies may need a paid licence. Any client deliverable has to price this in, or the client buys the licence.
- **video-talkcraft is PolyForm Noncommercial.** We can read it for ideas and port techniques (upstream already did: 19 cards were ported across), but we cannot ship it or build a product on it commercially without authorisation.
- **Tracked-out audio** is the quietest risk: 6 files with no traceable source. Replace them before a client-facing delivery rather than arguing about it later.
