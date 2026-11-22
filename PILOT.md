# Pilot: bessere UX an einer einzigen Aufgabe prüfen

**Status: Testplan, nicht ausgeführt.** Das Beispiel ist eine Designhypothese, keine Aussage über das aktuelle Produktverhalten.

## Aufgabe: Wochenliga im Spiel Bizi

Neutrale Aufgabenstellung: „Du hast dein Team gerade bearbeitet. Finde heraus, ob es für die nächste Runde wirklich gemeldet ist. Falls nicht, melde es an.“

- **Variante A – gemeinsame Ansicht:** Aufstellung und Meldestatus zusammen zeigen. „Aufstellung gespeichert“ und „für nächste Runde gemeldet“ sind unterschiedliche, sichtbar beschriftete Zustände.
- **Variante B – getrennte Ansichten:** Aufstellung und Meldung trennen. Die Aufstellung zeigt, was gespeichert wurde, und führt eindeutig zur Anmeldung. Die Meldungsansicht zeigt Runde und bestätigten Status.
- **Startfavorit A:** eng zusammengehörige Informationen bleiben sichtbar; das kann Suche und Kontextwechsel vermeiden. Variante B kann sinnvoll sein, wenn die Meldungsansicht zusätzliche Voraussetzungen oder mehrere Teams verwaltet. Der Pilot muss zeigen, ob Nutzer den Unterschied der Zustände tatsächlich verstehen.

## View-Vertrag vor der Umsetzung

Für jede relevante View dokumentieren:

1. Rolle, Einstieg und Nutzeraufgabe.
2. Primäre Aktion und Grund für deren Platzierung.
3. Erreichbare Zustände: Laden, leer, bereit, Erfolg, Fehler; pro Zustand den nächsten möglichen Schritt beschreiben.
4. Eine plausible Alternative, den Trade-off und die Evidenz hinter der Entscheidung. Annahmen als solche kennzeichnen.
5. Beobachtbare Akzeptanz: Was sieht oder tut der Nutzer, woran erkennt er Erfolg, und welcher Browsercheck belegt das?

## Browser-Abnahme

Nur in einem Testsystem oder mit isolierten Testdaten ausführen. Nach jedem Schritt den sichtbaren Zustand **und** die erwartete Folge prüfen. Desktop, schmalen mobilen Viewport und Tastaturbedienung getrennt protokollieren.[3]

- Nur speichern: Aufstellung ändert sich; die Oberfläche behauptet nicht, das Team sei gemeldet.
- Erfolgreich melden: Die richtige Runde und der bestätigte Status sind sichtbar und stimmen nach Neuladen weiterhin.
- Fehlgeschlagen melden: Kein falscher Erfolgsstatus; Fehlermeldung und weiterer Schritt sichtbar; gespeicherte Aufstellung bleibt erhalten.
- Fehlende oder geladene Daten: Keine irreführende Bestätigung während des Ladens; leerer Zustand erklärt, was erforderlich ist.
- Belege: je Fall Ergebnis, Testzustand und Screenshot bzw. Ablaufaufzeichnung festhalten. Nicht ausgeführte Fälle explizit markieren.

## Skill-Wirkung getrennt messen

1. Identischer Projektstand, Brief, Modell, Toolzugang und Zeitbudget. In getrennten Arbeitsständen ausführen: **ohne Skill** und **mit `product-design`**. Browserprüfungen für beide identisch. Weitere Skills einzeln zuschalten, wenn ihr Beitrag isoliert werden soll.
2. Varianten ohne Hinweis auf die Herkunft bewerten. Getrennt erfassen: fehlende Zustände, Abweichungen zwischen Begründung und tatsächlicher Implementierung, funktionale Fehler und unbegründete Zusatz-Views.
3. Mit repräsentativen Spielern den neutral formulierten Auftrag testen: erster Klick, Abschluss ohne Hinweis, Fehlannahmen und Verständnis des bestätigten Status beobachten. Nicht nach persönlichem Stilgeschmack statt Aufgabenabschluss werten.[13]
4. Den Versuch mit weiteren Aufgaben und unabhängigen Durchläufen wiederholen, bevor man eine allgemeine Verbesserung behauptet. Ein Pilot zeigt, wo nachgearbeitet werden muss, nicht dass ein Skill überall gewinnt.

## Sources

[3] https://github.com/mblode/agent-skills/blob/main/skills/ui-verification/SKILL.md
[13] https://www.nngroup.com/articles/usability-testing-101
