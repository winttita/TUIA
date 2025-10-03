fibonacci = [0, 1]

n = int(input("Ingrese la cantidad de elementos de la Serie de Fibonacci que desea conocer: "))

for i in range(n):
    if i == 0 or i == 1:
        continue
    else:
        fibonacci.append(fibonacci[i-2]+fibonacci[i-1])

print(f"\nLos {n} primeros numeros de la Serie de Fibonacci son: ", fibonacci)