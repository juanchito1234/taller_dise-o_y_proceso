import csv
from Entidades.estudiante import Estudiante
from Entidades.materia import Materia
from Entidades.inscripcion import Inscripcion

class LectorCSV:
    def leer_inscripciones(self, ruta_archivo):
        inscripciones = []

        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for linea in lector:
                cedula_estudiante = linea[0]
                nombre_estudiante = linea[1]
                codigo_materia = linea[2]
                nombre_materia = linea[3]

                estudiante = Estudiante(cedula_estudiante, nombre_estudiante)
                materia = Materia(codigo_materia, nombre_materia)
                inscripcion = Inscripcion(estudiante, materia)

                inscripciones.append(inscripcion)

        return inscripciones
