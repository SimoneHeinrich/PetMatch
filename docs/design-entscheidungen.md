---
title: Design Entscheidung
nav_order: 3
---

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

# Designentscheidung: Einführung von Branch-Management und `.gitignore`

### Meta
- **Status:** Entschieden
- **Datum:** 30. November 2024
- **Entscheidung getroffen von:** Simone Heinrich, Patryk Kujawski

---

### Problemstellung
Zu Beginn der Arbeit am Projekt haben wir beide direkt auf der `main`-Branch gearbeitet. Dies führte zu erheblichen Problemen:
- Gleichzeitige Änderungen führten regelmäßig zu Konflikten, die manuell gelöst werden mussten.
- Fehlende `.gitignore`-Datei führte dazu, dass automatisch generierte Dateien wie `__pycache__` getrackt wurden, was das Repository unnötig aufgebläht hat.
- Zeitverlust durch ständige Konfliktlösung und Überprüfungen, bevor Änderungen gepusht werden konnten.

---

| Kriterium                        | Arbeiten direkt auf `main`           | Einführung von Branch-Management    |
|----------------------------------|--------------------------------------|-------------------------------------|
| **Konflikte minimieren**         | ❌ Häufige Konflikte beim Pullen und Pushen | ✔️ Reduzierte Konflikte durch isolierte Branches |
| **Codequalität**                 | ❌ Keine Möglichkeit, Änderungen vorab zu testen | ✔️ Änderungen können vor Merge überprüft werden |
| **Lernaufwand**                  | ✔️ Kein zusätzlicher Aufwand          | ❌ Einführung von Git-Workflows erforderlich |
| **Effizienz bei Teamarbeit**     | ❌ Gering, da Konflikte manuell gelöst werden müssen | ✔️ Verbesserte Effizienz durch paralleles Arbeiten |
| **Nachvollziehbarkeit der Änderungen** | ❌ Änderungen schwer zuzuordnen       | ✔️ Klare Commit-Historie pro Feature |
| **Repositories und Datenaufblähung** | ❌ Kein Mechanismus, um unerwünschte Dateien wie `__pycache__` auszuschließen | ✔️ `.gitignore` verhindert Tracking unnötiger Dateien |
| **Skalierbarkeit**               | ❌ Ungeeignet für größere Teams, da Konflikte zunehmen | ✔️ Ermöglicht paralleles Arbeiten, auch bei großen Projekten |
| **Zeitaufwand für Problemlösungen** | ❌ Hoher Aufwand durch manuelle Konfliktlösung | ✔️ Geringer durch klarere Struktur und isolierte Branches |


### Entscheidung
Wir haben uns entschieden, ein Branch-Management-System einzuführen und eine `.gitignore`-Datei hinzuzufügen.

#### Begründung:
- **Branch-Management:**
  - Jeder arbeitet auf einem eigenen Branch (z. B. `feature-login` oder `feature-profile`), um Änderungen voneinander zu trennen.
  - Die `main`-Branch bleibt stabil und enthält nur funktionierenden Code.
  - Konflikte werden minimiert, da Änderungen unabhängig entwickelt und nach Abschluss gemerged werden.

- **.gitignore:**
  - Eine `.gitignore`-Datei verhindert, dass automatisch generierte Dateien wie `__pycache__` oder andere temporäre Dateien getrackt werden.
  - Dies reduziert die Größe des Repositories und sorgt für eine saubere Commit-Historie.

---

### Schritte zur Umsetzung
1. Einführung von Branch-Management:
   - Jeder erstellt vor Änderungen einen neuen Branch mit:
     ```bash
     git checkout -b feature-name
     ```
   - Nach Abschluss des Features wird der Branch in `main` gemerged:
     ```bash
     git checkout main
     git pull origin main
     git merge feature-name
     git push origin main
     ```

