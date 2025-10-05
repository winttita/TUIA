def dia_siguiente(fecha: tuple[int, str, int]) -> tuple[int, str, int]:
    """
    Calcula el día siguiente a la fecha dada como (día, mes, año).
    Asume que no hay años bisiestos.
    """

    dias_por_mes = {
        'ene': 31, 'feb': 28, 'mar': 31, 'abr': 30,
        'may': 31, 'jun': 30, 'jul': 31, 'ago': 31,
        'sep': 30, 'oct': 31, 'nov': 30, 'dic': 31
    }

    orden_meses = ['ene', 'feb', 'mar', 'abr', 'may', 'jun',
                   'jul', 'ago', 'sep', 'oct', 'nov', 'dic']

    dia, mes, año = fecha

    if dia < dias_por_mes[mes]:
        dia += 1
    else:
        dia = 1
        if mes == 'dic':
            mes = 'ene'
            año += 1
        else:
            indice_mes = orden_meses.index(mes)
            mes = orden_meses[indice_mes + 1]

    return (dia, mes, año)