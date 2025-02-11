---
title: Datenmodell
parent: Technische Dokumente
nav_order: 2
---


# Datenmodell PetMatch

## Tier

| Spalte         | Typ     | Beschreibung              |
|----------------|---------|---------------------------|
| Tier_id        | INTEGER | PK                        |
| Halter_id      | INTEGER | FK                        |
| Tier_name      | TEXT    | Name des Tieres           |
| Rasse          | TEXT    | Rasse des Tieres          |
| Geburtsdatum   | DATE    | Geburtsdatum              |
| Das_mag_ich    | TEXT    | Vorlieben des Tieres      |
| Das_mag_ich_nicht | TEXT | Abneigungen des Tieres    |

## Halter

| Spalte       | Typ     | Beschreibung            |
|--------------|---------|-------------------------|
| Halter_id    | INTEGER | PK                      |
| Email        | TEXT    | FK, E-Mail-Adresse des Benutzers |
| Name         | TEXT    | Name des Halters        |
| Strasse      | TEXT    | Straßennamen            |
| Hausnummer   | INTEGER | Hausnummer              |
| Stadt        | TEXT    | Stadtname               |
| PLZ          | INTEGER | Postleitzahl            |
| Breitengrad  | REAL    | Breitengrad als Dezimalzahl |
| Längengrad   | REAL    | Längengrad als Dezimalzahl |
| Radius       | INTEGER | Gewählter Radius des Nutzers (nur Deutschland, daher Ländercode raus) |

## Feedbeitrag

| Spalte      | Typ     | Beschreibung             |
|-------------|---------|--------------------------|
| Feed_id     | INTEGER | PK                       |
| Tier_id     | INTEGER | FK                       |
| Halter_id   | INTEGER | FK                       |
| Titel       | TEXT    | Titel des Beitrages      |
| Inhalt      | TEXT    | Der Inhalt des Beitrages |
| Erstellt_am | DATE    | Erstellungsdatum         |
| Erstellt_um | TIME    | Zeit der Erstellung      |


## Bild

| Spalte       | Typ     | Beschreibung                    |
|--------------|---------|---------------------------------|
| Bild_id      | INTEGER | PK                              |
| Feed_id      | INTEGER | FK zu Feedbeitrag               |
| Bild         | BLOB    | Bilddaten                       |
| Beschreibung | TEXT    | Optional: Beschreibung des Bildes |

## Benutzer (Registrierung/Anmeldung)

| Spalte         | Typ     | Beschreibung                     |
|----------------|---------|----------------------------------|
| Email          | TEXT    | PK, E-Mail-Adresse des Benutzers |
| Benutzername   | TEXT    | Benutzername                     |
| Passwort       | TEXT    | Gehashter Wert des Passworts     |
