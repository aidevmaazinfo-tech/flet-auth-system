import flet as ft
from auth import Auth
from screens.login_screen import LoginScreen
from screens.register_screen import RegisterScreen
from screens.welcome_screen import WelcomeScreen


def main(page: ft.Page):
    page.title = "Luxury App"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 450
    page.window.height = 850
    page.window_resizable = True
    page.padding = 0
    page.bgcolor = "#1a002a"

    auth = Auth()

    def show_login():
        page.views.clear()
        page.views.append(
            LoginScreen(auth, show_welcome, show_register)
        )
        page.go("/login")

    def show_register():
        page.views.clear()
        page.views.append(
            RegisterScreen(auth, show_welcome, show_login)
        )
        page.go("/register")

    def show_welcome(name, email):
        page.views.clear()
        page.views.append(
            WelcomeScreen(name, email, show_login)
        )
        page.go("/welcome")

    show_login()


ft.app(target=main)