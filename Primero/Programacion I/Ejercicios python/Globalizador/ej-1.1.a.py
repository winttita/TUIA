def menu():
    print("\t\tMENU\n")
    print("(E) ESTUDIANTE")
    print("(D) DOCENTE")
    print("(O) OTRO")

te = 0
td = 0
to = 0

menu()
for i in range(150):
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


