import unittest
from Control.control_inscripcion import ControlInscripcion

class TestControlInscripcion(unittest.TestCase):
    # se harán pruebas con el método mostrar_inscripciones()
    def test_mostrar_inscripciones(self):
        control = ControlInscripcion()
        url = "data/tests/inscripciones_test.csv"
        resultado = control.mostrar_inscripciones(url)

        self.assertEqual(resultado, "Juan Perez : 1\nAna Gómez : 1\n")

    def test_archivo_vacio(self):
        control = ControlInscripcion()
        url = "data/tests/vacio.csv"
        resultado = control.mostrar_inscripciones(url)

        self.assertEqual(resultado, "No hay inscripciones registradas.")

    def test_archivo_con_formato_incorrecto(self):
        control = ControlInscripcion()
        url = "data/tests/mal_formado.csv"

        with self.assertRaises(ValueError):
            control.mostrar_inscripciones(url)

    def test_tipo_url(self):
        control = ControlInscripcion()
        url = 123
        
        with self.assertRaises(ValueError):
            control.mostrar_inscripciones(url)
