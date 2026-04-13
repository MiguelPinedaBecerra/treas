import flet as ft

def loginView(page, auth_controller):
    email_input = ft.TextField(label="Correo electronico", width=350, border_radius=10)
    pass_imput = ft.TextField(label="Contraseña", password=True, width=350, border_radius=10)
    
    def login_click(e):
        user, msg = auth_controller.login(email_input.value, pass_imput.value)
        if user:
            page.session.set("user, user")
            page.go("/dashboard")
        else:
            page.snack.bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()
            
        return ft.View("/", [
            ft.AppBar(tittle=ft.Text("SIGE - login"), bgcolor=ft.Colors.BLUE_GREY_900, color="white"),
            ft.Colunm([
                ft.Icon(ft.Icons.LOCK_PERSON, size=50, color=ft.Colors.BLUE),
                ft.Text("Acceso al sistema", size=24, weigth="bold"),
                email_input,
                pass_input,
                ft.ElevateButton("Entrar", on_click=login_click, width=350),
                ft.TextButton("Crear una cuenta nueva", on_click=lambda _: page.go("/registro"))
            ], horizontal_alignment0ft.CrossAxisAlignment.CENTER, alignment=ft.NainAxisAlignment.CENTER)
        ])