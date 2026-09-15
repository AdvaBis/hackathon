from nicegui import ui
from geopy.geocoders import Nominatim

lat=31
lon=35
city="Tel Aviv"


def find_cord(city):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(str(city))
    cord=(location.latitude,location.longitude)
    return cord


cord=find_cord(city)
latitude=cord[0]
longitude=cord[1]

def map_page(lat=latitude, lon=longitude):
    ui.leaflet(center=(lat, lon), zoom=10)

ui.run(map_page())