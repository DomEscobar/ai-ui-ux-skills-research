---
name: product-ux-bundle
description: Use when designing or reviewing app flows. Verify behavior.
version: 0.1.0
author: DomEscobar
license: UNLICENSED
platforms: [linux, macos, windows]
---

# Product UX Bundle

Use for product interactions, information hierarchy, or app-view design and review. Do not activate for unrelated backend work. For a narrow visual change, inspect the affected surface and preserve the interaction contract; skip full discovery unless behavior changes.

## Route by deliverable

- **Decide:** load [flow](references/flow.md). Produce a short view contract, not implementation, when asked to plan only.
- **Build:** inspect the actual screens, project components and tokens. Load [flow](references/flow.md) for changed behavior and [build-review](references/build-review.md) for implementation and verification. Work in the existing stack.
- **Review:** load [build-review](references/build-review.md), inspect actual UI and main path when available, report findings before changes. Implement fixes only when asked or when build scope already includes them.
- **Attention, feeds, notifications, onboarding, consent, vulnerable audiences, AI suggestions:** also load [psychology](references/psychology.md). Use it to form design hypotheses, not to diagnose people or claim universal generational effects.

## Working contract

1. Identify the person’s goal, starting point and visible definition of done. Use project facts and observed examples before assumptions. Ask only for information that materially changes the decision and is not discoverable.
2. Define the primary action, why the view exists, and reachable states that change what a person sees or can do. For a significant choice, compare two feasible approaches and name what would overturn the choice. Document the short public rationale, not hidden reasoning.
3. Make choices traceable: **user need → decision → observable expected behavior → actual evidence or not verified**. No manufactured interviews, browser observations, analytics or success scores. Clear decisions are not user validation.
4. For builds, verify the main journey in the running view and one relevant recovery path; inspect mobile and desktop when layout changes, keyboard/focus when changed controls warrant it. If running is unavailable, identify the exact missing evidence. Screenshots prove visible layout, not state persistence or usability.
5. Treat coerced conversion as failure: no fake urgency, asymmetrical consent or deliberately hidden exit. Do not change production data, send messages, purchase tools or deploy without scope authorizing it. Do not execute scripts from references to assess their design guidance.

Report the decision, biggest trade-off, evidence and remaining uncertainty. Keep full research out of routine context.
