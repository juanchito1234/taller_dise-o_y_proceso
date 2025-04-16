from lectorCSV import LectorCSV

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
            estudiante = inscripcion.estudiante

            if estudiante in conteo:
                conteo[estudiante] += 1
            else:
                conteo[estudiante] = 1

        print(conteo)

control = ControlInscripcion()
control.mostrar_inscripciones("data/inscripciones.csv")

        
