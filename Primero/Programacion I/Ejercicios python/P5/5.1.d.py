list = []
lista_a = []

while True:
    palabra = input("Ingrese un palabra para la lista, o 'f' para finalizar: ")
    palabra.lower()
    if palabra == 'f':
        print("\nCarga finalizada.")
        break
    else:
        list.append(palabra)

for i in range(len(list)):
    if list[i][0] == 'a':
        lista_a.append(list[i])

print("\n", lista_a)