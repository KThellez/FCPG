from .entities.Persona import Persona
from .entities.Docente import Docente
from .entities.Nota import Nota
from .entities.Grupo import Grupo
from flask_mysqldb import MySQL

class ModeloListarDocentes:


    @classmethod
    def listar_docentes(self, db):
        try:
            cursor=db.connection.cursor()
            sql=f"""SELECT d.ID_Docente, p.Primer_Nombre, p.Primer_Apellido, g.ID_Grupo, g.Nombre_Grupo FROM docente d JOIN persona p ON d.ID_Persona = p.ID_Persona JOIN grupo g ON d.ID_Docente = g.ID_Docente;"""
            cursor.execute(sql)
            data = cursor.fetchall()    
            print(data)
            print('Datos Arriba')
            Docentes=[]
            for row in data:
                print(row)
                print('ROW arriba')
                docente = Docente(row[0],None,None)
                print('DOC arriba')
                estudiante = Persona(0, row[1], None, row[2], None, 0, None)
                print('est arriba')
                grupo = Grupo(row[3], row[4], docente, None)
                print('gru arriba')

                Docentes.append([docente,estudiante, grupo])
            print("DESPUES DE FOR Y LLENADO ED LA LISTA")
            return Docentes
        except Exception as ex:
            raise Exception(ex)