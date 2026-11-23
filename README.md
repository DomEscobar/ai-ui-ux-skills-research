# UI/UX-Skills für Coding Agents

**Stand: 22. November 2026.** Eine Recherche zu Skills, die nicht nur bessere Screens erzeugen, sondern entscheiden und begründen, **welche Views Nutzer brauchen, wie sie ihr Ziel erreichen und was schiefgehen kann**.

**Empfehlung für Produkt-Views:** `mblode/product-design` für Entscheidungen und Browser-QA für echte Klickpfade.[1][3]
Für die Umsetzung den vorhandenen Frontend-Workflow verwenden; `mblode/ui-design` ist eine Option, wenn der Stack passt.[2]
Für Website-Art-Direction ist Taste nützlich, aber kein Ersatz für Produkt-UX.[7]

## Eigenes Skill-Bundle

[`product-ux-bundle`](skills/product-ux-bundle/SKILL.md) verbindet Produktentscheidung, Umsetzung, Browser-Abnahme und bedarfsweise Medienpsychologie. Der Ordner ist eigenständig; die Recherche muss für Routineaufgaben nicht mitgeladen werden.

- **A ·** [GitHub-Vergleich: Was wir übernehmen und weglassen](docs/repo-sweep.md)
- **B ·** [Webrecherche: UX-Praxis und Standards](docs/web-practice.md)
- **C ·** [Medienpsychologie: Medienwandel, Aufmerksamkeit, KI-Vertrauen](docs/media-psychology.md)
- [Erste Recherche und Shortlist](RESEARCH.md)
- [Pilot: Ablauf, Prüfkriterien und Vergleich mit/ohne Skill](PILOT.md)

**Status:** eigener Skill-Entwurf, kein Wirksamkeitsnachweis. Drittanbieter-Skills sind verlinkt und nicht kopiert. Keine Fremdskripte erforderlich.

## Animierte Diagramme

[`ani-diagrams` v1.0.0](skills/ani-diagrams/SKILL.md) zeigt **Korrekturen**, **Entscheidungswege** und **Übergaben**. Aus einer JSON-Vorlage entstehen ein animiertes SVG und ein lesbares Standbild; optional lässt sich ein MP4 exportieren.

Beispielclips: [Korrektur](examples/ani-diagrams/change.mp4) · [Entscheidungsweiche](examples/ani-diagrams/branch.mp4) · [Objektübergabe](examples/ani-diagrams/handoff.mp4).

## Kurz installieren (Hermes)

Den vollständigen Ordner `skills/product-ux-bundle` in das `skills/`-Verzeichnis des aktiven Hermes-Profils kopieren. Die drei lokalen Referenzen gehören dazu. Mit `hermes skills list` prüfen, dass `product-ux-bundle` erkannt wird. In einer neuen Sitzung kann der Skill explizit mit `hermes chat --skills product-ux-bundle` geladen werden. Es braucht keine Drittanbieter-Plugins oder Paketinstallationen.

Beispielauftrag: „Entwirf den Meldeablauf für die nächste Wochenliga. Vergleiche zwei Interaktionsvarianten und definiere, woran ein Spieler eine bestätigte Meldung erkennt. Noch nichts bauen.“

## Sources

[1] https://github.com/mblode/agent-skills/blob/main/skills/product-design/SKILL.md
[2] https://github.com/mblode/agent-skills/blob/main/skills/ui-design/SKILL.md
[3] https://github.com/mblode/agent-skills/blob/main/skills/ui-verification/SKILL.md
[7] https://github.com/Leonxlnx/taste-skill
