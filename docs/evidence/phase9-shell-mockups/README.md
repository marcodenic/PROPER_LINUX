# Phase 9 shell mockups

Status: direction approved at the PM shell-surfaces review. These remain
visual-direction studies rather than implementation screenshots; the matching
installed-VM result is in `docs/evidence/phase9-shell-implementation`.

## Mockups

1. [Popup surface direction](01-popup-surface-direction.png) — calendar, status,
   notifications, networking, audio, power, and brightness using one calmer
   Vicinae-adjacent visual system.
2. [Central-bar variants](02-central-bar-variants.png) — five compact bottom-bar
   compositions labelled A through E.
3. [Integrated recommendation](03-integrated-recommendation.png) — the refined
   unified capsule and combined status popover in normal desktop context.

## Shared visual rules

- Neutral near-black surfaces at roughly 90–94% opacity
- Backdrop blur used for depth, not as the only source of contrast
- Thin neutral border and soft shadow instead of a blue title strip
- 14–16 px corner radii, 16 px panel padding, and an 8 px spacing rhythm
- One monochrome 20–22 px status-icon family with consistent optical bounds
- Desaturated blue reserved for selection, focus, slider fill, and progress
- Upstream Plasma behaviour retained beneath the visual layer

## Bar variants

- **A — Refined capsule:** one compact surface and the lowest implementation
  risk.
- **B — Three islands:** the clearest grouping, but it may require multiple
  panels or more custom composition than the visual gain warrants. Retain as a
  possible later experiment.
- **C — Quiet rail:** calm and dense, but less distinctly Proper and less
  forgiving for pointer targets.
- **D — Soft shelf:** the approved version 0.1 direction. It gives applications
  clearer emphasis while remaining one upstream, centred, fit-content panel.
- **E — Asymmetric compact:** a useful compromise if the clock should read as a
  separate object while the whole composition remains centred.

## Implementation hypothesis

The popup direction should first be tested as a narrow Proper Plasma Style plus
colour, icon, and supported widget configuration. The bar should remain the
upstream Plasma panel. A coherent icon theme and disciplined widget spacing are
likely to remove most of the current unevenness without replacing task, tray,
clock, networking, audio, power, or notification behaviour.

## Prompt set

The built-in image-generation workflow used the installed Proper desktop and
Phase 9 contact sheets as references. The three prompts requested: (1) a
shippable Vicinae-adjacent popup design system without blue header strips, (2)
five compact central-bar variants with unified monochrome icons, and (3) an
integrated desktop recommendation combining the refined capsule with a
practical status popover. All prompts required the original Proper identity,
compact pointer-friendly layouts, neutral charcoal surfaces, restrained blue
accents, and no macOS/Windows imitation.