2. Erstellung der `.gitignore`:
   - Eine `.gitignore`-Datei wurde hinzugefügt mit Einträgen wie:
     ```gitignore
     __pycache__/
     *.pyc
     *.log
     ```
   - Dadurch werden unerwünschte Dateien vom Tracking ausgeschlossen.

---

### Zusammenfassung
Die Einführung des Branch-Managements und der `.gitignore`-Datei hat die Zusammenarbeit im Projekt erheblich verbessert. Konflikte treten seltener auf, und die Commit-Historie ist klarer nachvollziehbar. Dieser Workflow ermöglicht es, effizienter und strukturierter zu arbeiten, während die Codequalität auf der `main`-Branch stets gewährleistet bleibt.

### Quellen
- Git Branching: https://git-scm.com/book/de/v2/Git-Branching-Branches-auf-einen-Blick
- .gitignore: https://www.atlassian.com/git/tutorials/saving-changes/gitignore
Zugriff 28-Nov-2024

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

| Kriterium            | WTForms (+ Flask-WTF)                 | Keine zusätzliche Abhängigkeit       |
|----------------------|----------------------------------------|--------------------------------------|
| **Lernaufwand**      | ❌ Erfordert OOP- und Python-Kenntnisse | ✔️ Kein zusätzlicher Lernaufwand     |
| **Validierung**      | ✔️ Integrierte und robuste Validierungslogik | ❌ Validierung muss manuell erfolgen |
| **Umsetzungsaufwand**| ❌ Zusätzliche Konfiguration erforderlich | ✔️ Schnell umsetzbar                 |
| **Fehleranfälligkeit**| ✔️ Reduziert durch zentrale Validierungslogik | ❌ Erhöhte Fehleranfälligkeit        |

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

| Kriterium            | Bootstrap (+ Bootstrap-Flask)                 | Keine zusätzliche Abhängigkeit       |
|----------------------|-----------------------------------------------|--------------------------------------|
| **Lernaufwand**      | ❌ Erfordert Grundkenntnisse in CSS-Frameworks | ✔️ Kein zusätzlicher Lernaufwand     |
| **Design-Konsistenz**| ✔️ Einheitliches und modernes Styling         | ❌ Abhängig von individuellen Fähigkeiten |
| **Umsetzungsaufwand**| ✔️ Schnelles Prototyping mit vorgefertigten Komponenten | ❌ Manuelle Erstellung erforderlich |
| **Performance**      | ❔ Zusätzlicher Code kann Performance beeinflussen | ✔️ Minimaler Ressourcenverbrauch     |


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

# Anpassung der Routen

## Meta
Status: **offen**
- **Entscheidung getroffen von:** Simone Heinrich, Patryk Kujawski
- **Erstellt**: 21. Dezember 2024

## Problemstellung

Bei der Umsetzung des MVPs ist aufgefallen, dass zusätzliche Routen erforderlich sind, um die Projektvoraussetzungen zu erfüllen und um alle geplanten Funktionen abzubilden. Für den Bereich „Mein Profil“ benötigen wir sowohl eine Route zum Anzeigen als auch eine Route zum Bearbeiten des Profils. Darüber hinaus müssen wir für die Umwandlung von Adressen in Längen- und Breitengrade zusätzliche Backend-Routen (z. B. sowas wie „api-konvertiert“ und „api-feed“) einrichten. Für die Übersichtlichkeit sollten Standardrouten wie Datenschutz, Impressum und Kontakt auch hinzugefügt werden.

Eine Herausforderung wird es sein, die neuen Routen sinnvoll in die Architektur zu integrieren, ohne die Arbeitsaufteilung aus dem Gleichgewicht zu bringen. Gleichzeitig sollen die Änderungen so vorgenommen werden, dass künftige Anpassungen an Hauptseiten oder zusätzlichen Backend-Funktionalitäten problemlos möglich sind.

### Betrachtete Optionen

