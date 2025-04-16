import csv
import os
from Entidades.estudiante import Estudiante
from Entidades.materia import Materia
from Entidades.inscripcion import Inscripcion

class LectorCSV:
    def leer_inscripciones(self, ruta_archivo):
        if not isinstance(ruta_archivo, str):
            raise ValueError("La ruta del archivo debe ser una cadena")

        if not ruta_archivo.endswith('.csv'):
            raise ValueError("El archivo debe tener extensión .csv")

        if not os.path.exists(ruta_archivo):
            raise ValueError("El archivo no existe")

        inscripciones = []

        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for i, linea in enumerate(lector, start=1):
                if len(linea) != 4:
                    raise ValueError(f"Línea mal formada en la fila {i}: {linea}")
                
                cedula_estudiante = linea[0].strip()
                nombre_estudiante = linea[1].strip()
                codigo_materia = linea[2].strip()
                nombre_materia = linea[3].strip()

                estudiante = Estudiante(cedula_estudiante, nombre_estudiante)
                materia = Materia(codigo_materia, nombre_materia)
                inscripcion = Inscripcion(estudiante, materia)

                inscripciones.append(inscripcion)

        return inscripciones
