from Control.control_inscripcion import ControlInscripcion

def main():
    # La ruta a los datos es "data/inscripciones.csv"
    ruta_csv = input("Ingrese la ruta: ")
    control = ControlInscripcion()
    control.mostrar_inscripciones(ruta_csv)

if __name__ == "__main__":
    main()