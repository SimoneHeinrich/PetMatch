from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Flask-App 
app = Flask(__name__)

# SQLite-Datenbank konfigurieren
# Pfad zur Datenbank, da wo Verzeichnis von db.py
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(base_dir, "petmatch.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Vermeidet unnötige Warnungen

# SQLAlchemy 
db = SQLAlchemy(app)

# Tabellen definieren
class Benutzer(db.Model):
    email = db.Column(db.String, primary_key=True)
    benutzername = db.Column(db.String, nullable=False)
    passwort = db.Column(db.String, nullable=False)

class Halter(db.Model):
    halter_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, db.ForeignKey('benutzer.email'), nullable=False)
    name = db.Column(db.String, nullable=False)
    strasse = db.Column(db.String)
    hausnummer = db.Column(db.Integer)
    stadt = db.Column(db.String)
    plz = db.Column(db.Integer)
    breitengrad = db.Column(db.Float)
    laengengrad = db.Column(db.Float)
    radius = db.Column(db.Integer)

class Tier(db.Model):
    tier_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    halter_id = db.Column(db.Integer, db.ForeignKey('halter.halter_id'), nullable=False)
    tier_name = db.Column(db.String, nullable=False)
    rasse = db.Column(db.String, nullable=False)
    geburtsdatum = db.Column(db.Date)
    das_mag_ich = db.Column(db.String)
    das_mag_ich_nicht = db.Column(db.String)

class Feedbeitrag(db.Model):
    feed_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tier_id = db.Column(db.Integer, db.ForeignKey('tier.tier_id'), nullable=False)
    halter_id = db.Column(db.Integer, db.ForeignKey('halter.halter_id'), nullable=False)
    titel = db.Column(db.String, nullable=False)
    inhalt = db.Column(db.String, nullable=False)
    erstellt_am = db.Column(db.Date, default=db.func.current_date())
    erstellt_um = db.Column(db.Time, default=db.func.current_time())

class Bild(db.Model):
    bild_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    feed_id = db.Column(db.Integer, db.ForeignKey('feedbeitrag.feed_id'), nullable=False)
    bild = db.Column(db.LargeBinary)
    beschreibung = db.Column(db.String)

# Datenbanktabellen erstellen
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Erstellt alle Tabellen, falls sie noch nicht existieren
        print("Datenbank erfolgreich erstellt!")