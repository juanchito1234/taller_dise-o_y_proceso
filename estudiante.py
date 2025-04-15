class Estudiante:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre

    def get_cedula(self):
        return self.cedula