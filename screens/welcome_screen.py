import flet as ft
import threading
import time


class WelcomeScreen(ft.View):
    def __init__(self, name, email, on_logout):
        super().__init__(route="/welcome")
        self.user_name = name
        self.user_email = email
        self.on_logout = on_logout
        initials = ''.join([n[0].upper() for n in name.split()[:2]]) if name else "U"

        self.menu_open = False

        # Welcome Text
        self.welcome_text = ft.Text(
            "", size=16, color="#d4af37", text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.W_300, opacity=0,
            animate_opacity=ft.Animation(800, ft.AnimationCurve.EASE_OUT)
        )

        # Name Text
        self.name_text = ft.Text(
            "", size=36, weight=ft.FontWeight.W_900, color="#ffffff",
            text_align=ft.TextAlign.CENTER, opacity=0,
            animate_opacity=ft.Animation(1000, ft.AnimationCurve.EASE_OUT)
        )

        # Subtitle
        self.subtitle = ft.Text(
            "", size=13, color="#888888", text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.W_300, opacity=0,
            animate_opacity=ft.Animation(800, ft.AnimationCurve.EASE_OUT)
        )

        # Avatar
        self.avatar = ft.Container(
            width=85, height=85, border_radius=42, bgcolor="#1c1c1c",
            alignment=ft.Alignment(x=0, y=0),
            border=ft.Border(
                left=ft.BorderSide(2, "#d4af37"),
                top=ft.BorderSide(2, "#d4af37"),
                right=ft.BorderSide(2, "#d4af37"),
                bottom=ft.BorderSide(2, "#d4af37")
            ),
            content=ft.Text(initials, size=32, weight=ft.FontWeight.BOLD, color="#d4af37", text_align=ft.TextAlign.CENTER),
            opacity=0, animate_opacity=ft.Animation(1000, ft.AnimationCurve.EASE_OUT)
        )

        # Hamburger Menu Button
        self.menu_button = ft.IconButton(
            icon=ft.Icons.MENU if hasattr(ft.Icons, 'MENU') else ft.Icons.LIST,
            icon_color="#d4af37",
            icon_size=24,
            bgcolor="#1c1c1c",
            on_click=self.toggle_menu,
        )

        # Menu Panel
        self.menu_panel = ft.Container(
            visible=False,
            width=180,
            bgcolor="#151515",
            border=ft.Border(
                left=ft.BorderSide(1, "#333333"),
                top=ft.BorderSide(1, "#333333"),
                right=ft.BorderSide(1, "#333333"),
                bottom=ft.BorderSide(1, "#333333")
            ),
            border_radius=12,
            padding=ft.Padding(left=0, top=8, right=0, bottom=8),
            content=ft.Column(
                spacing=0,
                controls=[
                    self._menu_item("👤  Profile", self.on_profile_click),
                    self._menu_item("⚙️  Settings", self.on_settings_click),
                    self._menu_item("❓  Help", self.on_help_click),
                    ft.Container(height=4),
                    ft.Container(height=1, bgcolor="#333333"),
                    ft.Container(height=4),
                    self._menu_item("🚪  Logout", self.on_logout_click, is_logout=True),
                ],
            ),
        )

        # Feature Cards
        features = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
            controls=[
                self._build_card("⚡", "Premium", "Top Quality"),
                self._build_card("🔒", "Secure", "Bank Level"),
                self._build_card("💎", "Exclusive", "VIP Access"),
            ],
        )

        # Profile Card
        profile_card = ft.Container(
            padding=ft.Padding(left=20, top=12, right=20, bottom=12),
            border_radius=12,
            bgcolor="#151515",
            border=ft.Border(
                left=ft.BorderSide(1, "#333333"),
                top=ft.BorderSide(1, "#333333"),
                right=ft.BorderSide(1, "#333333"),
                bottom=ft.BorderSide(1, "#333333")
            ),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("◆", size=14, color="#d4af37"),
                    ft.Container(width=8),
                    ft.Text(self.user_email, color="#888888", size=13),
                ],
            ),
        )

        # Stats Row
        stats_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            controls=[
                self._build_stat("128", "Orders"),
                self._build_stat("12", "Rewards"),
                self._build_stat("VIP", "Status"),
            ],
        )

        # Header
        header = ft.Container(
            padding=ft.Padding(left=0, top=5, right=0, bottom=0),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("NEXUS", size=20, weight=ft.FontWeight.W_900, color="#d4af37"),
                    self.menu_button,
                ],
            ),
        )

        # Menu Overlay
        self.menu_overlay = ft.Container(
            visible=False,
            alignment=ft.Alignment(x=1, y=-1),
            padding=ft.Padding(left=0, top=50, right=25, bottom=0),
            content=self.menu_panel,
        )

        self.controls = [
            ft.Container(
                expand=True,
                bgcolor="#0d0d0d",
                padding=ft.Padding(left=25, top=20, right=25, bottom=20),
                content=ft.Column(
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        # Stack for Header + Menu
                        ft.Stack(
                            controls=[
                                header,
                                self.menu_overlay,
                            ],
                        ),

                        ft.Container(height=30),

                        # Main Content
                        ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Container(width=40, height=3, border_radius=1, bgcolor="#d4af37"),
                                ft.Container(height=25),
                                self.welcome_text,
                                ft.Container(height=8),
                                self.name_text,
                                ft.Container(height=5),
                                self.subtitle,
                                ft.Container(height=30),
                                self.avatar,
                                ft.Container(height=25),
                                stats_row,
                                ft.Container(height=25),
                                profile_card,
                                ft.Container(height=25),
                                features,
                                ft.Container(height=40),
                            ],
                        ),
                    ],
                ),
            ),
        ]

    def _build_card(self, emoji, title, subtitle):
        return ft.Container(
            width=95,
            height=95,
            border_radius=12,
            bgcolor="#151515",
            alignment=ft.Alignment(x=0, y=0),
            border=ft.Border(
                left=ft.BorderSide(1, "#333333"),
                top=ft.BorderSide(1, "#333333"),
                right=ft.BorderSide(1, "#333333"),
                bottom=ft.BorderSide(1, "#333333")
            ),
            padding=ft.Padding(left=8, top=8, right=8, bottom=8),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=4,
                controls=[
                    ft.Text(emoji, size=22, text_align=ft.TextAlign.CENTER),
                    ft.Text(title, size=12, weight=ft.FontWeight.W_600, color="#ffffff", text_align=ft.TextAlign.CENTER),
                    ft.Text(subtitle, size=9, color="#888888", text_align=ft.TextAlign.CENTER),
                ],
            ),
        )

    def _build_stat(self, value, label):
        return ft.Container(
            padding=ft.Padding(left=15, top=10, right=15, bottom=10),
            border_radius=10,
            bgcolor="#151515",
            border=ft.Border(
                left=ft.BorderSide(1, "#333333"),
                top=ft.BorderSide(1, "#333333"),
                right=ft.BorderSide(1, "#333333"),
                bottom=ft.BorderSide(1, "#333333")
            ),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=2,
                controls=[
                    ft.Text(value, size=20, weight=ft.FontWeight.W_700, color="#d4af37", text_align=ft.TextAlign.CENTER),
                    ft.Text(label, size=10, color="#888888", text_align=ft.TextAlign.CENTER),
                ],
            ),
        )

    def _menu_item(self, label, on_click, is_logout=False):
        """Menu item - Fixed for Flet 0.86.5"""
        color = "#ff4444" if is_logout else "#ffffff"
        return ft.TextButton(
            content=ft.Text(label, size=14, color=color, weight=ft.FontWeight.W_500),
            on_click=on_click,
            style=ft.ButtonStyle(
                padding=ft.Padding(left=16, top=12, right=16, bottom=12),
                bgcolor=ft.Colors.TRANSPARENT if hasattr(ft.Colors, 'TRANSPARENT') else "#00000000",
            ),
        )

    def toggle_menu(self, e):
        self.menu_open = not self.menu_open
        self.menu_panel.visible = self.menu_open
        self.menu_overlay.visible = self.menu_open
        self.menu_overlay.update()
        self.menu_panel.update()

    def on_profile_click(self, e):
        self._close_menu()

    def on_settings_click(self, e):
        self._close_menu()

    def on_help_click(self, e):
        self._close_menu()

    def on_logout_click(self, e):
        self._close_menu()
        self.on_logout()

    def _close_menu(self):
        self.menu_open = False
        self.menu_panel.visible = False
        self.menu_overlay.visible = False
        self.menu_overlay.update()
        self.menu_panel.update()

    def did_mount(self):
        def animate():
            time.sleep(0.3)
            self.welcome_text.value = "WELCOME"
            self.welcome_text.opacity = 1
            self.welcome_text.update()

            time.sleep(0.3)
            self.name_text.value = self.user_name
            self.name_text.opacity = 1
            self.name_text.update()

            time.sleep(0.2)
            self.subtitle.value = "Enjoy your premium experience"
            self.subtitle.opacity = 1
            self.subtitle.update()

            time.sleep(0.3)
            self.avatar.opacity = 1
            self.avatar.update()

        threading.Thread(target=animate, daemon=True).start()