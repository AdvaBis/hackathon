from nicegui import ui
from geopy.geocoders import Nominatim

def find_cord(city):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(str(city))
    cord=(location.latitude,location.longitude)
    return cord

def find_pos(latitude,longitude):
    global pos_list
    m= ui.leaflet(center=(latitude,longitude))
    marker = m.marker(latlng=(latitude,longitude))
    pos_list.append(marker)

def main():
    pos_list = []
    lat = 31
    lon = 35
    city = "Tel Aviv"
    cord = find_cord(city)
    latitude = cord[0]
    longitude = cord[1]
    ui.run(find_pos(latitude,longitude))
main()