
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from db import db, Benutzer, Halter, Tier, Feedbeitrag, Bild #db.py importieren
from datetime import datetime
from geoapify import get_coordinates  # Importiere die Funktion aus geoapify.py
import os


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

@app.route('/feed', methods=['GET', 'POST'])
def feed():
    menu_open = False
    if request.method == 'POST':
        # Wenn der Benutzer auf das Bild klickt, Menü öffnen
        if 'open_menu' in request.form:
            menu_open = True
        # Wenn der Benutzer "Menü schließen" klickt, Menü schließen
        elif 'close_menu' in request.form:
            menu_open = False
    return render_template('feed.html', menu_open=menu_open)


# Route für 'Profil anzeigen'
@app.route("/profil_anzeigen")
def profil_anzeigen():
    # Logik hinzufügen, um Benutzerdaten zu laden
    return render_template("profil_anzeigen.html", title="Profil anzeigen")

# Route für 'Profil bearbeiten'
@app.route("/profil_bearbeiten", methods=['GET', 'POST'])
def profil_bearbeiten():
    # Überprüfen, ob der Nutzer eingeloggt ist
    if 'email' not in session:
        return redirect(url_for('anmeldung'))  # Weiterleitung zur Anmeldung, falls nicht eingeloggt

    email = session['email']  # E-Mail des Nutzers aus der Session holen

    # Daten des Halters anhand der E-Mail abrufen
    halter = Halter.query.filter_by(email=email).first()
    tier = Tier.query.filter_by(halter_id=halter.halter_id).first() if halter else None

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
                    das_mag_ich=request.form.get('das_mag_ich'),
                    das_mag_ich_nicht=request.form.get('das_mag_ich_nicht')
                )
                db.session.add(tier)
            else:
                tier.tier_name = request.form.get('tier_name')
                tier.rasse = request.form.get('rasse')
                tier.geburtsdatum = datetime.strptime(request.form.get('geburtsdatum'), '%Y-%m-%d').date() \
                    if request.form.get('geburtsdatum') else None
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
@app.route("/beitraege_erstellen")
def beitraege_erstellen():
    # Logik hinzufügen, um die Beitragsseite zu rendern
    return render_template("beitraege_erstellen.html", title="Beitrag erstellen")

# Impressum
@app.route("/impressum")
def impressum():
    return render_template("impressum.html", title="Impressum")

# Datenschutz
@app.route("/datenschutz")
def datenschutz():
    return render_template("datenschutz.html", title="Datenschutz")

# Prüfe, ob das Skript direkt ausgeführt wird (nicht importiert)
if __name__ == "__main__":
    # Erstellt alle Tabellen (falls sie noch nicht existieren)
    with app.app_context():
        db.create_all()

    # Start Flask-Anwendung im Debug-Modus, damit Änderungen ohne Neustart übernommen werden
    app.run(debug=True)