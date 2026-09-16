from datetime import datetime
from nicegui import ui
label = ui.label()
ui.timer(1.0, lambda: label.set_text(f'{datetime.now():%X}'))



with ui.tabs().classes('w-full') as tabs:
    one = ui.tab('One')
    two = ui.tab('Two')
with ui.tab_panels(tabs, value=two).classes('w-full'):
    with ui.tab_panel(one):
        ui.label('First tab')
    with ui.tab_panel(two):
        ui.label('Second tab')




ui.run()