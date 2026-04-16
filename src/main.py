import flet as ft
from controllers.UserController import AuthController
from controllers.TareaController import TareaController
from views.loginView import LoginView
from views.dashboard import DashboardView

def start(page: ft.Page):
    auth_ctrl = AuthController()
    task_ctrl = TareaController()
    
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            
            page.views.append(LoginView(page, task_ctrl))
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
            
        if not page.views:
            page.views.append(
                ft.view("/", [ft.Text("Error: Ruta no encontrada o vista vacia")])
            )
        page.update()
        
    page.on_route_change = route_change
    page.go("/")
    
def main():
    ft.app(target=start)
    
if __name__ == "__main__":
    main()