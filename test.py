from nicegui import ui

with ui.card() as container_a:
    ui.label("Container A")
    my_button = ui.button("Move Me!")

with ui.card() as container_b:
    ui.label("Container B")

# Move the button to container_b
ui.button("Change Place", on_click=lambda: my_button.move(container_b))

ui.run()
