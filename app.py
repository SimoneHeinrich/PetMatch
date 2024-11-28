# Importiere die Flask-Klasse aus dem Flask-Modul
from flask import Flask

# Erstelle eine Instanz der Flask-Klasse, die die Webanwendung repräsentiert
app = Flask(__name__)

# Dekoriere die Funktion `home` mit der Route `/`, die die Startseite der Anwendung definiert
@app.route("/")
def home():
    # Diese Funktion wird ausgeführt, wenn jemand die Startseite besucht
    return "Hello, PetMatch!"  # Der Rückgabewert wird als HTTP-Response gesendet

# Prüfe, ob das Skript direkt ausgeführt wird (nicht importiert)
if __name__ == "__main__":
    # Starte die Flask-Anwendung im Debug-Modus, damit Änderungen ohne Neustart übernommen werden
    app.run(debug=True)
