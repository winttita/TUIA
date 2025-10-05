def menu():
    print("\t\tMENU\n")
    print("(E) ESTUDIANTE")
    print("(D) DOCENTE")
    print("(O) OTRO")

def valida_menu(x):
    x = x.upper()
    while x not in {'E', 'D', 'O'}:
        x = input("Valor ingresaro incorrecto. Ingrese (E, D, O): ")
        x = x.upper()
    return x

te = 0
td = 0
to = 0
cont = 0

respuesta = 'S'

while respuesta == 'S':
    cont+=1
    menu()
    tipomenu = input("\nSeleccione una de las anteriores opciones: ")
    tipomenu = valida_menu(tipomenu)
    if tipomenu == 'E':
        te+=1
    elif tipomenu == 'D':
        td+=1
    elif tipomenu == 'O':
        to+=1
    else:
        print("La opcion es incorrecta.")
    
    respuesta = input("Desea ingresar otro menu? (S/N): ")
    respuesta = respuesta.upper()
porcentaje = te/cont*100
print("La cantidad de menues de estudiantes fueron: ",te, "como asi el ", porcentaje "porciento del total de menues. ")
print("La cantidad de menues de docentes fueron: ",td)
print("La cantidad de menues de tipo otros fueron: ",to)