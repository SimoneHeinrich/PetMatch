---
title: MVP für PetMatch
nav_order: 98
---

# MVP für PetMatch

## Ziel
Die Webanwendung **PetMatch** ermöglicht es Nutzern, ihre Adresse einzugeben, diese in Geokoordinaten umzuwandeln und Beiträge im Umkreis eines definierten Radius anzuzeigen. Dabei wird ein ausgewogener Fokus auf Backend-Funktionalitäten und ein einfaches, benutzerfreundliches UI gelegt.

---

## Funktionen im MVP

### **Backend-Fokus**
1. **Benutzerregistrierung und -anmeldung**
   - Nutzer können sich registrieren und einloggen
   - Speicherung der Nutzerdaten in SQLite (z. B. E-Mail, Passwort)

2. **Geoapify-Integration**
   - **Route 1:** POST `/api/konvertierte-adresse`
     - Nimmt die Adresse des Nutzers entgegen, ruft die Geoapify-API auf und speichert die Geokoordinaten in der Datenbank
   - **Route 2:** GET `/api/feed`
     - Gibt Beiträge im Umkreis des gespeicherten Radius zurück

3. **Feed-Logik**
   - Beiträge basierend auf Längen-/Breitengraden und Radius filtern
   - Speicherung der Beiträge in SQLite

---

### **UI-Fokus**
1. **Responsives Grunddesign**
   - Einfache Navigation
   - Klare Struktur 
   

2. **Formulare**
   - Formular zur Adresseneingabe, das die Daten per POST an das Backend sendet
   - Validierung der Adressdaten im Frontend (z. B. „Pflichtfelder“)

3. **Feed-Anzeige**
   - Beiträge werden in einer übersichtlichen als Karten angezeigt (Bootstrap)
   - Radiusauswahl über ein Dropdown oder Eingabefeld

---

## Aufgabenliste

### **Backend**
- [ ] SQLite-Datenbank erstellen und Tabellen für Nutzer, Adressen und Beiträge definieren.
- [ ] Routen implementieren.
- [ ] Geoapify-Integration zur Adressumwandlung einrichten (Route: `/api/konvertierte-adresse`).
- [ ] Radius-Filter-Logik und Feed-Endpunkt implementieren (Route: `/api/feed`).

### **Frontend**
- [ ] HTML-Formulare für Registrierung, Login und Mein Profil erstellen.
- [ ] Adressformular mit POST-Request an das Backend implementieren.
- [ ] Design der Seiten erweitern (Bootstrap).

---

## Technologien
- **Backend**: Flask, SQLite, Geoapify API
- **Frontend**: HTML, CSS, Bootstrap, optional Bootswatch
- **Tools**: Git für Versionskontrolle

---

## Nicht im MVP
- Erweitertes Styling (Animationen)
- Benachrichtigungen oder komplexe Interaktionen
- Erweiterte Rollen oder Berechtigungen
- Such- oder Filterfunktionen (außer Radius)

---

## Ziel des MVP
Das MVP soll sowohl die grundlegende **Backend-Funktionalität** als auch ein gut nutzbares, ansprechendes und benutzerfreundliches **Frontend** bieten. 
