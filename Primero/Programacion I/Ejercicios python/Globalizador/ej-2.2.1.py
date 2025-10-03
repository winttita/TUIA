def ingresoDeDatos() -> list:
    """
    Esta función solicita al usuario que ingrese los datos presentados
    en la planilla y devuelve una lista de tuplas, donde la primera
    componente es el nombre del estudiante y la segunda componente es
    la nota que obtuvo en el parcial.
    """
    notas = []
    print("Ingrese los datos del parcial (nombre y nota). Escriba '0' para terminar.\n")

    while True:
        nombre = input("Nombre del estudiante: ")
        if nombre.strip() == '0':
            print("Finalizando carga de datos...\n")
            break
        try:
            nota = int(input("Nota del estudiante (0 a 10): "))
            if 0 <= nota <= 10:
                notas.append((nombre.strip(), nota))
            else:
                print("La nota debe estar entre 0 y 10. Intente nuevamente.\n")
        except ValueError:
            print("Entrada inválida. La nota debe ser un número entero.\n")

    return notas


def promMax(listaNotas: list) -> tuple:
    """
    Esta función recibe una lista de tuplas donde la primera componente
    es el nombre del estudiante y la segunda componente es la nota
    del estudiante en el parcial, y devuelve la nota promedio del
    curso y la nota más alta del curso también.
    """
    if not listaNotas:
        return 0, 0

    suma = sum(nota for _, nota in listaNotas)
    prom = suma / len(listaNotas)
    notaMaxima = max(nota for _, nota in listaNotas)

    return prom, notaMaxima


def principal() -> None:
    """
    Este es el programa principal.
    """
    listaEstudiantes = ingresoDeDatos()
    if not listaEstudiantes:
        print("No se ingresaron datos.")
        return

    promedio, notaMasAlta = promMax(listaEstudiantes)
    print(f"\nEl promedio de notas del parcial es: {promedio:.2f}")
    print(f"La nota más alta obtenida fue: {notaMasAlta}")
    print("Estudiante(s) con la nota más alta:")

    for nombre, nota in listaEstudiantes:
        if nota == notaMasAlta:
            print(f"\t{nombre}")


# Ejecutar el programa
principal()
