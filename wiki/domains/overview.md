# video-shotcraft — overview

An open-source agent skill (Apache-2.0) that turns Claude Code or Codex into a motion-design studio: 157 shot recipe cards, 218 tuned Remotion demos, 149 sound effects and a validated 36.2-second promo template.

- **upstream**: https://github.com/Vincentwei1021/video-shotcraft — 10,100 stars, 899 forks, `5ddbf521038b`
- **site**: https://vincentwei1021.github.io/video-shotcraft

| | |
|---|---|
| shot cards | 157 |
| motion styles (demos) | 218 |
| documented parameters | 1057 |
| pitfalls | 792 (3 marked 命门) |
| motion params extracted by us | 1897 |
| aesthetic rules | 27 |
| SFX / BGM | 149 / 5 |
| upstream locales | 2 (en, zh) |
| our target locales | 9 |
| translation strings | 1298 |

## Read in this order

- [What video-shotcraft is, what it ships, and the four layers](domains/overview.md)
- [The 157 shot recipe cards, indexed by category, energy and duration](domains/cards.md)
- [Easing curves, spring configs and timing primitives extracted from the demos](domains/motion-grammar.md)
- [The production pipeline, the 27 aesthetic rules, the energy arc, sound and QA](domains/methodology.md)
- [How the upstream repo, the gallery site and the workbench fit together](domains/architecture.md)
- [Every licence in the stack and what it allows or blocks](domains/licensing.md)
- [The sibling skill, the tools, the channels, and the upstream author](domains/landscape.md)
- [Revenue models, ranked by time to first dollar, with the evidence](domains/monetization.md)
- [Motion-design vocabulary as used by these cards, with card references](domains/glossary.md)
- [The cinematic-technique catalog: what to shoot, and how to say it per tool](domains/cinematic.md)

## Hard rules that survive everything

1. **Real screenshots for real products.** Reproducing an existing page means capturing it with a headless browser at 2x, with element cutouts and a layout.json. Hand-drawn UI is only allowed outside reproduction contexts.
2. **The visual language grows from the product**, not from a borrowed promo skin. The cards supply motion grammar and timing; type, colour and material are re-derived from the target.
3. **One shot, one motion idea.** Repeat a technique across a film and it stops being a technique and starts being noise.
4. **Hold after every key beat.** Wordmark settle ≥1s, batch tail 0.5s still, opening hero ≥3s. Feedback history only ever asked for slower.
5. **With strong BGM, every cut lands on a beat.** Measure real BPM and phase first, then verify cut error ≤3 frames against the rendered audio.
6. **Determinism.** Seeded pseudo-randomness only; renders must be frame-reproducible.
7. **Independent final review.** The maker never does the first QA pass.
