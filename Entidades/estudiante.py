class Estudiante:
    def __init__(self, cedula, nombre):
        self._cedula = cedula
        self._nombre = nombre

    def get_cedula(self):
        return self._cedula
    
    def get_nombre(self):
        return self._nombre