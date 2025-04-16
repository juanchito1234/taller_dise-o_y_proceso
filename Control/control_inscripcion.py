from Control.lectorCSV import LectorCSV

class ControlInscripcion:
    def __init__(self):
        self._inscripciones = []
        self._url = ""
    
    def cargar_inscripciones(self):
        lector = LectorCSV()

        inscripciones = lector.leer_inscripciones(self._url)

        return inscripciones

    def mostrar_inscripciones(self, url):
        self._url = url

        self._inscripciones = self.cargar_inscripciones()

        conteo = {}

        for inscripcion in self._inscripciones:
            nombre_estudiante = inscripcion.get_estudiante().get_nombre()

            if nombre_estudiante in conteo:
                conteo[nombre_estudiante] += 1
            else:
                conteo[nombre_estudiante] = 1

        for nombre_estudiante in conteo:
            print(nombre_estudiante, ": ", conteo[nombre_estudiante])

        
