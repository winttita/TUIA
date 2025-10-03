list = []
lista_mas_1 = []

while True:
    numero = int(input("Ingrese un valor para la lista, o '-1' para finalizar: "))
    if numero == -1:
        print("\nCarga finalizada.")
        break
    else:
        list.append(numero)

for i in range(len(list)):
    lista_mas_1.append(list[i]+1)

print(lista_mas_1)