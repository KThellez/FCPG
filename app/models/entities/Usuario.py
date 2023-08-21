from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Usuario(UserMixin):
    def __init__(self,id_usuario, nombre_usuario, contrasena, tipo_usuario_id):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena  = contrasena
        self.tipo_usuario_id = tipo_usuario_id
    
    
    @classmethod
    def verify__password(self, encriptado, passw):
        return check_password_hash(encriptado, passw)
    
    def get_id(self):
        return str(self.id_usuario)