| **Option**                                  | **Bewertung**                                                                                     |
|---------------------------------------------|---------------------------------------------------------------------------------------------------|
| **Keine neuen Routen hinzufügen**           | Keine Option, da dann das MVP unvollständig sein wird                                            |
| **Alle neuen Routen von einer Person bearbeiten lassen** | Zu große Arbeitsbelastung und sehr unfaire Verteilung                                            |
| **Routen gleichmäßig aufteilen**            | Faire Verteilung und Verantwortlichkeit, bei Mehraufwand oder Problemen wird geholfen            |

### Entscheidung

Wir haben beschlossen, die genannten Routen in unsere bestehende Architektur zu integrieren und sinnvoll aufzuteilen. Die Profilfunktion wird in zwei Routen aufgeteilt (Profil anzeigen und Profil bearbeiten). Die API-Routen für die Koordinatenbestimmung werden gesondert umgesetzt und die Standardrouten (Datenschutz, Impressum, Kontakt) als separate Seiten integriert. Die Aufteilung bleibt im Wesentlichen erhalten. Falls an einzelnen Stellen ein größerer Arbeitsaufwand entsteht, bieten wir gegenseitige Unterstützung an. Die Aufteilung bleibt vorerst wie am 15.11.2024 vereinbart bestehen.

### Quellen

- User Interfaces | Full-Stack Web Dev @HWR Berlin URL: GitHub Repository
- Mitschrift Vorlesung Web-Entwicklung an der HWR Berlin bei Prof. Dr. Eck 6.12..docx 
- Get started with Bootstrap · Bootstrap v5.3
Zugriff 6-Dezember-2024

# Nutzung von Flask-Session

## Meta
Status: **Decided**
- **Entscheidung getroffen von:** Simone Heinrich
- **Erstellt**: 12. Januar 2025 Nachtrag zum 20. Dezember 2024 Implementierung profil-bearbeiten-URL

## Problemstellung
Bei der Implementierung der Route `profil_bearbeiten` war es notwendig, dass Nutzerdaten über verschiedene Routen hinweg verfügbar bleiben. Dieses Problem ergibt sich aus folgenden Anforderungen:
1. **Benutzeridentifikation:** Es muss sichergestellt sein, dass nur der aktuell angemeldete Nutzer seine Daten bearbeiten kann.
2. **Datensicherheit:** Sensible Informationen wie die E-Mail-Adresse sollen nicht nur clientseitig (z. B. als Cookies), sondern auch serverseitig verfügbar sein.
3. **Routing:** Der Benutzer muss zukünftig zwischen mehreren Seiten wechseln können, ohne dass die Anmeldung oder die Daten des Nutzers verloren gehen.

## Entscheidung
Ich habe mich für die Verwendung von Flask-Session entschieden. Mit Flask-Session können wir Nutzerdaten wie die E-Mail-Adresse serverseitig speichern und während der Sitzung abrufen. Die Session ermöglicht außerdem eine sichere Verwaltung von Benutzerdaten, ohne dass diese explizit in jeder Route übergeben werden müssen.

## Betrachtete Alternativen

| **Option**                     | **Bewertung**                                                                                                 |
|--------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Flask-Session**              | Einfach zu implementieren, ideal für Entwicklungsphasen. Keine zusätzliche Logik für Cookie-Verwaltung nötig. |
| **Manuelle Cookie-Verwaltung** | Flexibler, aber komplexer. Erfordert eigene Implementierung der Authentifizierung und Datenverwaltung.         |

## Pro & Contra

