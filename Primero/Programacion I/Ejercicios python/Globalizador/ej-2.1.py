def IngresoDeDatos():
    """
    Esta funcion solicita al usuario que ingrese los datos presentados
    en la planilla y los devuelve en un diccionario.
    """
    soportes={}
    respuesta = 'S'
    cont = 0
    while respuesta != 'N':
        soporte = input("Ingrese un soporte: ")
        soportes[soporte] = float(input(f"ingrese el porcentaje de uso del soporte {soporte}: "))
        cont+=1
        respuesta = input("Desea ingresar otro soporte? (S/N): ")
        respuesta = respuesta.upper()
        if respuesta == 'N':
            print("\nFin de carga")
            respuesta == '*'
            break
    return soportes, cont

def soporte_mas_usado(datos):
    """
    Esta funcion recibe un diccionario conteniendo los datos ingresados
    por el usuario y devuelve una tupla con el nombre del soporte
    mas utilizado y su porcentaje de uso.
    """
    mayor_soporte = max(datos, key=datos.get)
    uso_max = datos[mayor_soporte]
    return mayor_soporte, uso_max

## Principal
datos, total = IngresoDeDatos()
soportemax, usomax = soporte_mas_usado(datos)
print("El soporte mas ultilizado es", soportemax, "con un ", usomax, "porciento de uso.")

