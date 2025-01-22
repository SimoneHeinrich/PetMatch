# **PetMatch**

PetMatch ist eine innovative App-Idee, die Tierhalter in ihrer Umgebung miteinander verbindet, um den Austausch zu fördern und gemeinsame Aktivitäten zu organisieren. Mit einem radiusbasierten Feed, der auf Adress- und GPS-Daten basiert, bietet die App eine Plattform für gezielte Interaktion und Unterstützung.

---

## **Inhaltsverzeichnis**
- [Beschreibung](#beschreibung)
- [Features](#features)
- [Technologien](#technologien)
- [Dokumentation](#dokumentation)
- [Installation](#installation)
- [Status des Projekts](#status-des-projekts)
- [Mitwirkende](#mitwirkende)

---

## **Beschreibung**
**Ziel:**  
PetMatch wurde konzipiert, um Tierbesitzern eine Plattform zu bieten, auf der sie Erfahrungen teilen, Tipps austauschen und Treffen oder Aktivitäten organisieren können.

**Zielgruppe:**  
- Tierhalter (z. B. Hundebesitzer, Katzenfreunde, Pferdeliebhaber).  

**Wertversprechen:**  
- Lokale Vernetzung für Tierhalter.  
- Austausch von relevanten Informationen wie Pflegehinweisen, Tierarztempfehlungen oder Auslaufmöglichkeiten.  
- Unterstützung bei der Organisation von Treffen mit anderen Tierhaltern.

---

## **Features**
- **Benutzerprofile:** Nutzer können Profile für ihre Tiere und sich anlegen einschließlich Adressdaten.  
- **Radiusbasierter Feed:** Beiträge werden basierend auf der geografischen Nähe gefiltert und angezeigt.  
- **Multi-Tier-Verwaltung:** Ein Nutzer kann mehrere Tiere registrieren und verwalten.  
- **Geodaten-Integration:** Adressdaten werden in GPS-Daten umgewandelt und in der Datenbank gespeichert.  
- **Flexible Feed-Anpassung:** Der Radius für die Beitragsanzeige kann individuell angepasst werden.  

---

## **Technologien**
- **Frontend:** Geplant mit Flask und HTML/CSS.  
- **Backend:** SQLite und Python.  
- **Datenbank:** SQLite zur Verwaltung von Benutzer- und Beitragsdaten.  
- **API:** Adress-zu-GPS-Daten-Umwandlung durch eine externe Geocoding-API (z. B. OpenCage).  
- **Versionierung:** GitHub wird für die Versionskontrolle genutzt.  

---

## **Dokumentation**
Die gesamte Dokumentation ist unter folgendem Link verfügbar:  
> [PetMatch Dokumentation] https://simoneheinrich.github.io/PetMatch/

**Enthält:**  
- Starseite
- Team-Beurteilung
- Technische Dokumentation  
- Personas
- Nutzerbewertung 

---

## **Installation**
1. **Repository klonen:**  
   ```bash
   git clone https://github.com/studSH/PetMatch.git

2. **virtuelle Umgebung einrichten**
     ```bash
    python -m venv env
    source env/bin/activate  # Für macOS/Linux
    env\Scripts\activate     # Für Windows

3. **Abhängigkeiten installieren:**
     ```bash
    pip install -r requirements.txt
4. **Projekt starten**
     ```bash
    python app.py


## **Status des Projekts**
Aktuell befindet sich das Projekt noch in der Konzeptionsphase. Der Fokus lag bisher auf der Erstellung des Datenmodells, der UI-Designs und der Dokumentation/der Pages.  
Es wurde noch kein Code implementiert, da dies im Rahmen der Aufgabenstellung nicht erforderlich war.

---

## **Mitwirkende**
- **Simone Heinrich** (Matr.-Nr.: 77211956881)  
- **Patryk Kujawski** (Matr.-Nr.: 77211961546)

