list = []
lista_al_revez = []

while True:
    numero = input("Ingrese un valor para la lista, o 'f' para finalizar: ")
    numero = numero.lower()
    if numero == 'f':
        print("\nCarga finalizada.")
        break
    else:
        list.append(int(numero))

lista_al_revez = list[::-1]
print(lista_al_revez)