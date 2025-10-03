def dict_notas(alumnos: list[tuple[str, int]]) -> dict[int, str]:
    notas = {}

    for alumno in alumnos:
        nombre = alumno[0]
        nota = alumno[1]
        notas[nota] = nombre
    
    return notas