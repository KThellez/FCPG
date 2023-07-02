from werkzeug.security import check_password_hash
from .entities.Usuario import Usuario
from .entities.TipoUsuario  import TipoUsuario

class ModeloUsuario():

    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = "select ID_Usuario, Nombre_Usuario, Contraseña, tipo_usuario_id from usuario WHERE Nombre_Usuario = '{0}'".format(usuario.nombre_usuario)
            cursor.execute(sql)
            data=cursor.fetchone()
            if data is not None :
                coincidencia =check_password_hash(data[2],usuario.contrasena)
                if coincidencia:
                    usuario_logado = Usuario(data[0], data[1], None, None)
                    return usuario_logado
                else:
                    return None

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def obtener_por_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "select usu.ID_Usuario, usu.Nombre_Usuario, tipu.id, tipu.tipo from usuario usu join tipo_usuario tipu on usu.tipo_usuario_id = tipu.id WHERE usu.ID_Usuario = {0}".format(id)
            cursor.execute(sql)
            data=cursor.fetchone()
            tipusuario = TipoUsuario(data[2],data[3])
            usuario_logeado=Usuario(data[0], data[1], None, tipusuario)
            return usuario_logeado
        except Exception as ex:
            raise Exception(ex)
