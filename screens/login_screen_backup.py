import flet as ft
import time


class LoginScreen(ft.View):
    def __init__(self, auth, on_login_success, on_register_click):
        super().__init__(route="/login")
        self.auth = auth
        self.on_login_success = on_login_success
        self.on_register_click = on_register_click

        # Email field
        self.email = ft.TextField(
            label="Email",
            border_radius=15,
            bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
            border_color=ft.Colors.with_opacity(0.3, ft.Colors.WHITE),
            focused_border_color=ft.Colors.AMBER_400,
            text_size=16,
            prefix_icon=ft.Icons.EMAIL_OUTLINED,
            cursor_color=ft.Colors.AMBER_400,
            keyboard_type=ft.KeyboardType.EMAIL,
            height=55,
            color=ft.Colors.WHITE,
            label_style=ft.TextStyle(color=ft.Colors.WHITE70),
        )

        # Password field
        self.password = ft.TextField(
            label="Password",
            border_radius=15,
            bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
            border_color=ft.Colors.with_opacity(0.3, ft.Colors.WHITE),
            focused_border_color=ft.Colors.AMBER_400,
            text_size=16,
            password=True,
            can_reveal_password=True,
            prefix_icon=ft.Icons.LOCK_OUTLINED,
            cursor_color=ft.Colors.AMBER_400,
            height=55,
            color=ft.Colors.WHITE,
            label_style=ft.TextStyle(color=ft.Colors.WHITE70),
        )

        # Error/Success message
        self.status_text = ft.Text(
            color=ft.Colors.RED_300,
            size=14,
            text_align=ft.TextAlign.CENTER,
        )

        # Loading indicator
        self.loading = ft.ProgressRing(
            width=20,
            height=20,
            stroke_width=2,
            color=ft.Colors.AMBER_400,
            visible=False,
        )

        self.controls = [
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=[
                        ft.Colors.DEEP_PURPLE_900,
                        ft.Colors.PURPLE_900,
                        ft.Colors.BLUE_GREY_900,
                    ]
                ),
                content=ft.SafeArea(
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        scroll=ft.ScrollMode.HIDDEN,
                        controls=[
                            # Decorative top bar
                            ft.Container(
                                width=40,
                                height=4,
                                border_radius=2,
                                bgcolor=ft.Colors.AMBER_400,
                                margin=ft.margin.only(top=20),
                            ),

                            ft.Container(height=30),

                            # Logo Circle
                            ft.Container(
                                width=100,
                                height=100,
                                border_radius=50,
                                bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.WHITE),
                                border=ft.border.all(2, ft.Colors.AMBER_400),
                                shadow=ft.BoxShadow(
                                    spread_radius=1,
                                    blur_radius=20,
                                    color=ft.Colors.with_opacity(0.3, ft.Colors.AMBER_400),
                                ),
                                content=ft.Icon(
                                    ft.Icons.FLUTTER_DASH,
                                    size=50,
                                    color=ft.Colors.AMBER_400,
                                ),
                            ),

                            ft.Container(height=20),

                            # App Name
                            ft.Text(
                                "LUXURY",
                                size=36,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.AMBER_400,
                                letter_spacing=8,
                            ),
                            ft.Text(
                                "Elegance in Every Detail",
                                size=14,
                                color=ft.Colors.WHITE54,
                                letter_spacing=2,
                                italic=True,
                            ),

                            ft.Container(height=40),

                            # Login Card
                            ft.Container(
                                margin=ft.margin.symmetric(horizontal=25),
                                padding=ft.padding.all(30),
                                border_radius=20,
                                bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                                border=ft.border.all(1, ft.Colors.with_opacity(0.2, ft.Colors.WHITE)),
                                shadow=ft.BoxShadow(
                                    spread_radius=1,
                                    blur_radius=30,
                                    color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
                                ),
                                content=ft.Column(
                                    spacing=18,
                                    controls=[
                                        ft.Text(
                                            "Welcome Back",
                                            size=24,
                                            weight=ft.FontWeight.W_600,
                                            color=ft.Colors.WHITE,
                                        ),

                                        ft.Text(
                                            "Sign in to continue",
                                            size=14,
                                            color=ft.Colors.WHITE54,
                                        ),

                                        ft.Container(height=5),

                                        self.email,
                                        self.password,

                                        # Forgot Password
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.END,
                                            controls=[
                                                ft.TextButton(
                                                    "Forgot Password?",
                                                    style=ft.ButtonStyle(
                                                        color=ft.Colors.AMBER_300,
                                                    ),
                                                )
                                            ]
                                        ),

                                        self.status_text,

                                        # Login Button
                                        ft.Container(
                                            width=200,
                                            height=50,
                                            border_radius=25,
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    ft.Colors.AMBER_400,
                                                    ft.Colors.ORANGE_700,
                                                ]
                                            ),
                                            shadow=ft.BoxShadow(
                                                spread_radius=1,
                                                blur_radius=15,
                                                color=ft.Colors.with_opacity(0.5, ft.Colors.AMBER_400),
                                            ),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                spacing=10,
                                                controls=[
                                                    ft.TextButton(
                                                        "LOGIN",
                                                        style=ft.ButtonStyle(
                                                            color=ft.Colors.WHITE,
                                                            padding=ft.padding.all(0),
                                                        ),
                                                        on_click=self.login_clicked,
                                                    ),
                                                    self.loading,
                                                ],
                                            ),
                                        ),

                                        # Divider with text
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                            controls=[
                                                ft.Container(
                                                    width=80,
                                                    height=1,
                                                    bgcolor=ft.Colors.with_opacity(0.3, ft.Colors.WHITE),
                                                ),
                                                ft.Text(
                                                    "  OR  ",
                                                    color=ft.Colors.WHITE54,
                                                    size=12,
                                                ),
                                                ft.Container(
                                                    width=80,
                                                    height=1,
                                                    bgcolor=ft.Colors.with_opacity(0.3, ft.Colors.WHITE),
                                                ),
                                            ]
                                        ),

                                        # Register Link
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            spacing=5,
                                            controls=[
                                                ft.Text(
                                                    "Don't have an account?",
                                                    color=ft.Colors.WHITE54,
                                                    size=14,
                                                ),
                                                ft.TextButton(
                                                    "Register",
                                                    style=ft.ButtonStyle(
                                                        color=ft.Colors.AMBER_400,
                                                    ),
                                                    on_click=lambda _: self.on_register_click(),
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ),
            ),
        ]

    def login_clicked(self, e):
        # Reset status
        self.status_text.value = ""
        self.status_text.color = ft.Colors.RED_300
        self.status_text.update()

        # Validation
        if not self.email.value or not self.password.value:
            self.status_text.value = "Please fill all fields"
            self.status_text.update()
            return

        # Show loading
        self.loading.visible = True
        self.loading.update()

        # Authenticate
        time.sleep(0.5)  # Simulate network delay

        success, message, name = self.auth.login(
            self.email.value,
            self.password.value
        )

        # Hide loading
        self.loading.visible = False
        self.loading.update()

        if success:
            self.status_text.color = ft.Colors.GREEN_400
            self.status_text.value = "Login successful! 🎉"
            self.status_text.update()
            time.sleep(0.5)
            self.on_login_success(name, self.email.value)
        else:
            self.status_text.value = message
            self.status_text.update()