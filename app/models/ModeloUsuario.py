from werkzeug.security import check_password_hash
from .entities.Usuario import Usuario

class ModeloUsuario():

    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = "select ID_Usuario, Nombre_Usuario, Contraseña, tipo_usuario_id from usuario = {0}".format(usuario.nombre_usuario)
            cursor.execute(sql)
            data=cursor.fetchone()
            coincidencia =check_password_hash(data[2],usuario.contrasena)
            if coincidencia:
                usuario_logado = Usuario(data[0], data[1], None, None)
                return usuario_logado
            else:
                return None

        except Exception as ex:
            raise Exception(ex)