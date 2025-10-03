def cuenta_palabras(texto : str) -> dict[str, int]:

    conteo = {}
    palabras = texto.split()
    
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo