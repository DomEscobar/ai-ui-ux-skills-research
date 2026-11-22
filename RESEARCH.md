# Recherche: Agent-Skills für begründete UI/UX

## Wonach wir gesucht haben

Der Agent soll nicht sofort Layout oder CSS erzeugen. Er soll zunächst die Nutzeraufgabe, eine sinnvolle Informationsarchitektur, die Erreichbarkeit wichtiger Zustände und einen sichtbaren Erfolgsnachweis bestimmen. Bewertung nach vier Fragen: Hilft das Skill-Dokument bei der **UX-Entscheidung**, verlangt es eine **nachvollziehbare Begründung**, unterstützt es **Implementierung** oder die **Überprüfung am laufenden Produkt**?

Grundlage sind veröffentlichte Skill-Dateien und Autorendokumentation. Die Reihenfolge ist eine Empfehlung nach Aufgabenfit, nicht nach GitHub-Sternen, Modellleistung oder gemessenem Nutzen. Keine Installation und kein eigener A/B-Test.

## Shortlist

### 1. mblode: `product-design` → `ui-design` → `ui-verification`

**Erste Wahl für funktionale App-Views.** `product-design` spezifiziert die Nutzeraufgabe, Abläufe und Zustände, bevor Code geschrieben wird. `ui-design` ist die Umsetzungsstufe und orientiert sich an React-/Next-/Tailwind-Konventionen. `ui-verification` arbeitet am gerenderten Produkt und deckt unter anderem kleine Viewports, lange Inhalte sowie leere oder fehlerhafte Zustände ab.[1][2][3]

**Grenze:** Wenn der Stack nicht passt, die UX-Spezifikation übernehmen, nicht die Frontend-Konventionen erzwingen. Ein bestandener Browser-Klickpfad ist noch kein Beleg dafür, dass ein Mensch den Einstieg ohne Hinweise entdeckt.

### 2. magnus919: `product-design-and-ux`

**Kandidat für komplexe Entscheidungen und begründete Trade-offs.** Der Skill führt von Nutzerzielen und verfügbarer Evidenz zu Informationsarchitektur, Interaktionen, Zuständen und Abnahmekriterien. Besonders passend für KI-unterstützte Abläufe: Entscheidungsspielraum der KI, menschliche Kontrolle und Umgang mit Unsicherheit.[4]

**Grenze:** Vor allem UX-Entwurf, kein eigener Frontend-Builder. Für eine einfache View ist der schlankere mblode-Ablauf mein Startpunkt.

### 3. Impeccable: `shape` und `critique`

**Allrounder für neues Briefing und bestehende Views.** `shape` hilft vor der Umsetzung, die Nutzeraufgabe und offene Produktentscheidungen zu konkretisieren. `critique` priorisiert Probleme wie mangelnde Hierarchie und unklare Bedienung. Ein guter Einsatzfall: „Diese View wirkt falsch – zeig mir, woran es liegt und was ich zuerst ändern soll.“[5][19]

**Grenze:** Ein simulierter Nutzer-Walkthrough liefert Hypothesen. Ob echte Nutzer ihre Aufgabe ohne Hilfestellung schaffen, muss separat beobachtet werden.[13][19]

### 4. humbleteam: `design-review`

**Zweitmeinung und Variantenvergleich.** Das Format Vorher → Nachher → Warum macht Vorschläge greifbar; die Dokumentation verweist auf Nielsen-Heuristiken, WCAG und Plattformleitlinien. Am besten als Reviewer einsetzen, nicht als Builder. Konkrete Belege sind wertvoller als ein aggregierter Score.[33]

## Sinnvolle Ergänzungen, aber nicht als UX-Hauptskill

- **Taste Skill:** Art Direction, visuelle Referenzen und Browserchecks. Gute Ergänzung für einen bestehenden Redesign-Workflow; entscheidet nicht allein über den besten Produktablauf.[7]
- **Anthropic `frontend-design`:** setzt eine bewusste visuelle Richtung und hilft gegen generisches Frontend-Styling. Nach Klärung der Nutzeraufgabe einsetzen.[8]
- **UI UX Pro Max:** nützlich als Nachschlagewerk für Designsysteme, Stil, Typografie, Branchenmuster und UX-Regeln. Für eine schwierige Entscheidung über Navigation, Status oder Fehlerbehebung würde ich zuerst einen produktorientierten Skill nehmen.[9]

## Warum Begründung und Umsetzung getrennt geprüft werden müssen

*Design Theater* (arXiv v2) untersucht 120 generierte Interfaces aus fünf Tools anhand von 24 Aufgaben. Im Mittel waren rund 25 % der in den nutzerseitigen Begründungen beschriebenen Elemente nicht umgesetzt; in der funktionalen Aufgabengruppe waren es 34 %. Die Zahlen beschreiben die Übereinstimmung von Begründung und Implementierung in diesem Benchmark. Sie messen weder reale Nutzererfolge noch die Wirksamkeit der hier empfohlenen Skills.[16]

**Folgerung für den Workflow:** Jede wichtige UX-Entscheidung bekommt einen sichtbaren, prüfbaren Nachweis in der laufenden View. Beobachtete Nutzertests sind davon getrennt: Ein Teilnehmer soll die Aufgabe ausführen, ohne dass ein Moderator die Bedienung verrät.[13][16]

Praktisch: **Nutzeraufgabe → Views und Zustände → Alternative und Trade-off → Build → Browser-Nachweis → Beobachtung mit Nutzern.** Siehe [Pilot](PILOT.md).

## Sources

[1] https://github.com/mblode/agent-skills/blob/main/skills/product-design/SKILL.md
[2] https://github.com/mblode/agent-skills/blob/main/skills/ui-design/SKILL.md
[3] https://github.com/mblode/agent-skills/blob/main/skills/ui-verification/SKILL.md
[4] https://github.com/magnus919/agent-skills/blob/main/product-design-and-ux/SKILL.md
[5] https://impeccable.style/docs/shape
[7] https://github.com/Leonxlnx/taste-skill
[8] https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md
[9] https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
[13] https://www.nngroup.com/articles/usability-testing-101
[16] https://arxiv.org/html/2607.22928v2
[19] https://impeccable.style/docs/critique
[33] https://github.com/humbleteam/design-review
