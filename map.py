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


def find_pos(latitude,longitude):
    m= ui.leaflet(center=(latitude,longitude))
    marker = m.marker(latlng=(latitude,longitude))

def map_run():
    find_pos(latitude,longitude)