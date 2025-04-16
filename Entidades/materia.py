class Materia:
    def __init__(self, codigo, nombre):
        self._codigo = codigo
        self._nombre = nombre
    
    def get_codigo(self):
        return self._codigo
    
    def get_nombre(self):
        return self._nombre