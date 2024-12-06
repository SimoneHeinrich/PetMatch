---
title: Design Entscheidung
nav_order: 3
---

{: .label }
[Jane Dane]

{: .no_toc }
# Design Entscheidung

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

# Arbeitsaufteilung

Beim heutigen Treffen auf Discord haben wir zuerst die Dokumentationsarchitektur besprochen, wie wir diese aufbauen sollen. Da dies unser erstes Projekt dieser Art ist, haben wir uns dafür entschieden, die Architektur des Dozenten Prof. Dr. Eck von [https://github.com/hwrberlin/fswd-app/tree/main](https://github.com/hwrberlin/fswd-app/tree/main) zu übernehmen. Diese wurde auch am 15.11.2024 in unser Repository [https://github.com/studSH/PetMatch](https://github.com/studSH/PetMatch) übernommen. 

## Absprasche vom 15.11.2024 

### Zusammenarbeit 

**Meta**  
- **Status:** laufend  
- **Aktualisierung:** 15.11.2024  

### Problemstellung  
Da es sich hierbei um unser erstes Projekt dieser Art handelt, haben wir uns die Frage gestellt, wie wir effizient zusammenarbeiten können, ohne große Lücken in der Codeerstellung durch das gleichzeitige Arbeiten entstehen. Ein weiteres Problem ist die Aufteilung der zu verrichtenden Arbeiten, sodass die einzelnen Parteien des Projektes auch unabhängig voneinander arbeiten können, ohne dass es zu einem Arbeitsstau kommt. 

### Entscheidung  
Wir haben uns für GitHub entschieden. Dies wurde uns in der Vorlesung vorgestellt, und wir sehen es als ein optimales Werkzeug, um die oben genannten Probleme zu bewältigen. Um einen Arbeitsstau zu verhindern, haben wir uns für folgende Option entschieden:  

Wir teilen uns die Arbeit in **User-Screen-Ansichten** auf, mit der Option, dass wir uns gegenseitig helfen bei Komplikationen oder bei einem nicht vorhersehbaren Mehraufwand:  
- **Erster Screen:** Patryk  
- **Hauptseite:** Simone/Patryk (wir vermuten hier einen großen Aufwand)  
- **Anmeldung:** Patryk  
- **Beiträge verfassen:** Simone  
- **Registrieren:** Patryk  
- **Profil Haustiere:** Simone  

Es wird wie folgt gearbeitet:  
1. **Entwurf erstellen** – Dieser wird der anderen Partei vorgestellt, und es werden Änderungen besprochen.  
2. **Änderung umsetzen** – Die Änderung wird umgesetzt und nochmals vorgestellt.  
3. **Wiederholen** – Diese Schritte werden so lange wiederholt, bis beide Parteien zufrieden sind.  

### Betrachtete Optionen  
Wir haben keine weiteren Optionen der Zusammenarbeit betrachtet. Für uns ist es sehr plausibel, die vorgestellte Art der Zusammenarbeit zu nutzen, da wir uns damit schon beschäftigt haben und es soweit eingerichtet haben, dass es funktioniert. Es wäre ein unnötiger Mehraufwand, sich jetzt noch über andere Optionen zu informieren, da GitHub auch eine Anforderung vom Dozenten ist.  

Bei der Aufgabenaufteilung war unsere erste Idee, diese auf rein **Frontend** und **Backend** zu verteilen. Beim heutigen Meeting ist uns jedoch aufgefallen, dass der Backend-Anteil viel größer und komplexer ist als der vom Frontend. Deswegen haben wir einstimmig entschieden, diese Idee zu verwerfen und die oben genannte Option in **Entscheidung** weiterzuverfolgen. Diese kann sich im Laufe des Projektes noch ändern.  

# API Vergleich


## Vergleich der Geoapify Geocoding API und Google Geocoding API
### Meta

Status  
: **Decided**

Updated  
: 19-Nov-2024

### Problem statement

Für unser Projekt benötigen wir eine API, die Adressen in Geokoordinaten umwandeln kann. Dabei ist es wichtig, dass die API sowohl einfach zu integrieren als auch kosteneffizient ist. Zusätzlich legen wir Wert auf Datenschutz und eine einfache Einrichtung ohne unnötige Komplexität.

Wir haben die **Geoapify Geocoding API** und die **Google Geocoding API** evaluiert, um die beste Wahl für unser Projekt zu treffen.

### Entscheidung

Wir haben uns für die **Geoapify Geocoding API** entschieden.

**Begründung:** Die Geoapify API ist kosteneffizient, leicht einzurichten und bietet ausreichende Funktionalitäten für ein kleines Projekt wie unseres. Mit einer großzügigen kostenlosen Nutzung und ohne Anforderungen an eine Abrechnung passt sie ideal zu den Anforderungen eines Prototypen. Die Nutzung von OpenStreetMap-Daten sorgt zudem für besseren Datenschutz, da keine dauerhafte Speicherung von Nutzerdaten erfolgt.

**Entscheidung getroffen von:** Simone Heinrich, Patryk Kujawski

### Regarded options

Wir haben zwei Optionen evaluiert:

| Merkmal                 | Geoapify Geocoding API                                 | Google Geocoding API                              | Bewertung für unser Projekt               |
|-------------------------|--------------------------------------------------------|---------------------------------------------------|-------------------------------------------|
| **Kosten**              | Kostenlose Nutzung bis 3.000 Anfragen pro Tag; günstige Tarife für Mehrbedarf. | Monatliches Gratis-Guthaben von 200 USD, für bis zu 40.000 Anfragen; Konto mit Abrechnung nötig. | Geoapify ist kostengünstig und ohne Abrechnung ideal für unser kleines Projekt |
| **Einrichtung**         | API-Schlüssel ohne Abrechnungsanforderungen.           | API-Schlüssel nur mit aktivierter Abrechnung.     | Geoapify hat eine einfache Einrichtung ohne Abrechnungszwang |
| **Datenumfang**         | Basisdaten: Koordinaten, Adressstruktur. Zusätzliche Funktionen gegen Gebühr. | Sehr detaillierte Adressdaten und Geodaten.       | Für unsere Zwecke sind die Geoapify-Basisdaten ausreichend |
| **Zusätzliche Funktionen** | Länderspezifische Infos, Zeitzonen (kostenlos nutzbar). | Zusätzliche Standortinformationen (z. B. `location_type`). | Geoapify bietet einige nützliche Funktionen, Google ist detaillierter. |
| **Datenschutz**         | Nutzt OpenStreetMap-Daten, speichert keine Nutzerdaten dauerhaft. | Erfordert Google Cloud-Account und speichert Daten auf Google-Servern. | Geoapify bietet besseren Datenschutz ohne externe Speicherung. |
| **Support und Dokumentation** | Solide Dokumentation, hauptsächlich in Englisch. | Umfangreiche Dokumentation in Deutsch und Englisch. | Google hat umfassendere Doku, Geoapify reicht aber für ein kleines Projekt. |
| **Einsatzbeispiele**    | Ideal für Prototypen, kleine bis mittlere Anwendungen. | Bewährt für umfangreiche kommerzielle Anwendungen mit hohen Anforderungen. | Geoapify ist ideal für Prototypen und kleine Projekte wie unseres. |

### Zusammenfassung der Entscheidung

Die Wahl der Geoapify API liegt in ihrer Einfachheit und Kosteneffizienz, die sich besonders für ein kleines, moderates Projekt wie ein Uni-Projekt anbietet. Geoapify bietet einen unkomplizierten Zugriff ohne Anforderungen an die Abrechnung und eine solide kostenlose Nutzung für bis zu 3.000 Anfragen pro Tag, was für eine solche Anwendung völlig ausreicht. Zudem erfordert Geoapify keine Speicherung sensibler Nutzerdaten auf externen Servern, was den Datenschutz verbessert.

Diese API bietet ausreichende Funktionalität für die Umwandlung von Adressen in Geokoordinaten und ist schnell und einfach integrierbar. Daher eignet sich die Geoapify API für einen ersten Prototyp, bei dem eine moderate Nutzung und einfache Handhabung im Vordergrund stehen.

### Quellen

- Geoapify Geocoding API: [https://www.geoapify.com/geocoding-api/](https://www.geoapify.com/geocoding-api/)
- Google Geocoding API: [https://developers.google.com/maps/documentation/geocoding/](https://developers.google.com/maps/documentation/geocoding/)  
Zugriff 13-Nov-2024


# Datenbank

## Firebase oder SQLite

### Meta

**Status**  
: **Entschieden**

### Problemstellung

In unserem Team stellte sich die Frage, welche Datenbank wir nutzen sollen, da wir auf diverse Daten zugreifen, diese abfragen und organisieren müssen. Viele Funktionen unserer Webentwicklung können nur mit einer Datenbank umgesetzt werden. Außerdem möchten wir die Möglichkeit bieten, Bilder hochzuladen, die für andere sichtbar sind.

### Entscheidung

Wir haben uns für SQLite entschieden, auch wenn wir mit Firebase in App-Entwicklung arbeiten und dies uns eine Echtzeit-Synchronisation ermöglicht, ist dies für unser Projekt nicht von Relevanz, da wir am Ende ein fertiges Projekt abgeben und dieses wird Nutzern nicht zur Verfügung gestellt.

Dementsprechend können wir auch gut auf den Sicherheitsmechanismus von Firebase verzichten. SQLite kommt aus mehreren Gründen für uns in Frage. Wir haben den Umgang mit SQL queries im Modul Datenbanken gelernt und haben ein sehr gutes Beispiel von Prof. Dr. Eck, an dem wir uns orientieren können und diese für unsere Bedürfnisse anpassen werden. Ein weiterer Vorteil ist, dass wir kein Firebase Setup benötigen und die Daten von SQLite lokal gespeichert werden.

### Tabelle

| **Merkmal**                | **SQLite**                          | **Firebase**                          | **Bewertung für das Projekt**                                       |
|-----------------------------|--------------------------------------|---------------------------------------|----------------------------------------------------------------------|
| **Einrichtung**            | Einfach                              | Erfordert Firebase-Setup und Google-Konto | Eine einfache Einrichtung anhand des Beispiels ist vom großen Vorteil. |
| **Echtzeit-Synchronisation** | Nicht möglich                       | Unterstützt Echtzeit                  | Für unser Projekt ist dies irrelevant.                              |
| **Kosten**                 | Kostenlos                            | Kostenlos bis zu einem Limit          | Kein ausschlaggebender Punkt, da unser Projekt bei Firebase nicht das Limit erreichen würde. |
| **Skalierbarkeit**         | Für kleinere Projekte gedacht         | Hoch skalierbar                       | Da wir ein kleines Projekt haben, ist SQLite ausreichend.           |
| **Komplexität**            | Gering                               | Höher bei der Datenmodellierung       | Wir haben uns für den minimalistischen Einsatz entschieden und beschränken uns auf das Wesentliche.                          |
| **Datensicherheit**        | Keine Sicherheitsmechanismen          | Eingebaute Sicherheits-Features       | Da es sich hier um ein Uni-Projekt handelt, sind Sicherheitsmaßnahmen zweitrangig. |

### Quellen

- SQLite: [https://www.computerwoche.de/article/2834389/6-gute-gruende-fuer-sqlite.html](https://www.computerwoche.de/article/2834389/6-gute-gruende-fuer-sqlite.html)
- Firebase: [https://blog.back4app.com/de/was-ist-firebase/](https://blog.back4app.com/de/was-ist-firebase/)  
Zugriff 29-Nov-2024

# Entscheidung für Formularverwaltung (WTForms vs. Keine zusätzliche Abhängigkeit)

## Meta
Status: **Decided**
- **Entscheidung getroffen von:** Simone Heinrich, Patryk Kujawski
- **Erstellt**: 06. Dezember 2024



- **Problemstellung**:  
  Sollten wir WTForms (+ Flask-WTF) verwenden, um Formulare für die Adressumwandlung und Benutzerregistrierung zu erstellen, oder einfache HTML-Formulare ohne zusätzliche Abhängigkeit nutzen?

## Entscheidung
Wir **entscheiden uns für HTML-Formulare ohne zusätzliche Abhängigkeit**.

## Begründung
### Abgewogene Optionen
| Kriterium                     | WTForms (+ Flask-WTF)                            | Keine zusätzliche Abhängigkeit       |
|-------------------------------|--------------------------------------------------|--------------------------------------|
| **Lernaufwand**               | ❌ Erfordert OOP- und Python-Kenntnisse          | ✔️ Kein zusätzlicher Lernaufwand     |
| **Validierung**               | ✔️ Integrierte und robuste Validierungslogik     | ❌ Validierung muss manuell erfolgen |
| **Umsetzungsaufwand**         | ❌ Zusätzliche Konfiguration erforderlich         | ✔️ Schnell umsetzbar                 |
| **Fehleranfälligkeit**        | ✔️ Reduziert durch zentrale Validierungslogik    | ❌ Erhöhte Fehleranfälligkeit        |

### Entscheidungsgrundlage
- **Pro HTML-Formulare ohne Abhängigkeit**:
  - Einfach zu implementieren und anpassbar an unsere spezifischen Anforderungen.
  - Kein zusätzlicher Lernaufwand für Flask-WTF.
  - Da das Projekt nicht produktiv gehen wird, reicht eine manuelle Validierung aus.
- **Contra HTML-Formulare**:
  - Validierung muss sowohl im Frontend als auch im Backend implementiert werden.
- **Pro WTForms**:
  - Bietet saubere Backend-Validierung.
  - Wiederverwendbarkeit für zukünftige Projekte.
- **Contra WTForms**:
  - Höherer initialer Aufwand und komplexere Integration.

## Fazit
Da das MVP keine komplexen Formularanforderungen hat, reicht eine einfache HTML-Lösung aus, um Zeit zu sparen und dennoch funktional zu bleiben.

# Entscheidung für Styling (Bootstrap vs. Keine zusätzliche Abhängigkeit)

## Meta
Status: **Decided**
- **Erstellt**: 06. Dezember 2024
- **Entscheidung getroffen von:** Simone Heinrich, Patryk Kujawski

- **Problemstellung**:  
  Sollten wir Bootstrap verwenden, um ein responsives und modernes Design zu erstellen, oder stattdessen einfache CSS-Regeln verwenden?

## Entscheidung
Wir **entscheiden uns für Bootstrap**.

## Begründung
### Abgewogene Optionen
| Kriterium                     | Bootstrap (+ Bootstrap-Flask)                   | Keine zusätzliche Abhängigkeit       |
|-------------------------------|--------------------------------------------------|--------------------------------------|
| **Lernaufwand**               | ❌ Erfordert Grundkenntnisse in CSS-Frameworks   | ✔️ Kein zusätzlicher Lernaufwand     |
| **Design-Konsistenz**         | ✔️ Einheitliches und modernes Styling            | ❌ Abhängig von individuellen Fähigkeiten |
| **Umsetzungsaufwand**         | ✔️ Schnelles Prototyping mit vorgefertigten Komponenten | ❌ Manuelle Erstellung erforderlich |
| **Performance**               | ❔ Zusätzlicher Code kann Performance beeinflussen | ✔️ Minimaler Ressourcenverbrauch     |

### Entscheidungsgrundlage
- **Pro Bootstrap**:
  - Bietet vorgefertigte Komponenten wie Formulare, Navigation und Buttons, die direkt verwendet werden können.
  - Ermöglicht ein responsives Design ohne großen Mehraufwand.
- **Contra Bootstrap**:
  - Einführung in das Framework erfordert eine Lernkurve.
  - Abhängigkeit von externem Code.
- **Pro keine Abhängigkeit**:
  - Minimaler Ressourcenverbrauch und einfache Kontrolle über das Design.
  - Kein zusätzlicher Code, der gepflegt werden muss.
- **Contra keine Abhängigkeit**:
  - Erfordert mehr Zeit für die manuelle Erstellung von responsive Layouts und Design-Komponenten.

## Fazit
Bootstrap ist ideal, um mit wenig Aufwand ein konsistentes und modernes Design zu erreichen, das unseren UI-Anforderungen gerecht wird. Der zusätzliche Lernaufwand ist minimal im Vergleich zum Nutzen für das Projekt.

