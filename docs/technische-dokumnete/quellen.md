---
title: Quellen
parent: Technische Dokumente
nav_order: 5
---


# Quellen für PetMatch

In diesem Dokument werden die Quellen die wir für das Projekt verwendeten haben hinterlegt.

# Quellenverzeichnis von Simone Heinrich

## Formular und Button
  - How To Use Web Forms in a Flask Application - [GeeksforGeeks](https://www.geeksforgeeks.org/how-to-use-web-forms-in-a-flask-application/)
  - How to Create a Basic Form in Python Flask - [Python adv](https://python-adv-web-apps.readthedocs.io/en/latest/flask_forms.html)

---

## Dropdown-Menü und Select-Felder
  - Bootstrap Dropdowns - [W3Schools](https://www.w3schools.com/bootstrap/bootstrap_dropdowns.asp)
  - Bootstrap Dropdown Reference - [Getbootstrap](https://getbootstrap.com/docs/5.3/components/dropdowns/)

---

## Template-Engine Jinja2
  - Jinja2 Documentation - [Jinja](https://jinja.palletsprojects.com/)
  - Learn the templating language (Jinja 2) in 10 minutes - [APITemplate](https://docs.apitemplate.io/reference/learn-jinja2.html#learn-the-templating-language-jinja-2-in-10-minutes)

---

## Datenbankoperationen mit Flask und SQLAlchemy
  - SQLAlchemy Documentation - [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
  - SQLAlchemy Unified Tutorial - [SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/latest/tutorial/)

---

## Session-Management in Flask
  - Flask Session - [Flask Documentation](https://flask-session.readthedocs.io/en/latest/)
  - Documentation - [Palletsproject](https://flask.palletsprojects.com/en/stable/quickstart/)
  - Vergleich - [Fullstackstorm](https://dev.to/fullstackstorm/working-with-sessions-in-flask-a-comprehensive-guide-525k)

---

## Datumsformatierung und -validierung
  - Python Datetime Module - [Python Documentation](https://docs.python.org/3/library/datetime.html)
  - Strptime in Python - [Stackoverflow](https://stackoverflow.com/questions/62500829/python-dealing-with-dates/62503693)

---

## Allgemeine Ressourcen
  - Flask Documentation - [Palletsprojects](https://flask.palletsprojects.com/en/latest/)
  - Bootstrap Documentation - [Getbootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

---

## Geoapify Geocoding API und Google Geocoding API
- Geoapify Geocoding API - [Geoapify](https://www.geoapify.com/geocoding-api/)
- Google Geocoding API - [Google](https://developers.google.com/maps/documentation/geocoding?hl=de)  
- Geoapify - Geocoding Python - [Geoapify](https://www.geoapify.com/tutorial/geocoding-python/) 
- Geoapify - Get Started with Maps API - [Geoapify](https://www.geoapify.com/get-started-with-maps-api/) 
- Requests: HTTP for Humans™ - [Python docs](https://docs.python-requests.org/en/latest/)  
- Python Documentation - [Python docs](https://docs.python.org/3/library/http.client.html)
- Oxylabs - HTTPX vs Requests vs AIOHTTP - [Oxylabs](https://oxylabs.io/blog/httpx-vs-requests-vs-aiohttp)    

---

## Branch-Management und .gitignore
- Git Branching: Branches auf einen Blick - [Git-scm](https://git-scm.com/book/de/v2/Git-Branching-Branches-auf-einen-Blick)   
- .gitignore: Atlassian Git Tutorials - [Atlassian](https://www.atlassian.com/git/tutorials/saving-changes/gitignore)   

---

## Formularverwaltung (WTForms vs. Keine zusätzliche Abhängigkeit)
- Flask-WTF Documentation - [Flask-WTF](https://flask-wtf.readthedocs.io/en/latest/)
- Why use WTForms instead of just posting with HTML - [Stackoverflow](https://stackoverflow.com/questions/45973346/why-use-wtforms-instead-of-just-posting-with-html)  

---

## Styling (Bootstrap vs. Keine zusätzliche Abhängigkeit)
- Get started with Bootstrap - [Getbootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) 

---

## Figma-Einbettung und iFrame-Nutzung
- Figma Embed Dokumentation - [Figma](https://www.figma.com/developers/embed#overview)  
- MDN Web Docs - [IFrame](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe)

---

## Einsatz von ChatGPT bei der API-Integration
Zur Integration der Geoapify-API wurde ChatGPT als Unterstützung genutzt, um dynamische Nutzereingaben zu verarbeiten und eine effektive HTTP-Fehlerbehandlung zu implementieren. Die folgenden Prompts wurden in einer logischen Reihenfolge verwendet, um gezielt Lösungen zu erarbeiten:

1. "Vergleiche requests und http.client für Python-APIs. Was sind die Vor- und Nachteile? Bitte gib mir relevante Quellen an."  
2. "Welche Best Practices gibt es für die Fehlerbehandlung bei HTTP-Anfragen in Python?"  
3. "Hier ist mein aktueller Code zur Integration der Geoapify-API, basierend auf der Dokumentation für Geocode a Single Address. Wie kann ich falsche Nutzereingaben effektiv abfangen?"  
4. "Wie funktioniert response.raise_for_status() in der requests-Bibliothek und wann sollte es verwendet werden?"

Durch diese iterative Vorgehensweise wurde die Integration der Geoapify-API erfolgreich an die spezifischen Anforderungen der Anwendung angepasst. Dies führte zu einer stabilen und benutzerfreundlichen Implementierung, die sowohl für Tests als auch für den produktiven Einsatz geeignet ist.

---


# Quellenverzeichnis von Patryk Kujawski

## Vorwort
Bei Internetquellen wurde ein Mozilla Add-on benutzte, was die Seite von Englisch auf Deutsch übersetzt.
Adobe Photoshop 2020 wurde zur Bilderanpassung und Logo Erstellung benutzt.

## Allgemein
- Wi-Inf-M09-F02 Full-Stack Web Development - [Notebook](https://hwrberlin.github.io/fswd/)

---

## Struktur der Pages
- Wi-Inf-M09-F02 Full-Stack Web Development - [Notebook](https://hwrberlin.github.io/fswd/)

---

## Ordnerstruktur der Repo
- Wi-Inf-M09-F02 Full-Stack Web Development - [Notebook](https://hwrberlin.github.io/fswd/)

---

## Markdown
- Getting Startes Narkdown Guid - [Markdownguide](https://www.markdownguide.org/getting-started/)

Nach zwei erstellten Markdown Dateien habe ich Chat GPT mehrmals genutzt mit folgenden Prompt: Wandel folgenden Text in eine Markdown Datei um: "...(Text aus Word kopiert)..." so sehen meine bisherigen Markdown Dateien aus "...(Kopierter Markdown Text)... " behalte die Struktur und Art bei. 

---

## CSS
- CSS Layout - [Mdn web docs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout)
- CSS Website Layout - [W3schools](https://www.w3schools.com/css/css_website_layout.asp)
- Anschauungs Beispiele - [CSS-tricks](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

Chat GPT Prompt: (Bild von einer Farbe hochgeladen) ermittel mir den Farbcode für den hochgeladenen Screenshot.
Chat GPT Prompt: Überprüfe ob diese style.css so "...(CSS Code eingefügt)..." funktionieren würde und ob meine Kommentare plausibel und richtig sind. ggf. korrigiere  diese.

---

## Datenbank
- Recherche SQLite - [Computerwoche](https://www.computerwoche.de/article/2834389/6-gute-gruende-fuer-sqlite.html)
- Recherche Firebase - [Back4App](https://blog.back4app.com/de/was-ist-firebase/)
- How to Use Flask-SQLAlchemy - [Digitalocean](https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application)
- Flask-Login - [Digitalocean](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login-de)

Um die Einträge in der Datenbank zu sehen wurde [SQLite Browser](https://sqlitebrowser.org/) benutzt.

---

## Optik 
- Bootstrap - [Getbootstrap](https://getbootstrap.com/docs/5.3/layout/breakpoints/)
- Formen - [Mdn web docs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Your_first_form)
- Jinja - [Jinja](https://jinja.palletsprojects.com/en/stable/templates/#template-inheritance)

---

## Datenschutz
- Vorlage Datenschutzerklärung - [Datenschutz](https://www.datenschutz.org/datenschutzerklaerung-muster.pdf)

---

## Haversine
- Was ist Haversine - [Rosettacode](https://rosettacode.org/wiki/Haversine_formula)
- Beispiel Haversine - [Nathan](https://nathan.fun/posts/2016-09-07/haversine-with-python/)
- Beispiel 2 Haversine - [Mathyourlife](http://mathyourlife.github.io/spouting-jibberish/Haversine/Haversine.html)

Chat GPT Prompt: Hier ist meine Haversine Formle (...Code eingefügt...) wieso funktioniert diese nicht, erkläre mir meinen Fehler und korrigiere diesen. 

---

# Bilder im Projekt

- anna_mueller.jpeg - [Pinterest](https://de.pinterest.com/pin/68742087759/)
- justin_baecker.jpg - [Pinterest](https://de.pinterest.com/pin/757097387331883067/)  
- erm.png - eigene Darstellung
- alle anderen Bilder wie Logo und Profilbearbeiten Button wurden selbst erstellt und sind eine Eigenkreation
- alle verwebdet Bilder in der Präsentation sind selbst fotografiert, mit der Erlaubnis der Halter.


  