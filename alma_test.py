from datetime import datetime
from nicegui import ui
from nicegui import ui
from geopy.geocoders import Nominatim
from uuid import uuid4
from html_sanitizer import Sanitizer
from langchain_openai import ChatOpenAI




OPENAI_API_KEY = 'not-set'
#map
def find_cord(city):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(str(city))
    cord=(location.latitude,location.longitude)
    return cord

def find_pos(latitude,longitude):
    m= ui.leaflet(center=(latitude,longitude))
    marker = m.marker(latlng=(latitude,longitude))
#
#
#
def main_map():
    lat = 31
    lon = 35
    city = "Tel Aviv"
    cord = find_cord(city)
    latitude = cord[0]
    longitude = cord[1]
    find_pos(latitude, longitude)




label = ui.label()
ui.timer(1.0, lambda: label.set_text(f'{datetime.now():%X}'))
with ui.tabs().classes('w-full') as tabs:
    one = ui.tab('Map')
    two = ui.tab('Chat')
    tree=ui.tab('chat bot')
with ui.tab_panels(tabs, value=two).classes('w-full'):
    with ui.tab_panel(one):
        ui.link_target(main_map())
    with ui.tab_panel(two):
        ui.label('agam akziza')
    with ui.tab_panel(tree):
        ui.label('alma')
ui.run()














