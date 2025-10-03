def correcion_tupla(precio_dolar: tuple[int, int, int, int, int]) -> tuple[int, int, int, int, int]:
    p1, p2, p3, p4, p5 = precio_dolar
    p2 = int(input(f"Ingrese el valor para actualizar el precio del dolar: "))
    precio_actualizado = p1, p2, p3, p4, p5
    return precio_actualizado
