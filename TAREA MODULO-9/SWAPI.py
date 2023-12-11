import requests

# a) ¿En cuántas películas aparecen planetas cuyo clima sea árido?
url_planets = "https://swapi.dev/api/planets/?search=arid"
response_planets = requests.get(url_planets)
response_planets.raise_for_status()

if response_planets.status_code == 200:
    data_planets = response_planets.json()
    film_appearances = set()
    for planet in data_planets['results']:
        film_appearances.update(planet['films'])
    print(f"Los planetas con clima árido aparecen en {len(film_appearances)} películas")
else:
    print(f"Error al hacer la petición: {response_planets.status_code}")

# b) ¿Cuántos Wookies aparecen en la sexta película?
url_wookies = "https://swapi.dev/api/people/?search=Wookiee&film=3"
response_wookies = requests.get(url_wookies)
response_wookies.raise_for_status()

if response_wookies.status_code == 200:
    data_wookies = response_wookies.json()
    episode_6_wookies = len(data_wookies['results'])
    print(f"En la sexta película aparecen {episode_6_wookies} Wookiees")
else:
    print(f"Error al hacer la petición: {response_wookies.status_code}")

# c) ¿Cuál es el nombre de la aeronave más grande en toda la saga?
url_vehicles = "https://swapi.dev/api/vehicles/?page=1"
response_vehicles = requests.get(url_vehicles)
response_vehicles.raise_for_status()

if response_vehicles.status_code == 200:
    data_vehicles = response_vehicles.json()
    largest_vehicle = {"name": "", "length": 0}
    for vehicle in data_vehicles['results']:
        if vehicle['length'] != "unknown":
            vehicle_length = float(vehicle['length'])
            if vehicle_length > largest_vehicle['length']:
                largest_vehicle['name'] = vehicle['name']
                largest_vehicle['length'] = vehicle_length
    print(f"La aeronave más grande en toda la saga es el {largest_vehicle['name']} con una longitud de {largest_vehicle['length']} metros")
else:
    print(f"Error al hacer la petición: {response_vehicles.status_code}")