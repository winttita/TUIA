list = []
sumapar = 0
productoimpar = 1

while True:
    numero = int(input("Ingrese un valor para la lista, o '-1' para finalizar: "))
    if numero == -1:
        print("\nCarga finalizada.")
        break
    else:
        list.append(numero)
hay_impar = False
for i in list:
    if i % 2 == 0:
        sumapar += list[i]
    else:
        productoimpar *= list[i]
        hay_impar = True
if not hay_impar:
    productoimpar = 0

print(f"\nLa suma de los numeros pares es {sumapar} y el producto de impares es {productoimpar}.")

