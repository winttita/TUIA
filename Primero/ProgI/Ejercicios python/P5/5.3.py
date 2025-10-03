lista = []
vistos = []
duplicados = []

#---------- metodo 1 ----------
while True:
    numero = int(input("Ingrese un valor para la lista, o '-1' para finalizar: "))
    if numero == -1:
        print("\nCarga finalizada.")
        break
    else:
        lista.append(numero)

for num in lista:
    if num in vistos:
        duplicados.append(num)
    else:
        vistos.append(num)

print("Los numeros duplicados son: ", duplicados)

#---------- metodo 2 ----------
while True:
    numero = int(input("Ingrese un valor para la lista, o '-1' para finalizar: "))
    if numero == -1:
        print("\nCarga finalizada.")
        break
    else:
        lista.append(numero)

for i in range(len(lista)):
    if lista[i] in lista[i+1:] and lista[i] not in duplicados:
        duplicados.append(lista[i])

if duplicados:
    print("\nElementos repetidos: ", duplicados)
else:
    print("\nNo hay elementos repetidos.")