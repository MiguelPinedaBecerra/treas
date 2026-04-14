import bycript
from .database import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()

    def registrar(self, usuario_data):
        #Encriptar contraseña
        salt = bycript.gensalt()
        hashed_pw = bycript.hashpw(usuario_data.password.encode('utf-8'),salt)
        
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)",
                (usuario_data.nombre, usuario_data.email, hashed_pw.decode('utf-8'))

            )
            conn.commit()
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    def validar_login(self, email, password):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        usuario = cursor.fetchone()
        conn.close()
        
        if usuario and bycript.checkpw(password.encode('utf-8'), usuario['password'].encode('utf-8')):
            return usuario
        return None