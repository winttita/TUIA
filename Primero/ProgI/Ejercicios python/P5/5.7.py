# representacion del tiempo --> (horas, minutos, segundos)
def suma_horas(t1: tuple[int, int, int], t2: tuple[int, int, int]) ->tuple[int, int, int]:
    """
    CALCULA LA SUMA DE DOS TIEMPOS QUE SON PASADOS COMO ARGUMENTOS. SE GUARDA LA SUMA EN UNA NUEVA TUPLA DE LA MISMA DISPOSICION.
    """    
    segundos = t1(2) + t2(2)
    minutos = t1(1) + t2(1) + segundos // 60
    horas = t1(0) + t2(0) + minutos //60

    segundos = segundos % 60
    minutos = minutos % 60

    return (horas, minutos, segundos)