| **Kriterium**                | **Flask-Session**                                                                                 | **Manuelle Cookie-Verwaltung**                                                       |
|------------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **Implementierungsaufwand**  | ✔️ Minimaler Aufwand – Integration mit wenigen Zeilen Code.                                       | ❌ Höherer Aufwand – erfordert detaillierte Logik für Cookie-Erstellung und -Validierung. |
| **Benutzerfreundlichkeit**   | ✔️ Einfaches Arbeiten mit serverseitig gespeicherten Sitzungsdaten.                              | ❌ Aufwendigere Nutzung – Nutzerinformationen müssen in jedem Request mitgesendet werden. |
| **Datensicherheit**          | ✔️ Serverseitige Speicherung sorgt für höhere Sicherheit im Vergleich zu rein clientseitigen Cookies. | ❌ Erhöhtes Risiko bei unsicherer Implementierung – z. B. durch unsichere Cookies.       |
| **Flexibilität**             | ❌ Weniger flexibel, da an Flask-Mechanismen gebunden.                                            | ✔️ Höhere Anpassungsmöglichkeiten für spezielle Anwendungsfälle.                      |


### Zusammenfassung
Die Entscheidung für Flask-Session ermöglicht eine einfache und sichere Umsetzung der `profil_bearbeiten`-Route. Die E-Mail des Nutzers wird beim Login in der Session gespeichert und bleibt während der Sitzung verfügbar. Dies erlaubt serverseitige Datenabfragen, ohne dass sensible Informationen wie die E-Mail-Adresse explizit im Frontend gespeichert werden müssen. Durch den statischen Key verzichte ich auf zusätzliche Abhängigkeiten wie externe Bibliotheken oder Services (z. B. Redis oder JWT). Dies reduziert die Komplexität und hält die App schlank.

### Quellen
- Flask-Session: https://flask-session.readthedocs.io/en/latest/
Zugriff 12. Januar 2025
- Flask Documentation: https://flask.palletsprojects.com/en/2.3.x/quickstart/#sessions
Zugriff 12. Januar 2025
- Flask-Login Documentation: https://flask-login.readthedocs.io/en/latest/
Zugriff 12. Januar 2025

# Nutzung der `requests`-Bibliothek

## Meta
Status: **Entschieden**
- **Entscheidung getroffen von:** Simone Heinrich
- **Erstellt**: 12. Januar 2025 

## Problemstellung

Im Rahmen der Geoapify-API-Integration mussten Adressdaten in Geo-Koordinaten umgewandelt werden, um sie in der App zu speichern. Dabei gab es zwei mögliche Ansätze:
1. Die Nutzung der `requests`-Bibliothek.
2. Die Implementierung mit der nativen Python-Bibliothek `http.client`.

Da die Integration in kurzer Zeit und mit möglichst geringer Fehleranfälligkeit umgesetzt werden sollte, stellte sich die Frage, welche Lösung für das Projekt besser geeignet ist.

**Begründung**:
Die `requests`-Bibliothek bietet eine benutzerfreundliche und effiziente Möglichkeit, HTTP-Requests umzusetzen. Sie reduziert den Entwicklungsaufwand und bietet robuste Fehlerbehandlung, die insbesondere bei der Arbeit mit externen APIs von Vorteil ist. Dadurch bleibt mehr Zeit für die Implementierung und Optimierung anderer Projektbestandteile.

Die iterative Entwicklung begann mit einer einfachen Implementierung basierend auf der Geoapify-API-Dokumentation[1], welche jedoch bei ungültigen Adressen und HTTP-Fehlern zu Abstürzen führte. Mithilfe von ChatGPT wurden gezielt Lösungsansätze getestet, z. B. durch Prompts wie:
- "Vergleiche requests und http.client für Python-APIs. Was sind die Vor- und Nachteile, gebe mir Quellen an."
- "Hier ist meine bisherige Lösung zur Integration der geoapify: (code aus der Quelle) angelehnt am Beispiel in der Quelle der Geoapify-Dokumentaiton für Gecode a Single Address. Wie fange ich falsche Nutzereingaben ab?" 
- "Wie fange ich HTTP-Fehler in Python ab?"
- "Wie funktioniert `response.raise_for_status()` in requests?"

## Betrachtete Optionen

