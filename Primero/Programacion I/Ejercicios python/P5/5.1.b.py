list = []

while True:
    numero = int(input("Ingrese un valor para la lista, o '-1' para finalizar: "))
    if numero == -1:
        print("\nCarga finalizada.")
        break
    else:
        list.append(numero)

for i in range(len(list)):
    if i == 0:
        mayor = list[0]
        menor = list[0]
    elif list[i] > mayor:
        mayor = list[i]
    elif list[i] < menor:
        menor = list[i]

print("\nEl mayor numero es: ", mayor) 
