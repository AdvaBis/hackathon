from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

from nicegui import app, ui

israel_cities = [
    "Jerusalem",
    "Tel Aviv-Yafo",
    "Haifa",
    "Rishon LeZion",
    "Petah Tikva",
    "Ashdod",
    "Netanya",
    "Beer Sheva",
    "Holon",
    "Bnei Brak",
    "Ramat Gan",
    "Rehovot",
    "Ashkelon",
    "Bat Yam",
    "Beit Shemesh",
    "Herzliya",
    "Kfar Sava",
    "Hadera"
]


hobbies = [
    "Dance",
    "Sing",
    "Work Out",
    "Sleep",
    "Read",
    "Gaming",
    "Cook",
    "Bake",
]

# in reality users passwords would obviously need to be hashed
passwords = {'user1': 'pass1', 'user2': 'pass2'}

# top-level static routes like /favicon.ico must be unrestricted, otherwise the middleware redirects them to /login
unrestricted_page_routes = {'/favicon.ico', '/login', '/signup'}


@app.add_middleware
class AuthMiddleware(BaseHTTPMiddleware):
    """This middleware restricts access to all NiceGUI pages.

    It redirects the user to the login page if they are not authenticated.
    """

    async def dispatch(self, request: Request, call_next):
        path = request.url.path
        if app.storage.user.get('authenticated') or path in unrestricted_page_routes or path.startswith('/_nicegui'):
            return await call_next(request)
        return RedirectResponse(f'/login?redirect_to={path}')


@ui.page('/')
def main_page() -> None:
    def logout() -> None:
        app.storage.user.clear()
        ui.navigate.to('/login')

    with ui.column().classes('absolute-center items-center'):
        ui.label(f'Hello {app.storage.user["username"]}!').classes('text-2xl')
        ui.button(on_click=logout, icon='logout').props('outline round')


@ui.page('/login')
def login(redirect_to: str = '/') -> RedirectResponse | None:
    if app.storage.user.get('authenticated'):
        return RedirectResponse('/')


    def try_login() -> None:
        if passwords.get(username.value) == password.value:
            app.storage.user.update(username=username.value, authenticated=True)
            ui.navigate.to(redirect_to)  # go back to where the user wanted to go
        else:
            ui.notify('Wrong username or password', color='negative')


    with ui.card().classes('absolute-center items-stretch'):
        username = ui.input('Username').props('autofocus').on('keydown.enter', lambda: password.run_method('focus'))
        password = ui.input('Password', password=True, password_toggle_button=True).on('keydown.enter', try_login)
        ui.button('Log in', on_click=try_login)
        ui.link('dont have an account? sign up', '/signup').classes('mt-4 text-sm self-center')


    return None

from nicegui import ui






@ui.page('/signup')
def signup_page():
    # def handle_signup():
    #         return ui.label(f'Account created for {username.value}!', color='positive')

    with ui.card().classes('absolute-center p-6 w-80'):
        ui.label('Create Account').classes('text-2xl font-bold mb-4')

        username = ui.input('Username').classes('w-full mb-2')
        email = ui.input('Email').classes('w-full mb-2')
        ui.label('City')
        city = ui.select(israel_cities)
        password = ui.input('Password', password=True, password_toggle_button=True).classes('w-full mb-2')
        confirm_password = ui.input('Confirm Password', password=True, password_toggle_button=True).classes(
            'w-full mb-4')
        ui.label('Hobbie')
        hobby = ui.select(hobbies)

        # passwords['Username'] = password

        ui.button('Sign Up').classes('w-full bg-primary text-white')
        ui.link('Already have an account? Log in', '/login').classes('mt-4 text-sm self-center')


if __name__ in {'__main__', '__mp_main__'}:
    ui.run(storage_secret='THIS_NEEDS_TO_BE_CHANGED')
