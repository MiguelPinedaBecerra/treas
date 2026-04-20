import flet as ft
from controllers.UserController import AuthController
from controllers.TareaController import TareaController
from views.loginView import LoginView
from views.dashboard import DashboardView

def start(page: ft.Page):
    #Configuracion inicial de la pagina
    page.tile = "Sistema SIGE"
    page.window_width = 450
    page.window_height = 700
    
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
        
    def view_pop(e):
            if len(page.views) > 1:
                page.views.pop()
                top_view = page.view[-1]
                page.go(top_view.route)
        
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
def main():
    ft.app(target=start)
    
if __name__ == "__main__":
    main()