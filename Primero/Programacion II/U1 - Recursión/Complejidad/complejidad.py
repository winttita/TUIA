## Ejercicio 0 #############################################################

def condicional0(num: int) -> int:
    if num > 10:
        print(f"{num} es mayor que 10")
        aux = num % 2
    else:
        print(f"{num} es menor que 10")
        aux = num // 2

    return aux

    # La complejidad del algoritmo es O(1)(constante) ya que el numero de pasos que el algoritmo
    # ejecuta, no cambia dependiendo del valor de entrada. La cantidad de operaciones es igual
    # n = 5, que para n = 10000.

## Ejercicio 1 #############################################################
def condicional1(num: int) -> int:
    if num > 10:
        print(f"{num} es mayor que 10")
        aux = num % 2
        if aux == 0:
            print(f"{num} es divisible por 2")
        else:
            print(f"{num} no es divisible por 2")
            aux = num * num * num
    else:
        print(f"{num} es menor que 10")
        aux = num // 2
        producto = num * 2
        if producto % 3 == 0:
            print("producto es divisible por 3")
    return aux

    # Este algoritmo tiene complejidad O(1), ya que el numero de operaciones que el algoritmo realiza
    # no varia segun el valor de entrada.

## Ejercicio 2 #############################################################
def ciclo0(n: int) -> None:
    lista = list(range(n))
    m = n // 2
    for i in range(0, n):
        print("inicio ciclo j")
        for j in range(m):
            print("inicio ciclo k")
            for k in range(0, 3):
                print(lista[k])
    
    # l42 n asignaciones a i.
    # l44 m asignaciones a j. m = n // 2.
    # l46 3 asignaciones a k.
    # La complejidad del algorito es (n * (n // 2) * 3) = 3/2 * n² -> O(n²)

## Ejercicio 3 #############################################################
def ciclo1(n: int) -> None:
    lista = list(range(n))
    m = n % 2
    for i in range(0, n):
        print("inicio ciclo j")
        for j in range(m):
            print("inicio ciclo k")
            for k in range(0, 3):
                print(lista[k])

    # l58 n asignaciones a i.
    # l60 m = n % 2 asignaciones a j, que en este caso pueden ser 0 o 1, asi que tomamos
    # el peor de los casos, 1 asignacion a j.
    # l62 3 asignaciones a k.
    # La complejidad de este algoritmo es (n * 1 * 3) = n -> O(n)

## Ejercicio 4 #############################################################
def ciclo2(n: int, m: int) -> None:
    lista = [1, 2, 3, 4]
    for i in range(0, n):
        print("inicio ciclo j")
        for j in range(0, m):
            print("inicio ciclo k")
            for k in range(0, 3):
                print(lista[k])

    # l74 n asignaciones a i.
    # l76 m asignaciones a j.
    # l78 3 asignaciones a k.
    # Este algoritmo tiene complejidad igual a 3*m*n -> O(mn)

## Ejercicio 5 #############################################################
def ciclo3(n: int, m: int, b: bool) -> None:
    for i in range(0, n):
        if b:
            print("inicio ciclo j")
            for j in range(0, m):
                print(n + j)
        else:
            print("inicio ciclo k")
            for k in range(1000):
                print(n)
    
    # l88 n asignaciones a i.
        # b = true # l91 m asignaciones a j
        # b = false # l95 1000 asignaciones a k.
    # En este algoritmo nos encontramos con dos posibles complejidades, O(mn) y O(n).

## Ejercicio 6 #############################################################
def ciclo4(n: int) -> None:
    if n > 10:
        print("Tabla de multiplicar")
        for i in range(1, 11):
            print(i, n * i)
    else:
        print(n // 2, n * 2)
    
    # n > 10 # 10 asignaciones a i. O(1)
    # n < 10 # O(1)
    # La complejidad de este algorito es constante.

## Ejercicio 7 #############################################################
def ciclo5() -> None:
    numero = int(input("Ingrese un valor"))
    lista = []
    while numero != 0 and len(lista) < 10000:
        lista.append(numero)
        numero = int(input("Ingrese un valor"))
    for i in range(len(lista)):
        print(lista[i])

    # l118 se asigna una entrada a num.
    # l120 vemos que como MAXIMO numero cambiaria de valor 9999.
    # l123 9999 asignaciones a i a lo sumo.
    # Complejidad de valor constante O(1), ya que el numero de operaciones no varia.

## Ejercicio 8 #############################################################
def mezcla_de_listas(L1: list[int], L2: list[int]) -> list[int]:
    # precond: L1 y L2 estan ordenadas
    i, j = 0, 0
    L3 = []
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L3.append(L1[i])
            i += 1
        else:
            L3.append(L2[j])
            j += 1
    if i == len(L1):
        for k in range(j, len(L2)):
            L3.append(L2[k])
    else:
        for k in range(i, len(L1)):
            L3.append(L1[k])
    return L3

    # l136 a lo sumo (n = len(L1) + m = len(L2)) iteraciones en total O(n+m).
        # i == len(L1) # a lo sumo m iteraciones.
        # i =! len(L1) # a lo sumo n iteraciones.
    #Complejidad final O(n+m).

## Ejercicio 9 #############################################################
def traza(M1: list[list[int]]) -> int:
    # precond: M1 es cuadrada
    traza = 0
    for i in range(0, n):
        traza += M1[i][i]
    return traza

    # Complejidad del algoritmo es O(n).

## Ejercicio 10 #############################################################
def primo(numero: int) -> bool:
    # Precond: numero es no negativo
    if numero <= 1:
        return False
    else:
        cont = 0
        for i in range(2, numero + 1):
            if numero % i == 0:
                cont += 1
        if cont == 1:
            return True
        else:
            return False

    # El algoritmo tiene una complejidad de O(numero).

## Ejercicio 11 #############################################################
def factorial(numero: int):
    fact = 1
    for i in range(1, numero + 1):
        fact *= 1
    return fact

    # La complejidad de la funcion es O(numero)

## Ejercicio 12 #############################################################
def fibo(numero: int) -> int:
    fib0 = 0
    fib1 = 1
    if numero == 0:
        return fib1
    elif numero == 1:
        return fib2
    else:
        resultado = 0
        for i in range(2, numero + 1):
            resultado = fib1 + fib2
            fib1 = fib2
            fib2 = resultado
        return resultado

    # La complejidad del algoritmo es O(numero)
