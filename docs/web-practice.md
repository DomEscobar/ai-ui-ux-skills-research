# B · Praxis und Standards außerhalb von GitHub

| Quelle / Evidenzart | Transfer ins Bundle | Grenze |
| --- | --- | --- |
| [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) · Webstandard | Relevante Kriterien benennen und prüfen: Tastatur, Fokus, Zielgröße mit Ausnahmen, Fehler, Status und Reflow | Automatisierte Prüfung oder visuelle Sichtung allein belegt keine Konformität |
| [W3C COGA: Making Content Usable](https://www.w3.org/TR/coga-usable/) · ergänzende Working Group Note | Klarer Zweck, konsistente Begriffe, Wiedereinstieg nach Unterbrechung, Hilfe zur richtigen Zeit | Ergänzt WCAG; nicht mit normativen Erfolgskriterien gleichsetzen |
| [GOV.UK Error Summary](https://design-system.service.gov.uk/components/error-summary/) · erprobtes Praxispattern | Bei umfangreichen Formularen: Sprung zu betroffenen Feldern und konkrete lokale Fehlerkopie, Eingaben erhalten | Bei einem einzelnen Feld reicht oft die lokale, gut angekündigte Meldung |
| [Baymard Checkout](https://baymard.com/blog/checkout-flow-ux-optimization) · eigene E-Commerce-Tests | Bei Transaktionen unnötige Konto- und Eingabehürden überprüfen; Fehler in Nutzersprache | Checkout-Befunde nicht pauschal auf Spiel, Behördenprozess oder Admin übertragen |
| [NN/g Usability Testing](https://www.nngroup.com/articles/usability-testing-101/) · Forschungsmethode | Neutrale Aufgabe, keine Lösung verraten; ersten Klick, Abschluss ohne Hilfe und Fehlannahmen beobachten | Astreiner Browser-Test misst keine Auffindbarkeit für neue Nutzer |
| [Design Theater v2](https://arxiv.org/html/2607.22928v2) · Preprint, Benchmark | Zusagen gegen tatsächliche UI und Zustände prüfen. Im Benchmark mit 120 Interfaces aus fünf Tools blieb im Schnitt rund ein Viertel der beschriebenen Designentscheidungen unimplementiert, bei funktionalen Anforderungen rund 34 %. | Bestimmte Tools, Aufgaben und HTML/CSS/JS-Rahmenbedingungen; kein Benchmark dieses Bundles und kein Ersatz für Nutzertests |

## In der Praxis bedeutet das

1. **Vor dem Pixel:** Nutzeraufgabe, Einstieg, Abschluss und beobachtbares Ergebnis festlegen. Bei komplexen Aufgaben zwei echte Interaktionsvarianten abwägen; zwei Farbpaletten sind keine UX-Alternative.
2. **Während des Builds:** vorhandene Komponenten und Begriffe benutzen; statische Screens nicht mit funktionaler Umsetzung verwechseln. Ein Screen braucht keinen Hero, wenn er zum Arbeiten und nicht zum Überzeugen dient.
3. **Beim Review:** zuerst funktionale Schwere, dann Verständnis, dann visueller Feinschliff. Nicht „sieht AI aus“, sondern „die gleich gewichteten Karten verstecken den einzigen nächsten Schritt auf Mobil“.
4. **Beim Nachweis:** Layout-Screenshot für visuelle Aussagen, Interaktionsbelege für Verhalten, Nutzertest für Auffindbarkeit. Explizit trennen.
