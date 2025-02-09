from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from db import db, Benutzer, Halter, Tier, Feedbeitrag, Bild #db.py importieren
from datetime import datetime
from geoapify import get_coordinates  # Importiere die Funktion aus geoapify.py
import os
import math

app = Flask(__name__)

#statischer Session-Schlüssel
app.secret_key = 'geheimer_schluessel'

# Datenbank konfigurieren (Speicherung in instance-Ordner)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(app.instance_path, "petmatch.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Stelle sicher, dass der instance-Ordner existiert
if not os.path.exists(app.instance_path):
    os.makedirs(app.instance_path)

# Datenbank mit der App initialisieren
db.init_app(app)

# Tabellen erstellen
with app.app_context():
    db.create_all()

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Berechnet die Entfernung in Kilometern zwischen zwei Punkten,
    gegeben durch Breitengrad (lat) und Längengrad (lon),
    anhand der Haversine-Formel.
    """
    R = 6371.0  # Radius in km

    # Umwandlung von Grad in Radian
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)

    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)

    # Haversine-Formel
    a = (math.sin(d_lat / 2)**2
         + math.cos(lat1_rad)
         * math.cos(lat2_rad)
         * math.sin(d_lon / 2)**2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

# Ausloggen
@app.route('/logout', methods=['POST'])
def logout():
    """ Beendet die Sitzung und leitet zur Startseite weiter """
    session.clear()  # Löscht die Sitzung
    return redirect(url_for('index'))  # Leitet zur Startseite weiter

# Startseite
@app.route("/")
def index():
    return render_template("index.html", title="Startseite")

# Registrierung
@app.route("/registrierung", methods=['GET', 'POST'])
def registrierung():
    if request.method == 'POST':
        # Daten aus dem Formular erhalten
        email = request.form['email']
        email_wiederholen = request.form['email_wiederholen']
        benutzername = request.form['benutzername']
        passwort = request.form['passwort']

        # Überprüfen, ob die E-Mails übereinstimmen
        if email != email_wiederholen:
            return "Die E-Mail-Adressen stimmen nicht überein. Bitte versuche es erneut."

        # Benutzer in die Datenbank einfügen
        neuer_benutzer = Benutzer(email=email, benutzername=benutzername, passwort=passwort)
        try:
            db.session.add(neuer_benutzer)
            db.session.commit()
            return redirect(url_for('index'))  # Weiterleitung nach erfolgreicher Registrierung
        except Exception as e:
            db.session.rollback()
            return f"Fehler bei der Registrierung: {e}"

    return render_template("registrierung.html", title="Registrieren")

# Anmeldung
@app.route("/anmeldung", methods=['GET', 'POST'])
def anmeldung():
    if request.method == 'POST':
        email = request.form['email']
        passwort = request.form['passwort']

        # Überprüfung der Benutzeranmeldedaten
        benutzer = Benutzer.query.filter_by(email=email, passwort=passwort).first()

        if benutzer:
            session['email'] = email  # Speichere die E-Mail in der Session
            return redirect(url_for('feed'))  # Weiterleitung bei erfolgreicher Anmeldung
        else:
            return "Ungültige Anmeldedaten. Bitte versuche es erneut."

    return render_template("anmeldung.html", title="Anmelden")

# Kontakt
@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html", title="Kontakt")

# Feed
@app.route('/feed', methods=['GET', 'POST'])
def feed():
    menu_open = False  # Standardmäßig ist das Menü geschlossen

    if request.method == 'POST':
        if 'open_menu' in request.form:
            menu_open = True  # Menü öffnen
        elif 'close_menu' in request.form:
            menu_open = False  # Menü schließen
        # Bei "jetzt filtern" wird die Filterradius Funktion aktiviert
        filter_distance = None
        if 'apply_filter' in request.form:
            try:
                filter_distance = float(request.form.get('filter_radius', ''))
            except ValueError:
                filter_distance = None
    else:
        filter_distance = None

    if 'email' not in session:
        return redirect(url_for('anmeldung'))

    email = session['email']
    halter = Halter.query.filter_by(email=email).first()
    halter_existiert = halter is not None

    # Überprüfen, ob der Nutzer ein Tier hat
    tier = None
    tier_existiert = False
    if halter:
        tier = Tier.query.filter_by(halter_id=halter.halter_id).first()
        tier_existiert = tier is not None

    # Nur wenn Halter UND Tier existieren, Beiträge anzeigen
    beitraege = []
    if halter_existiert and tier_existiert:
        beitraege = db.session.query(
            Feedbeitrag.titel,
            Feedbeitrag.inhalt,
            Feedbeitrag.erstellt_am,
            Tier.tier_name.label('tier_name'),
            Tier.tier_id,  # Hier die tier_id mitgeben
            Halter.breitengrad.label('halter_lat'),
            Halter.laengengrad.label('halter_lon')
        ).join(Halter, Feedbeitrag.halter_id == Halter.halter_id) \
         .join(Tier, Feedbeitrag.tier_id == Tier.tier_id) \
         .order_by(Feedbeitrag.erstellt_am.desc()).all()
        # filtern nach Entfernung
        if filter_distance is not None and halter.breitengrad and halter.laengengrad:
            user_lat = halter.breitengrad
            user_lon = halter.laengengrad

            gefilterte_beitraege = []
            for b in beitraege:
                # Koordinaten des Erstellers
                dist = haversine_distance(user_lat, user_lon, b.halter_lat, b.halter_lon)
                if dist <= filter_distance:
                    gefilterte_beitraege.append((b, dist))

            # Sortierung nach Entfernung 
            gefilterte_beitraege.sort(key=lambda x: x[1])

            # gefilterte Beiträge anzeigen
            beitraege = [pair[0] for pair in gefilterte_beitraege]

    return render_template('feed.html', 
                           menu_open=menu_open, 
                           beitraege=beitraege, 
                           halter_existiert=halter_existiert, 
                           tier_existiert=tier_existiert, 
                           tier_id=tier.tier_id if tier else None)

@app.route("/profil_anzeigen/<int:tier_id>")
def profil_anzeigen(tier_id):
    tier = Tier.query.get(tier_id)
    if not tier:
        return "Tier nicht gefunden", 404

    return render_template("profil_anzeigen.html", title="Profil anzeigen", tier=tier)

# Route für 'Profil bearbeiten'
@app.route("/profil_bearbeiten", methods=['GET', 'POST'])
def profil_bearbeiten():
    # Überprüfen, ob der Nutzer eingeloggt ist
    if 'email' not in session:
        return redirect(url_for('anmeldung'))  # Weiterleitung zur Anmeldung, falls nicht eingeloggt

    email = session['email']  # E-Mail des Nutzers aus der Session holen

    # Daten des Halters anhand der E-Mail abrufen
    halter = Halter.query.filter_by(email=email).first()
    tier = Tier.query.filter_by(halter_id=halter.halter_id).one() if halter else None

    if request.method == 'POST':
        # Adresse zusammenbauen
        adresse = f"{request.form.get('strasse')} {request.form.get('hausnummer')}, {request.form.get('plz')} {request.form.get('stadt')}"
        
        # Geo-Koordinaten abrufen
        breitengrad, laengengrad = get_coordinates(adresse)
        
        try:
            # Sicherstellen, dass der Halter existiert oder erstellt wird
            if not halter:
                halter = Halter(
                    email=email,
                    name=request.form.get('name'),
                    strasse=request.form.get('strasse'),
                    hausnummer=request.form.get('hausnummer'),
                    plz=request.form.get('plz'),
                    stadt=request.form.get('stadt'),
                    breitengrad=breitengrad,
                    laengengrad=laengengrad
                )
                db.session.add(halter)
                db.session.commit()  # Halter speichern und ID generieren

            else:
                halter.name = request.form.get('name')
                halter.strasse = request.form.get('strasse')
                halter.hausnummer = request.form.get('hausnummer')
                halter.plz = request.form.get('plz')
                halter.stadt = request.form.get('stadt')
                halter.breitengrad = breitengrad
                halter.laengengrad = laengengrad
                db.session.commit()  # Änderungen am Halter speichern

            # Sicherstellen, dass das Tier existiert oder erstellt wird
            if not tier:
                tier = Tier(
                    halter_id=halter.halter_id,
                    tier_name=request.form.get('tier_name'),
                    rasse=request.form.get('rasse'),
                    geburtsdatum=datetime.strptime(request.form.get('geburtsdatum'), '%Y-%m-%d').date()
                    if request.form.get('geburtsdatum') else None,
                    geschlecht=request.form.get('geschlecht'),
                    das_mag_ich=request.form.get('das_mag_ich'),
                    das_mag_ich_nicht=request.form.get('das_mag_ich_nicht')
                )
                db.session.add(tier)
            else:
                tier.tier_name = request.form.get('tier_name')
                tier.rasse = request.form.get('rasse')
                tier.geburtsdatum = datetime.strptime(request.form.get('geburtsdatum'), '%Y-%m-%d').date() \
                    if request.form.get('geburtsdatum') else None
                tier.geschlecht = request.form.get('geschlecht')
                tier.das_mag_ich = request.form.get('das_mag_ich')
                tier.das_mag_ich_nicht = request.form.get('das_mag_ich_nicht')

            db.session.commit()
            return redirect(url_for('feed'))  # Erfolgreich gespeichert, zurück zum Feed

        except Exception as e:
            db.session.rollback()
            return f"Fehler beim Speichern: {e}"

    # GET-Methode: Formular anzeigen mit vorhandenen Daten
    return render_template(
        "profil_bearbeiten.html",
        title="Profil bearbeiten",
        halter=halter,
        tier=tier
    )

# Route für 'Beitrag erstellen'
@app.route("/beitraege_erstellen", methods=['GET', 'POST'])
def beitraege_erstellen():
    # Überprüfen, ob der Nutzer eingeloggt ist, sonst zur Anmeldung weiterleiten
    if 'email' not in session:
        return redirect(url_for('anmeldung'))
    
    # Email des Halters abrufen
    email = session['email']
    halter = Halter.query.filter_by(email=email).first()

    if not halter:
        return "Kein Halter gefunden. Bitte erstelle dein Profil."
    
    # Tier des Halters abrufen (jeder Halter hat genau ein Tier)
    tier = Tier.query.filter_by(halter_id=halter.halter_id).one()

    if not tier:
        return "Kein Tier gefunden. Bitte erstelle ein Profil mit einem Tier."

    if request.method == 'POST':
        # Formulardaten abrufen
        titel = request.form.get('titel')
        inhalt = request.form.get('inhalt')

        # Validierung der Eingaben
        if not titel or not inhalt:
            return "Titel und Inhalt dürfen nicht leer sein."

        try:
            # Neuen Beitrag erstellen
            neuer_beitrag = Feedbeitrag(
                tier_id=tier.tier_id,
                halter_id=halter.halter_id,
                titel=titel,
                inhalt=inhalt
            )

            # Beitrag in die Datenbank speichern
            db.session.add(neuer_beitrag)
            db.session.commit()

            # Erfolgreich gespeichert, Weiterleitung zum Feed
            return redirect(url_for('feed'))

        except Exception as e:
            db.session.rollback()
            return f"Fehler beim Speichern des Beitrags: {e}"

    # Bei GET-Anfrage das Formular anzeigen
    return render_template("beitraege_erstellen.html", title="Beitrag erstellen")

# Impressum
@app.route("/impressum")
def impressum():
    return render_template("impressum.html", title="Impressum")

# Datenschutz
@app.route("/datenschutz")
def datenschutz():
    return render_template("datenschutz.html", title="Datenschutz")

# Prüft, ob das Skript direkt ausgeführt wird (nicht importiert)
if __name__ == "__main__":
    # Erstellt alle Tabellen (falls sie noch nicht existieren)
    with app.app_context():
        db.create_all()

    # Start Flask-Anwendung im Debug-Modus, damit Änderungen ohne Neustart übernommen werden
    app.run(debug=True)
