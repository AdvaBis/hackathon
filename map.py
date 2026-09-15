from nicegui import ui

def map_page(lat=31, lon=35):
    ui.leaflet(center=(lat, lon), zoom=10)
    return None

fullscreen=ui.fullscreen()
ui.run(map_page())