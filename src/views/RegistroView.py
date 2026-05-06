import flet as ft

def RegistroView(page: ft.Page, auth_controller):
    nombre_input = ft.TextField(label="Nombre", width = 350, border_radius=10)
    apellido_input = ft.TextField(label="Apellido", width = 350, border_radius=10)    
    email_input = ft.TextField(label="Correo Electronico", width = 350, border_radius=10)
    pass_input = ft.TextField(label="Constraseña", password=True, can_reveal_password=True, width=350, border_radius=10)
    def login_click(e):
        
        def registrarse_click(e):
        if not email_input.value or not pass_input.value or not nombre_input.value or not apellido_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, llene todos los campos"))
            page.snack_bar.open = True
            page.update()
            return
        
         `id_usuario` int(11) NOT NULL,
    `nombre` varchar(100) DEFAULT NULL,
    `apellido` varchar(100) DEFAULT NULL,
    `email` varchar(150) DEFAULT NULL,
    `password` varchar(255) DEFAULT NULL,
    `telefono` varchar(20) NOT NULL,
    `activo` tinyint(1) NOT NULL,
    `foto_perfil` varchar(255) NOT NULL

        if user:
            page.user_data = user
            page.go("/")
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()
                        
    registrarse_button = ft.ElevatedButton("Crear cuenta", on_click=registrarse_click, width=350, bgcolor="cyan", color = "black", icon=(ft.Icon(ft.Icons.CHECK, color=ft.Colors.WHITE, size=25)))
    volver_button = ft.ElevatedButton("¿Ya tienes una cuenta?", on_click=lambda _: page.go("/"), width=350, bgcolor="green", color = "black", icon=(ft.Icon(ft.Icons.LOGIN, color=ft.Colors.WHITE, size=25)))
    
    pass_input.on_submit = registrarse_click
        
    
    return ft.View(
        route = "/registrarse",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(title=ft.Text("REGISTRO :)"), bgcolor="cyan", color= "white"),
        controls=[
            ft.Column(
                [
                    ft.Text("Registrate", size=24, weight="bold"),
                    nombre_input,
                    apellido_input,
                    email_input,
                    pass_input,
                    registrarse_button,
                    volver_button,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=20
            )
        ]
    )