## 00 #############################################################

def factorial(n: int) -> int:
    if n == 0:
        return 1
    
    return n * factorial(n-1)

## 01 #############################################################

def calcula_triangular(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n + calcula_triangular(n-1)
    
## 02 #############################################################

def fibonacci(n: int):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
## 03.1 #############################################################

def print_string(n: int, s: str) -> str:
    if n == 0:
        return ""
    else:
        return s + "\n" + print_string(n-1, s)
    
## 03.2 #############################################################

def repeat_string(n: int, s: str) -> str:
    if n == 0:
        return ""
    else:
        return s + repeat_string(n-1, s)

## 04 #############################################################

def iterativa(l: list[int]) -> int:
    c = 1
    for i in l:
        c = c * i
    return c

def trans_funcion(l: list[int]) -> int:
    if l == []:
        return 1
    else:
        return l[0] * trans_funcion(l[1:])

## 05 #############################################################

def find_max(l: list[int]) -> int:
    if not l:
        return 0
    elif len(l) == 1:
        return l[0]
    else:
        return max(l[0], find_max(l[1:])) 
    
## 06 #############################################################

def power(a: int, b:int) -> int:
    if a == 0 or b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)
    
## 07 #############################################################

def count_digits(n: int) -> int:
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)

## 08 #############################################################

def reverse_string_i(s: str) -> str:
    if not s:
        return ""
    else:
        return s[::-1]

def reverse_string_r(s: str) -> str:
    if not s:
        return ""
    else:
        return reverse_string_r(s[1:]) + s[0]

## 09 #############################################################

def replicate(l: list[int], n: int) -> list[int]:
    if not l:
        return []
    else:
        return [l[0]] * n + replicate(l[1:], n)
    
## 10 #############################################################

def is_palindrome(s: str) -> bool:
    if not s or len(s) == 1:
        return True
    elif s[0] == s[-1] and is_palindrome(s[1:-1]):
        return True
    else:
        return False

## 11 #############################################################

def mystery(a: int, b: int) -> int:
    if (b == 0):
        return a
    return mystery(2 * a, b - 1)

    # para el caso  f(x,3), para un x cualquiera, esta funcion muestra en pantalla x*2*2*2 (o x*6). Para una f(x,y) donde x e y son
    # numeros cualquiera, x representa el valor inicial del acumulador e y la cantidad de veces que se va a
    # multiplicar a este numero por 2.

## 12 #############################################################

def potencia(a: int, b: int) -> float:
    if a == 0 or b == 0:
        return 0
    elif b == 1:
        return a
    elif b == -1:
        return 1 / a
    elif b < 0:
        return (1 / a) * potencia(a, b+1)
    else:
        return a * potencia(a, b-1)
    
## 13 #############################################################

def aux(lista: list[float]) -> tuple[int, float]:
    if not lista:
        return (0, 0)
    else:
        c, s = aux(lista[1:])
        return (c + 1, lista[0] + s)

def average(lista: list[float]) -> float:
    if aux(lista) == (0, 0):
        return 0
    else:
        c, s = aux(lista)
        return s / c 

## 14.1 y .2 #############################################################

def posicion(a: str, b: str, i: int = 0) -> int:
    if len(b) > len(a):
        return None
    elif a.startswith(b):
        return i
    else:
        return posicion(a[1:], b, i+1)
    
## 15.1 #############################################################

memo = {} #Diccionario global

def fibonacci_2(n: int) -> int:
    if n in memo:
        return memo[n]

    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fibonacci_2(n-1) + fibonacci_2(n-2)

    return memo[n]

## 15.2 #############################################################

def fibonacci_memo(n: int, memo: dict[int, int]) -> tuple[int, dict[int, int]]:
    if n in memo:
        return memo[n]

    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    
    return (memo[n], memo.items())

memo = {}
print(fibonacci_memo(10, memo))