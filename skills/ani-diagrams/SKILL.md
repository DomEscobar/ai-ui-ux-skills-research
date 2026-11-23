---
name: ani-diagrams
description: Use when illustrating a change, branch or handoff in motion.
version: 1.0.0
author: DomEscobar
license: UNLICENSED
platforms: [linux, macos, windows]
---

# Ani Diagrams

Erstelle ein eigenständiges, editierbares Bewegungsdiagramm, dessen Aussage auch als Standbild lesbar bleibt. Deutsch als Standard, sonst Sprache des Briefs. Keine externen Generatoren oder Assets nötig. Bei einer einfachen Statusmeldung, numerischen Datenanalyse oder einem großen Architekturplan nicht automatisch animieren.

## Die Frage bestimmt die Bewegung

- **Was ist neu? → Korrektur** ([Beispiel](templates/change.json)). Gleiche Start- und Endpunkte in zwei Zeilen. Nur der eingefügte Schritt bekommt eine kurz gezeichnete Kontur. Nicht verwenden, wenn sich tatsächlich beide Endpunkte geändert haben.
- **Welche Alternative wird verfolgt? → Entscheidungsweiche** ([Beispiel](templates/branch.json)). Zwei sichtbare Ausgänge, jeweils mit Bedingung und Ergebnis. Nur der konkret gewählte Beispielpfad wird nachgezeichnet. `selected` ist der Index (0 oder 1); die Auswahl nicht als statistische Häufigkeit darstellen.
- **Wer hat das Objekt jetzt? → Objektübergabe** ([Beispiel](templates/handoff.json)). Akteure bleiben ortsfest, nur der benannte Gegenstand wandert. Der Endzustand nennt die Verantwortung. Übergabe ist kein Abschluss und kein Beweis für Zustimmung.

Wenn der Auftrag Varianten verlangt, dieselbe fachliche Regel einfrieren, in jedem Bild genau eine andere Frage beantworten und Videos direkt zeigen. Wenn die Beziehung nicht zu einem Muster passt (etwa mehrere Rückkopplungen), das sagen und einen anderen Diagrammtyp wählen, statt Tatsachen zu erfinden. Ein Textsatz ohne Motion ist eine gültige Alternative.

## Rendern – aus dem Skill-Ordner

1. Passende JSON-Vorlage in den Arbeitsbereich kopieren, dort mit echten Rollen, kurzem Titel, Labels und einem klaren Ergebnissatz füllen. Keine sensiblen Live-Daten einsetzen. `selected` ausdrücklich festlegen. Die Vorlagen sind Datenverträge, keine zu kopierenden PO-Texte.
2. `python3 scripts/draw.py /pfad/spec.json /pfad/neuer-ausgabeordner` schreibt `diagram.svg` und `still.svg` (Python 3, nur Standardbibliothek). Eine belegte Ausgabe wird nicht überschrieben. Bei zu langen Texten die Aussage präzisieren, nicht die Schrift beliebig verkleinern.
3. Für einen zeigbaren Clip `node scripts/export.cjs /pfad/neuer-ausgabeordner` ausführen. Benötigt Node, lokal verfügbares Playwright mit Chromium und FFmpeg mit H.264. Bei nicht standardmäßiger Installation `PW_MODULE` auf das vorhandene Playwright-Paket und `CHROMIUM` auf die vorhandene ausführbare Datei setzen. Nur selbst generierte lokale SVGs rendern. Keine automatische Nachinstallation und kein Upload. Falls der Export fehlt, die funktionierenden SVGs liefern und die Lücke benennen.
4. Der Export produziert `diagram.mp4` (5 Sekunden, einmaliger Ablauf) und `still.png`. Die SVG berücksichtigt reduzierte Bewegung, der MP4-Player nicht: deshalb immer das Standbild oder statische SVG mit anbieten. Für die Weiterbearbeitung JSON und SVG aufheben. Die installierten Vorlagen nicht mit dem Ergebnis überschreiben.

## Abnahme

- Originalregel gegen **Richtung, Auslöser, Auswahl und Endzustand** prüfen. Nicht „versendet“ schreiben, wenn nur „freigegeben“ belegt ist.
- Gerenderte Pixel am Anfang, in der Bewegung und am Ende prüfen; Überlappungen auch innerhalb der Zeichenfläche kontrollieren. Eingebaute Randprüfung ersetzt keinen Blick auf lange Labels. Am vorgesehenen Anzeigeformat prüfen; für schmale eingebettete Ansichten ggf. eigene Hochkant-Komposition statt unlesbarer Verkleinerung.
- Bewegung hat genau einen Fokus, läuft einmal und verdeckt keine Pflichtinformation. Ohne Bewegung muss beispielsweise die aktive Route weiter beschriftet sein oder das Objekt beim Empfänger stehen.
- Bei Auslieferung zuerst den sichtbaren Clip zeigen, dann Quellen anbieten. Nicht „getestet“ melden, wenn nur der SVG-Text generiert wurde. Eine funktionierende Animation ist kein Nachweis von Nutzerverständnis.
