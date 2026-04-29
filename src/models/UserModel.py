import bcrypt
from .databaseModel import Database

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
        user = cursor.fetchone()
        conn.close()
        
        if user and bycript.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            return user
        return None
    
    def iniciar_sesion(self, usuario_data):
        conn = None
        cursor = None
        try: 
            #1. establecer conexion
            conn = self.db.get_connection()
            cursor = conn.cursor+(dictionary=True) #dictionary facilita leer por nombre de columna
            
            #2. Definir la consilta
            #IMPORTANTE: Usamos placeholders (%) para evitar la Inyeccion SQL
            query = "SELECT = FROM usuarios WHERE email = %s"
            values = (usuarios_data.email,)
            
            #3.Ejecutar y obtener resultado
            cursor.execute(query, values)
            usuario_encontrado = cursor.fetchone()
            
            #4. Logica de rentorno
            if usuario_encontrado:
                #Verificar la contraseña usando bycript
                if bycript.checkpw(usuario_data.contrseña.encode('utf-8'), usuario_encontrado['contraseña'].encode('utf-8')):
                    return True #Credenciales validas
                else:
                    return False #No se encontro el usuario o la clave no coincidio
            else:
                return False #No se encontro el usuario o la clave no coincide
            
        except Expedition as err:
            print(f"Error en la base de datos: (err)")
            return False
        finally:
            #5. Siempre crrar cursor y connexion
            if cursor: cursor.close()
            if conn.close()