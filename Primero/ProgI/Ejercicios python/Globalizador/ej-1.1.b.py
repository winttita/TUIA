def menu():
    print("\t\tMENU\n")
    print("(E) ESTUDIANTE")
    print("(D) DOCENTE")
    print("(O) OTRO")

te = 0
td = 0
to = 0

cant = input("Ingrese la cantidad de menues que desea clasificar: ")

menu()
for i in range(cant):
    tipomenu = input("Seleccione una de las anteriores opciones.")
    tipomenu = tipomenu.upper()
    if tipomenu == 'E':
        te+=1
    elif tipomenu == 'D':
        td+=1
    elif tipomenu == 'O':
        to+=1
    else:
        print("La opcion es incorrecta.")

print("La cantidad de menues de estudiantes fueron: ",te)
print("La cantidad de menues de docentes fueron: ",td)
print("La cantidad de menues de tipo otros fueron: ",to)

