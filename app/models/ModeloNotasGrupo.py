from .entities.Persona import Persona
from .entities.Estudiante import Estudiante
from .entities.Docente import Docente
from .entities.Nota import Nota
from .entities.Grupo import Grupo
from .entities.GrupoEstudiante import GrupoEstudiante
from .entities.Modulo import Modulo
from flask_mysqldb import MySQL

class ModeloNotasGrupo:


    @classmethod
    def listar_estudiantes(self, db, id_docente=1, nombre_grupo='Grupo 2 - Docente Uno'):
        try:
            cursor=db.connection.cursor()
            sql=f"""SELECT e.Código, p.Primer_Apellido, p.Segundo_Apellido, p.Primer_Nombre, p.Segundo_Nombre, p.Teléfono, p.Correo, n1.Puntaje AS Simple, n2.Puntaje AS Winters, n3.Puntaje AS Arma, (n1.Puntaje + n2.Puntaje + n3.Puntaje) / 3 AS Promedio FROM estudiante e JOIN grupo_estudiante ge ON e.ID_Estudiante = ge.ID_Estudiante JOIN persona p ON e.ID_Persona = p.ID_Persona JOIN nota n1 ON e.ID_Estudiante = n1.ID_Estudiante AND n1.ID_Módulo = 1 JOIN nota n2 ON e.ID_Estudiante = n2.ID_Estudiante AND n2.ID_Módulo = 2 JOIN nota n3 ON e.ID_Estudiante = n3.ID_Estudiante AND n3.ID_Módulo = 3 JOIN módulo m ON n1.ID_Módulo = m.ID_Módulo JOIN grupo g ON ge.ID_Grupo = g.ID_Grupo JOIN docente d ON g.ID_Docente = d.ID_Docente WHERE d.ID_Docente = ( SELECT ID_Docente FROM docente WHERE ID_Docente = {id_docente} ) AND g.Nombre_Grupo = '{nombre_grupo}';"""
            cursor.execute(sql)
            data = cursor.fetchall()    
            print(data)
            print('Datos Arriba')
            #   data = {
            #    "estudiante": data
            #}
            Estudiantes=[]
            for row in data:
                print(row)
                print('ROW arriba')
                estudiante = Persona(0,row[3],row[4],row[1], row[2], row[5], row[6])
                estudianteCod = Estudiante(0,0,estudiante,row[0])
                notaSimple = Nota(0,estudiante,1,row[7])
                notaWinters = Nota(0,estudiante,1,row[8])
                notaARMA = Nota(0,estudiante,1,row[9])
                notas=[notaSimple,notaWinters,notaARMA]
                promedio = row[10]
                Estudiantes.append([estudianteCod,estudiante, notas, promedio])
            print("DESPUES DE FOR Y LLENADO ED LA LISTA")
            return Estudiantes
        except Exception as ex:
            raise Exception(ex)