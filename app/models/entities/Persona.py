class Persona:

    def __init__(self, id_persona, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, telefono, correo, fecha_nacimiento=None):
        self.id_persona =id_persona
        self.primer_nombre = primer_nombre
        self.segundo_nombre = segundo_nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.telefono = telefono
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento

    def nombre_completo(self):
        return "{0}, {1}, {2}, {3}".format(self.primer_apellido, self.segundo_apellido, self.primer_nombre, self.segundo_nombre)


