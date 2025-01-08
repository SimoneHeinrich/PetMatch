# https://www.geoapify.com/get-started-with-maps-api/
# https://www.geoapify.com/tutorial/geocoding-python/
# https://myprojects.geoapify.com/api/jZTxsYj7RGTTV2f8Xa2b/keys
import requests

GEOAPIFY_API_KEY = "ef346015db9d4eb889b31e901f27d0f8"  

def get_coordinates(address):
    """
    Holt die Koordinaten (Breitengrad, Längengrad) für eine gegebene Adresse.
    """
    url = "https://api.geoapify.com/v1/geocode/search"
    params = {
        "text": address,
        "apiKey": GEOAPIFY_API_KEY
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Fehler anzeigen, falls HTTP-Fehler auftreten
        data = response.json()
        
        if data['features']:
            coords = data['features'][0]['geometry']['coordinates']
            return coords[1], coords[0]  # Rückgabe: Breitengrad, Längengrad
        else:
            return None, None  # Keine Koordinaten gefunden
    except requests.exceptions.RequestException as e:
        print("Fehler beim Abrufen der Geo-Daten:", e)
        return None, None
