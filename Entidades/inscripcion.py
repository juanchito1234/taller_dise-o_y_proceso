class Inscripcion:
    def __init__(self, estudiante, materia):
        self._estudiante = estudiante
        self._materia = materia 

    def get_estudiante(self):
        return self._estudiante
    
    def get_materia(self):
        return self._materia