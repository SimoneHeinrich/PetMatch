---
title: Architektur
parent: Technische Dokumente
nav_order: 1
---


{: .no\_toc }

# Architektur

## Überblick

PetMatch ist eine Webanwendung, die Tierhalter dabei unterstützt, Spielkameraden für ihre Haustiere zu finden. Durch ein datenbankgestütztes Matching basierend auf Standortinformationen und Tierpräferenzen bietet die Plattform eine einfache Möglichkeit zur Vernetzung von Haltern in Wohnortnähe.
Die Anwendung besteht aus einem **Flask-Backend**, einer **SQLite-Datenbank** und einer **Bootstrap-basierten Weboberfläche**. Die API-Integration ermöglicht die Umwandlung von Adressdaten in Geo-Koordinaten, um nahegelegene Tierhalter zu identifizieren.

---

## Strukturübersicht

Die Anwendung ist in **drei Hauptbereiche** unterteilt:

### 1. Frontend

- **HTML-Templates:** Strukturieren die Benutzeroberfläche und ermöglichen die Darstellung dynamischer Inhalte.
- **Bootstrap:** Dient zur Gestaltung eines responsiven und modernen Designs.
- **Jinja-Templates:** Ermöglichen die dynamische Integration von Backend-Daten.

### 2. Backend

- **Flask:** Verantwortlich für das Routing, die Verarbeitung von HTTP-Anfragen und die API-Kommunikation.
- **SQLAlchemy:** ORM für die Interaktion mit der SQLite-Datenbank.
- **Geoapify API:** Dient zur Umwandlung von Adressen in Geo-Koordinaten.
- **Flask-Session:** Speichert Benutzeranmeldedaten während der Session.

### 3. Datenbank (SQLite)

- **Benutzer:** Enthält Anmeldeinformationen.
- **Halter:** Speichert persönliche Informationen und Standortdaten von Tierhaltern.
- **Tier:** Enthält Daten zu Haustieren wie Name, Rasse, Geschlecht, Vorlieben und Abneigungen.
- **Feedbeitrag:** Ermöglicht das Posten von Beiträgen durch Halter.
- **Bild:** Speicherung von Bildern zu Beiträgen (optional).

---

## Querschnittsthemen

### Datenmodell

Die Anwendung nutzt eine relationale SQLite-Datenbank, in der jeder **Halter genau ein Tier besitzt**. Beiträge im Feed sind mit dem jeweiligen Tier und Halter verknüpft. Die Speicherung erfolgt in einer **lokalen SQLite-Datenbank**, die im `instance`-Ordner der Anwendung abgelegt wird.

### Authentifizierung & Sitzungsverwaltung

- Die Benutzeranmeldung erfolgt über E-Mail und Passwort.
- Die Anmeldungssitzung wird über das `session`-Dictionary von Flask gespeichert, indem die E-Mail des angemeldeten Benutzers hinterlegt wird.
- Beim Logout wird die Sitzung durch `session.clear()` beendet.

### Geo-Location & API-Integration

- Adressen der Halter werden in Geo-Koordinaten umgewandelt, indem die **Geoapify API** genutzt wird.
- Die gespeicherten Standortdaten werden verwendet, um die Entfernung zwischen Tierhaltern mit der **Haversine-Formel** zu berechnen.
- Nutzer können Beiträge nach Entfernung filtern.

### Beiträge & Medienverwaltung

- Tierhalter können Beiträge im Feed veröffentlichen, um Spielpartner für ihr Tier zu finden.
- Jeder Beitrag enthält einen Titel, einen Inhalt und das Erstellungsdatum.
- Die Beiträge sind mit dem jeweiligen Tier und Halter verknüpft.
- Bilder können zwar mit der Klasse `Bild` in der Datenbank gespeichert werden, sind aber noch **nicht implementiert**.

### Profilverwaltung

- Halter können ihr Profil bearbeiten und eine Adresse angeben, die in Geo-Koordinaten umgerechnet wird.
- Es kann genau **ein Tier pro Halter** erstellt oder bearbeitet werden.
- Tierprofile enthalten Informationen wie Name, Rasse, Geburtsdatum, Geschlecht sowie Vorlieben und Abneigungen.


### Architekturübersicht

Die Architektur folgt dem Model-View-Controller (MVC)-Prinzip:

1. **Model (SQLAlchemy)**: Definiert die Datenbankmodelle.
2. **View (Jinja, HTML, Bootstrap)**: Verantwortlich für die Darstellung der Daten.
3. **Controller (Flask-Routes)**: Vermittelt zwischen Benutzereingaben und Datenbankabfragen.

---

## Fazit

Die Architektur von PetMatch ermöglicht eine **strukturierte, leicht verständliche und erweiterbare** Codebasis. Die Nutzung von Flask, SQLite und einer klaren Datenbankstruktur gewährleistet eine effiziente Speicherung und Verarbeitung von Informationen, während die API-Integration das Finden passender Spielpartner erleichtert.

Weitere Optimierungen könnten in der **Erweiterung der Matching-Logik**, einer **Echtzeit-Chatfunktion**, dem **Hochladen von Profilbildern und Bildern in den Feedbeiträgen** sowie der **Einführung einer moderierten Community** bestehen.

