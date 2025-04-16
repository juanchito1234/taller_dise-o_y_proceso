import unittest
from Control.lectorCSV import LectorCSV

class TestLectorCSV(unittest.TestCase):

    def test_leer_inscripciones_correctas(self):
        lector = LectorCSV()
        ruta_archivo = "data/tests/inscripciones_test.csv"
        inscripciones = lector.leer_inscripciones(ruta_archivo)
        self.assertEqual(len(inscripciones), 2)

        self.assertEqual(inscripciones[0].get_estudiante().get_cedula(), "12345")
        self.assertEqual(inscripciones[0].get_estudiante().get_nombre(), "Juan Perez")
        self.assertEqual(inscripciones[0].get_materia().get_codigo(), "101")
        self.assertEqual(inscripciones[0].get_materia().get_nombre(), "Matemáticas")

        self.assertEqual(inscripciones[1].get_estudiante().get_cedula(), "67890")
        self.assertEqual(inscripciones[1].get_estudiante().get_nombre(), "Ana Gómez")
        self.assertEqual(inscripciones[1].get_materia().get_codigo(), "202")
        self.assertEqual(inscripciones[1].get_materia().get_nombre(), "Inglés")
    
    def test_archivo_no_existente(self):
        lector = LectorCSV()
        ruta_archivo = "data/tests/no_existe.csv"
        with self.assertRaises(ValueError):
            lector.leer_inscripciones(ruta_archivo)

    def test_archivo_no_csv(self):
        lector = LectorCSV()
        ruta_archivo = "data/tests/archivo_no_csv.txt"
        with self.assertRaises(ValueError):
            lector.leer_inscripciones(ruta_archivo)

    def test_csv_vacio(self):
        lector = LectorCSV()
        ruta_archivo = "data/tests/vacio.csv"
        inscripciones = lector.leer_inscripciones(ruta_archivo)
        self.assertEqual(inscripciones, [])

    def test_linea_mal_formada(self):
        lector = LectorCSV()
        ruta_archivo = "data/tests/mal_formado.csv"
        with self.assertRaises(ValueError):
            lector.leer_inscripciones(ruta_archivo)

    def test_ruta_no_es_string(self):
        lector = LectorCSV()
        ruta_archivo = 123
        with self.assertRaises(ValueError):
            lector.leer_inscripciones(ruta_archivo)

if __name__ == '__main__':
    unittest.main()
