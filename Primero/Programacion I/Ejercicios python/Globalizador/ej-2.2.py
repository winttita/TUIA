def ingresoDeDatos():
    notas = {}
    todaslasnotas = []

    while True:
        nombre = input("\nIngrese el nombre de un estudiante. O '0' para finalizar: ")
        if nombre == '0':
            print("Ha finalizado la carga de notas.")
            break
        notas[nombre] = int(input(f"\nIngrese la nota que obtuvo {nombre}: "))
        todaslasnotas.append(notas[nombre])
    todaslasnotas = sorted(todaslasnotas)
    return notas, todaslasnotas

def promMax(notas, todaslasnotas):
    mayoresnotas = []

    mayoresnotas.append(max(notas, key=notas.values))
    mayoresnotas.append(todaslasnotas[len(todaslasnotas)-1])
    mayoresnotas.append(todaslasnotas[len(todaslasnotas)-2])
    prom = sum(todaslasnotas)/len(todaslasnotas)
    return prom, mayoresnotas

def principal():

    listaestudiantes, notas = ingresoDeDatos()
    promedio, notasaltas = promMax(listaestudiantes, notas)
    print("El promedio de notas del primer parcial es: ", promedio)
    print(f"\nLas notas mas alta es '{notasaltas[0]} y la obtuvo el alumno '{listaestudiantes.index(notasaltas[0])}' ")
    print("\nAsi como los 3 alumnos con notas mas altas son: ")
    for i in range(3):
        print(f"\t{listaestudiantes.index(notasaltas[i])} : {notasaltas[i]}")

principal()