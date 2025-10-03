list = []

while True:
    numero = int(input("Ingrese un valor para la lista, o '-1' para finalizar: "))
    if numero == -1:
        print("\nCarga finalizada.")
        break
    else:
        list.append(numero)

n = int(input("Ingrese el numero del cual quiere saber la posicion: "))

if n not in list:
    print("-1")
else:
    for i in range(len(list)):
        if list[i] == n:
            posicion = i

print(posicion)