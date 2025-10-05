def dict_notas(alumnos: list[tuple[str, int]]) -> dict[str, int]:
    notas = {}

    for alumno in alumnos:
        nombre = alumno[0]
        nota = alumno[1]
        notas[nombre] = nota
    
    return notas