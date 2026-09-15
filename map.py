from nicegui import ui
lat=31
lon=35

def map_page(lat, lon):
    ui.leaflet(center=(lat, lon), zoom=10)

fullscreen=ui.fullscreen()
ui.run(map_page(lat, lon))