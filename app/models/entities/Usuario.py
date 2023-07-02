from werkzeug.security import generate_password_hash, check_password_hash


class Usuario:
    def __init__(self,id_usuario, nombre_usuario, contrasena, tipo_usuario_id):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena  = contrasena
        self.tipo_usuario_id = tipo_usuario_id

    def encrypt__password(passw):
        encriptado = generate_password_hash(passw)
        coincidencia = check_password_hash(encriptado, passw)
        return coincidencia