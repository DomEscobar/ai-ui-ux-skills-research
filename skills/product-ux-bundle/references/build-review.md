# Build and review the actual experience

## Build

Inspect the existing route, state model, terms, components and responsive constraints. Build one complete path before expanding variants. Use task-relevant real or representative content: long labels, realistic counts, sparse and dense data. Choose a composition that makes the task clear. Preserve the original’s useful features; do not replace working controls with decoration. Choose design tokens in the project's system rather than introducing a competing palette or toolkit.

Check semantic controls, focus order/visibility, error notices, labeled fields, contrast, layout/reflow and touch interactions as applicable. Use the relevant standard criteria, not a universal pixel rule. For multiple invalid fields, consider an error summary linked to fields alongside local actionable messages; for a single input a clearly associated local error may suffice.

## Browser evidence

1. Open the running target in scoped test data. Start from a realistic initial state. Observe visible control, destination and expected effect. Read back persisted results after reload if persistence is part of the contract.
2. Try one relevant adverse route: empty data, long content, rejected request, interrupted use or back navigation. Check what the user can infer and do next, and verify no accidental state loss. Do not reproduce disruptive actions in production.
3. Capture matched desktop/mobile when layout changes and check keyboard navigation for changed controls. Use screenshot for visual hierarchy, interaction trace for behavior, and a real user attempt with a neutral task for discoverability. A simulated walkthrough is only a hypothesis. Mark accessibility checks as scoped, never blanket compliance.
4. When reviewing, report up to three material findings by severity. Use **where/when → observed behavior → user consequence → smallest fix → verification**. Distinguish definite bug, supported hypothesis and untested claim. Do not use a general aesthetic score as a release gate.

If no browser or real users are available, report that limit and the next exact check. Do not infer successful behavior from source code, a build, a screenshot or a developer clicking a known shortcut.
