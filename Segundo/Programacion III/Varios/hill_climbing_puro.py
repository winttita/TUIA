"""
HILL-CLIMBING PURO (Ascensión de Colinas) — Problema de las 8-Reinas
======================================================================

OBJETIVO DEL PROBLEMA:
Ubicar N reinas en un tablero de NxN de forma que ninguna ataque a otra
(no compartan fila, columna ni diagonal).

REPRESENTACIÓN DEL ESTADO:
Usamos una lista de N elementos: tablero[col] = fila donde está la reina
de esa columna. Por construcción, nunca hay dos reinas en la misma columna
(eso ya está resuelto por la representación), así que solo hace falta
chequear filas y diagonales.

FUNCIÓN OBJETIVO (a minimizar):
Cantidad de PARES de reinas que se atacan entre sí. El óptimo es 0.

ESTRATEGIA DEL ALGORITMO:
En cada paso, miramos TODOS los vecinos posibles (mover una sola reina
a otra fila dentro de su columna), y nos movemos al mejor de ellos.
Si ningún vecino mejora la situación actual, nos detenemos ahí mismo
-> esto es lo que causa que quedemos atrapados en MÍNIMOS LOCALES.
"""

import random


def contar_ataques(tablero):
    """
    Cuenta cuántos PARES de reinas se atacan entre sí.

    Dos reinas en columnas c1 y c2 (con c1 < c2) y filas f1 y f2 se atacan si:
      - están en la misma fila:           f1 == f2
      - están en la misma diagonal:       |f1 - f2| == |c1 - c2|
        (la diferencia de filas es igual a la diferencia de columnas,
         eso es justamente lo que define una diagonal de 45°)

    Recorremos todos los pares (c1, c2) con c1 < c2 para no contar
    cada par dos veces.
    """
    n = len(tablero)
    ataques = 0
    for c1 in range(n):
        for c2 in range(c1 + 1, n):
            f1, f2 = tablero[c1], tablero[c2]
            misma_fila = (f1 == f2)
            misma_diagonal = abs(f1 - f2) == abs(c1 - c2)
            if misma_fila or misma_diagonal:
                ataques += 1
    return ataques


def vecinos(tablero):
    """
    Genera TODOS los estados vecinos de 'tablero'.

    Un vecino se obtiene moviendo UNA SOLA reina a otra fila,
    dentro de su misma columna (las demás reinas quedan fijas).

    Para n=8: hay 8 columnas, y en cada una 7 filas alternativas
    posibles (todas menos la actual) -> 8 x 7 = 56 vecinos en total.

    Esto es importante: NO modificamos 'tablero' directamente,
    hacemos una COPIA (tablero[:]) para cada vecino, porque si no
    estaríamos pisando el estado original mientras lo recorremos.
    """
    n = len(tablero)
    resultado = []
    for col in range(n):
        for fila in range(n):
            if fila != tablero[col]:        # no tiene sentido "moverse" al mismo lugar
                nuevo = tablero[:]            # copia superficial de la lista
                nuevo[col] = fila             # mover la reina de esa columna
                resultado.append(nuevo)
    return resultado


def hill_climbing_reinas(n=8, verbose=True):
    """
    Hill-Climbing puro (greedy, sin movimientos laterales, sin reinicios).

    PASO A PASO:
    1. Arrancamos con un tablero completamente aleatorio.
    2. En cada iteración generamos TODOS los vecinos posibles.
    3. Elegimos el vecino con MENOR cantidad de ataques (porque acá
       estamos MINIMIZANDO, a diferencia del pseudocódigo genérico del
       resumen que maximiza -> la lógica es simétrica, solo cambia
       max() por min()).
    4. Si ese mejor vecino NO mejora respecto al estado actual
       (es decir, tiene igual o más ataques), significa que estamos
       en un mínimo local (o una meseta) -> nos detenemos ahí.
    5. Si mejora, nos movemos a ese vecino y repetimos.

    Devuelve: (tablero_final, cantidad_de_pasos, motivo_de_parada)
    """
    actual = [random.randint(0, n - 1) for _ in range(n)]  # estado inicial aleatorio
    paso = 0

    while True:
        ataques_actual = contar_ataques(actual)

        if verbose:
            print(f"Paso {paso}: tablero={actual}  ataques={ataques_actual}")

        # Condición de éxito: 0 ataques significa solución perfecta
        if ataques_actual == 0:
            return actual, paso, "SOLUCION ENCONTRADA"

        # Generar todos los vecinos y quedarnos con el mejor (menos ataques)
        candidatos = vecinos(actual)
        mejor_vecino = min(candidatos, key=contar_ataques)
        ataques_mejor_vecino = contar_ataques(mejor_vecino)

        # Si el mejor vecino no es estrictamente mejor que el actual,
        # estamos atascados: ni un solo movimiento nos ayuda.
        # Esto puede ser un MÍNIMO LOCAL (todos los vecinos son peores)
        # o una MESETA (algunos vecinos son iguales, ninguno mejor).
        if ataques_mejor_vecino >= ataques_actual:
            return actual, paso, "ATASCADO EN MINIMO LOCAL"

        # Si llegamos acá, hay mejora real: nos movemos
        actual = mejor_vecino
        paso += 1


if __name__ == "__main__":
    # Semilla fija para que el resultado sea reproducible.
    # Cambiá el número o sacá esta línea para ver corridas distintas.
    random.seed(34)

    resultado, pasos, estado_final = hill_climbing_reinas(n=8)

    print()
    print(f"Resultado final: {resultado}")
    print(f"Ataques restantes: {contar_ataques(resultado)}")
    print(f"Estado: {estado_final}")
    print()
    print("NOTA: corré este script varias veces (cambiando la seed) y vas a ver")
    print("que la mayoría de las veces NO llega a 0 ataques -> eso es Hill-Climbing")
    print("puro quedando atrapado en mínimos locales. Estadísticamente, ronda")
    print("un 12-14% de éxito en 8-reinas.")
