def promedios(alumnos: dict[str,list[int]]) -> None:
    promedios = []
    sumador = 0
    contador = 0

    for alumno, notas in alumnos.items():
        sumador = sum(notas)
        promedio = sumador / len(notas)
        promedios.append(promedio)
        print(f"El promedio de {alumno} es {promedio: .2f}")

#prueba

alumnos = {"Juan": [6,9,8], "Manuel": [9,10,9], "Martin": [5,6,7]}
promedios(alumnos)