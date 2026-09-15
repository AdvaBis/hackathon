from nicegui import ui

def root():
    ui.sub_pages({
        '/': table_page,
        '/map/{lat}/{lon}': map_page,
    }).classes('w-full')

def table_page():
    ui.table(rows=[
        {'name': 'Israel', 'lat': 31, 'lon': 35}
    ]).props('flat bordered') \
        .on('row-click', lambda e: ui.navigate.to(f'/map/{e.args[1]["lat"]}/{e.args[1]["lon"]}'))

def map_page(lat: float, lon: float):
    ui.leaflet(center=(lat, lon), zoom=10)
    ui.link('Back to table', '/')

ui.run(root)