| **Kriterium**               | **`requests`-Bibliothek**                                               | **`http.client`**                                                             |
|-----------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **Benutzerfreundlichkeit**  | 🟢 Einfache, intuitive Syntax für HTTP-Requests.                      | 🔴 Komplexere Syntax, da Header, Parameter und Body manuell formatiert werden müssen. |
| **Codeumfang**              | 🟢 Weniger Code, da viele Funktionen vorkonfiguriert sind.           | 🔴 Längere und fehleranfälligere Implementationen durch manuelle Arbeitsschritte. |
| **Flexibilität**            | 🟢 Unterstützt Features wie Timeout, Sessions und JSON-Payload nativ.| 🟠 Unterstützung vorhanden, aber aufwendiger zu implementieren.            |
| **Projektabhängigkeiten**   | 🔴 Erfordert Installation einer neuen Bibliothek.                    | 🟢 Keine zusätzlichen Abhängigkeiten, da `http.client` Teil der Standardbibliothek ist. |
| **Fehlermanagement**        | 🟢 Integrierte Methoden wie `raise_for_status()` erleichtern Debugging. | 🔴 Fehler müssen detaillierter und aufwendiger abgefangen werden.           |


## Vorteile der `requests`-Bibliothek

1. **Benutzerfreundlichkeit**  
   Die Bibliothek ermöglicht eine intuitive Umsetzung von HTTP-Requests und reduziert den Codeumfang erheblich.

2. **Zeitersparnis**  
   Funktionen wie `response.json()` und `raise_for_status()` beschleunigen die Entwicklung und verbessern die Effizienz.

3. **Robustheit**  
   Die integrierte Fehlerbehandlung sorgt dafür, dass HTTP- und Netzwerkfehler besser abgefangen werden.

4. **Komplexitätsreduktion**  
   Vorkonfigurierte Features wie Parameterencoding und Timeout erleichtern die Arbeit mit APIs erheblich.


## Zusammenfassung

Die Entscheidung für die `requests`-Bibliothek hat die Umsetzung der Geoapify-API-Integration wesentlich vereinfacht und beschleunigt. Obwohl dadurch eine zusätzliche Projektabhängigkeit eingeführt wurde, war der Nutzen im Hinblick auf Benutzerfreundlichkeit, Robustheit und Entwicklungszeit deutlich größer als der Nachteil.

Die iterative Entwicklung der Lösung – mithilfe von ChatGPT und den unten aufgeführten Quellen – hat es ermöglicht, die API Integration mithilfe eines kompakten und leicht verständlichen Codes (geoapify.py und dem Funktionsaufruf im profil-bearbeiten-routing in der app.py) umzusetzen und ein robustes System zu entwickeln, das HTTP-Fehler und ungültige Eingaben abfängt und damit die Nutzerfreundlichkeit erhöht.

### Quellen

- Geoapify - Geocoding Python Tutorial: [https://www.geoapify.com/tutorial/geocoding-python/](https://www.geoapify.com/tutorial/geocoding-python/)  
Zugriff am 12. Januar 2025

- Geoapify - Get Started with Maps API: [https://www.geoapify.com/get-started-with-maps-api/](https://www.geoapify.com/get-started-with-maps-api/)  
Zugriff am 12. Januar 2025

- Requests: HTTP for Humans™: [https://docs.python-requests.org/en/latest/](https://docs.python-requests.org/en/latest/)  
Zugriff am 12. Januar 2025

- Python Documentation - `http.client`: [https://docs.python.org/3/library/http.client.html](https://docs.python.org/3/library/http.client.html)  
Zugriff am 12. Januar 2025

- Oxylabs - HTTPX vs Requests vs AIOHTTP: [https://oxylabs.io/blog/httpx-vs-requests-vs-aiohttp](https://oxylabs.io/blog/httpx-vs-requests-vs-aiohttp)  
Zugriff am 12. Januar 2025