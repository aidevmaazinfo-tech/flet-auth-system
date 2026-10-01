import flet as ft
import time


class RegisterScreen(ft.View):
    def __init__(self, auth, on_register_success, on_login_click):
        super().__init__(route="/register")
        self.auth = auth
        self.on_register_success = on_register_success
        self.on_login_click = on_login_click

        # Field style same as login
        field_style = {
            "border_radius": 12,
            "bgcolor": "#1c1c1c",
            "border_color": "#c9a84c",
            "focused_border_color": "#d4af37",
            "height": 50,
            "color": "#ffffff",
            "cursor_color": "#d4af37",
            "text_size": 14,
            "label_style": ft.TextStyle(color="#999999"),
        }

        self.name = ft.TextField(label="Full Name", **field_style)
        self.email = ft.TextField(label="Email", **field_style)
        self.password = ft.TextField(label="Password", password=True, can_reveal_password=True, **field_style)
        self.confirm_password = ft.TextField(label="Confirm Password", password=True, can_reveal_password=True, **field_style)

        self.status_text = ft.Text(color="#ff4444", size=13, text_align=ft.TextAlign.CENTER)
        self.loading = ft.ProgressRing(width=20, height=20, color="#d4af37", visible=False)

        self.controls = [
            ft.Container(
                expand=True,
                bgcolor="#0d0d0d",
                alignment=ft.Alignment(x=0, y=0),
                padding=ft.Padding(left=25, top=20, right=25, bottom=20),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        # Back Button - Left aligned
                        ft.Container(
                            alignment=ft.Alignment(x=-1, y=0),
                            content=ft.TextButton(
                                "← Back",
                                on_click=lambda _: self.on_login_click(),
                                style=ft.ButtonStyle(color="#d4af37"),
                            ),
                        ),

                        ft.Container(height=10),

                        # Logo
                        ft.Container(
                            width=70,
                            height=70,
                            border_radius=35,
                            bgcolor="#1c1c1c",
                            alignment=ft.Alignment(x=0, y=0),
                            border=ft.Border(
                                left=ft.BorderSide(2, "#d4af37"),
                                top=ft.BorderSide(2, "#d4af37"),
                                right=ft.BorderSide(2, "#d4af37"),
                                bottom=ft.BorderSide(2, "#d4af37")
                            ),
                            content=ft.Text("◆", size=30, color="#d4af37", text_align=ft.TextAlign.CENTER),
                        ),

                        ft.Container(height=15),

                        # Brand
                        ft.Text("NEXUS", size=32, weight=ft.FontWeight.W_900, color="#d4af37", text_align=ft.TextAlign.CENTER),
                        ft.Text("Create Account", size=12, color="#888888", weight=ft.FontWeight.W_300, text_align=ft.TextAlign.CENTER),

                        ft.Container(height=30),

                        # Register Card
                        ft.Container(
                            padding=ft.Padding(left=25, top=25, right=25, bottom=25),
                            border_radius=14,
                            bgcolor="#151515",
                            border=ft.Border(
                                left=ft.BorderSide(1, "#333333"),
                                top=ft.BorderSide(1, "#333333"),
                                right=ft.BorderSide(1, "#333333"),
                                bottom=ft.BorderSide(1, "#333333")
                            ),
                            content=ft.Column(
                                spacing=14,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text("Join Nexus", size=20, weight=ft.FontWeight.W_600, color="#ffffff", text_align=ft.TextAlign.CENTER),
                                    ft.Text("Fill in the details below", size=13, color="#999999", text_align=ft.TextAlign.CENTER),

                                    self.name,
                                    self.email,
                                    self.password,
                                    self.confirm_password,

                                    ft.Container(
                                        alignment=ft.Alignment(x=0, y=0),
                                        content=self.status_text,
                                    ),

                                    ft.Container(height=5),

                                    # Register Button
                                    ft.Container(
                                        alignment=ft.Alignment(x=0, y=0),
                                        content=ft.Container(
                                            width=220,
                                            height=48,
                                            border_radius=12,
                                            alignment=ft.Alignment(x=0, y=0),
                                            gradient=ft.LinearGradient(
                                                begin=ft.Alignment(x=-1, y=0),
                                                end=ft.Alignment(x=1, y=0),
                                                colors=["#c9a84c", "#d4af37"]
                                            ),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    ft.TextButton(
                                                        "CREATE ACCOUNT",
                                                        on_click=self.register_clicked,
                                                        style=ft.ButtonStyle(color="#000000"),
                                                    ),
                                                    self.loading,
                                                ],
                                            ),
                                        ),
                                    ),

                                    ft.Container(height=5),

                                    # Login Link
                                    ft.Container(
                                        alignment=ft.Alignment(x=0, y=0),
                                        content=ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                            controls=[
                                                ft.Text("Already have an account? ", color="#888888", size=13, text_align=ft.TextAlign.CENTER),
                                                ft.TextButton(
                                                    "Sign In",
                                                    on_click=lambda _: self.on_login_click(),
                                                    style=ft.ButtonStyle(color="#d4af37"),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ),
        ]

    def register_clicked(self, e):
        self.status_text.value = ""
        self.status_text.color = "#ff4444"
        self.status_text.update()
        if not self.name.value or not self.email.value or not self.password.value:
            self.status_text.value = "Please fill all fields"
            self.status_text.update()
            return
        if self.password.value != self.confirm_password.value:
            self.status_text.value = "Passwords do not match"
            self.status_text.update()
            return
        if len(self.password.value) < 4:
            self.status_text.value = "Password must be at least 4 characters"
            self.status_text.update()
            return
        self.loading.visible = True
        self.loading.update()
        time.sleep(0.5)
        success, message = self.auth.register(self.name.value, self.email.value, self.password.value)
        self.loading.visible = False
        self.loading.update()
        if success:
            self.status_text.color = "#4caf50"
            self.status_text.value = "Account created successfully! ✨"
            self.status_text.update()
            time.sleep(0.8)
            self.on_register_success(self.name.value, self.email.value)
        else:
            self.status_text.value = message
            self.status_text.update()