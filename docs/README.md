# **PetMatch**

Dieses Repository enthält den Quellcode und die Dokumentation für **PetMatch**, eine Webanwendung zur Vernetzung von Tierhaltern in der Umgebung. Die App ermöglicht es Nutzern, passende Spielgefährten für ihre Haustiere zu finden, indem Beiträge basierend auf Standortdaten gefiltert werden.

---

## **Schritte zur Ausführung der Anwendung**

### **Schritt 1: Repository klonen**
Zuerst muss das Repository lokal geklont werden. Öffnen Sie ein Terminal und führen Sie folgenden Befehl aus:

```bash
git clone https://github.com/SimoneHeinrich/PetMatch.git
cd PetMatch
```

---

### **Schritt 2: Virtuelle Python-Umgebung einrichten**
Bevor Sie Abhängigkeiten installieren, richten Sie eine virtuelle Umgebung ein und aktivieren Sie diese:

```bash
python -m venv env
source env/bin/activate  # Für macOS/Linux
env\Scripts\activate     # Für Windows
```

---

### **Schritt 3: Erforderliche Pakete installieren**
Installieren Sie alle benötigten Abhängigkeiten mit:

```bash
pip install -r requirements.txt
```

Falls Flask nicht installiert ist, führen Sie zusätzlich aus:

```bash
pip install flask
```

Überprüfen Sie, ob Flask erfolgreich installiert wurde:

```bash
pip list | findstr flask  # Windows
pip list | grep flask     # macOS/Linux
```

---

### **Schritt 4: Anwendung starten**
Starten Sie die Anwendung: 

```bash
flask run
```

---

### **Schritt 5: Anwendung öffnen**
Nach dem Start kann die Anwendung im Browser aufgerufen werden unter:

```
http://127.0.0.1:5000/
```

---

## **Registrierung und Anmeldung**

### **Option 1: Eigene Registrierung**
1. Rufen Sie die Registrierungsseite auf:
   ```
   http://127.0.0.1:5000/registrierung
   ```
2. Füllen Sie das Registrierungsformular aus:
   - E-Mail-Adresse (zweimal eingeben)
   - Benutzername wählen
   - Passwort setzen
   - Datenschutzerklärung bestätigen (Checkbox setzen)
   - Auf **"Registrieren"** klicken
3. Nach erfolgreicher Registrierung erfolgt eine Weiterleitung zur Anmeldeseite:
   ```
   http://127.0.0.1:5000/anmeldung
   ```
4. Melden Sie sich anschließend mit Ihrer E-Mail und Ihrem Passwort an.

---

### **Option 2: Nutzung eines Testaccounts**
Falls keine Registrierung erfolgen soll, kann folgender Testaccount verwendet werden:

- **E-Mail:** `Admin1999@web.de`
- **Passwort:** `Admin3`

Damit kann sich direkt eingeloggt werden unter:
```
http://127.0.0.1:5000/anmeldung
```

---

## **Repository-Inhalt**

- **Quellcode der Anwendung:** Implementiert mit Flask, SQLite und Bootstrap.  
- **Technische Dokumentation:** Detaillierte Architektur, Designentscheidungen und Setup-Anleitungen.  
- **Entwicklungshistorie:** Die Entwicklungsschritte lassen sich anhand der Commit-Historie im Repository nachvollziehen.  

---

## **Technologie-Stack**

- **Backend:** Flask (Python)  
- **Frontend:** Bootstrap, HTML, Jinja  
- **Datenbank:** SQLite (SQLAlchemy ORM)  
- **API-Integration:** Geoapify für Geolokalisierungsdienste  

---

## **Dokumentation**

Die vollständige technische Dokumentation finden Sie unter folgendem Link:  
[PetMatch Dokumentation](https://simoneheinrich.github.io/PetMatch/)

**Inhalt der Dokumentation:**  

### **Projektstruktur und Teamreflexion**
- Design Entscheidung  
- Team Beurteilung (mit Unterkategorien)  
- Technische Dokumente (mit Unterkategorien)   
- Persona  
- Nutzerbewertung  
- MVP für PetMatch  
- Präsentation  
- Figma Prototyp  

---

## **Projektstatus**

### **Implementierte Funktionen**
- Benutzer-Authentifizierung (Registrierung & Login)  
- Profil- und Tierverwaltung  
- Beitragserstellung  
- Anzeigen der Beiträge im Feed  
- Standortbasierter Feed mit Radius-Filterung  

### **Mögliche erweiternde Features**
- Upload von Profilbildern  
- Upload von Beitragsbildern  
- Direkte Nachrichten zwischen Nutzern  

---

## **Mitwirkende**

- **Simone Heinrich** – Matrikelnummer: 77211956881  
- **Patryk Kujawski** – Matrikelnummer: 77211961546  

---

## **Lizenz**  

Dieses Projekt wurde für den Kurs an der HWR Berlin entwickelt und steht unter der **MIT License**.  
Die **MIT-Lizenz** erlaubt es, den Code frei zu verwenden, zu verändern und zu verbreiten, solange ein Hinweis auf die ursprünglichen Autoren erhalten bleibt.  

Die vollständige Lizenz finden Sie in der Datei [`LICENSE.txt`](LICENSE.txt).