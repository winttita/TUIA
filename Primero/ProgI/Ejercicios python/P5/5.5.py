def ingreso_datos() -> list[list[str | int]]:
    basedatos = []

    while True:
        datos_personales = []
        nombre = input("Ingrese el nombre del alumno o '0' para finalizar: ")
        if nombre == '0':
            print("\nCarga de datos finalizada.")
            break
        apellido = input(f"\nIngrese el apellido del alumno {nombre} : ")
        localidad = input(f"\nIngrese la localidad del alumno {nombre} : ")
        edad = int(input(f"\nIngrese la edad del alumno {nombre} : "))
        dni = int(input(f"\nIngrese el dni del alumno {nombre} : "))
        carrera = input(f"\nIngrese la carrera que estudia : ")
        inicio_carrera = int(input(f"\nIngrese el año de ingreso a la carrera {carrera} : "))

        datos_personales.append(nombre)
        datos_personales.append(apellido)
        datos_personales.append(localidad)
        datos_personales.append(edad)
        datos_personales.append(dni)
        datos_personales.append(carrera)
        datos_personales.append(inicio_carrera)
        basedatos.append(datos_personales)
    return basedatos

def cantidad_años_cursados(lista_datos: list[any]) -> list[str]:

    años_cursados = 2025 - lista_datos[6]
    lista_datos.append(años_cursados)
    print(años_cursados)
    
    return lista_datos
