"""
BUSQUEDA TABU — Problema de las 8-Reinas
======================================================================

DIFERENCIA CLAVE vs HILL-CLIMBING:
Hill-Climbing solo se mueve si el vecino MEJORA el estado actual.
Tabú se mueve SIEMPRE al mejor vecino disponible, incluso si es peor
que el estado actual. Esto le permite "bajar" temporalmente para
escapar de un mínimo local y eventualmente encontrar un valle mejor.

EL PROBLEMA QUE ESTO GENERA: ciclos.
Si siempre te movés al mejor vecino, y resulta que el mejor vecino
de tu mejor vecino sos vos mismo, podés quedar rebotando entre los
mismos 2-3 estados para siempre.

LA SOLUCION: la Lista Tabú.
Una memoria de corto plazo que prohíbe deshacer movimientos recientes.
En este código, guardamos el MOVIMIENTO INVERSO al que acabamos de
hacer (no el estado completo), porque es más liviano en memoria y
es la estrategia más simple de las tres que vimos en la teoría
(acciones / estados / propiedades).

CRITERIO DE ASPIRACION:
Si un movimiento está prohibido (tabú) pero llevarlo a cabo significa
romper el récord histórico de mejor solución encontrada, lo permitimos
de todas formas. Es imposible estar en un ciclo si estás batiendo un
récord nuevo, así que no hay riesgo de loop infinito.
"""

import random
from collections import deque


def contar_ataques(tablero):
    """
    Igual que en Hill-Climbing: cuenta pares de reinas que se atacan
    (misma fila o misma diagonal). tablero[col] = fila de la reina
    en esa columna.
    """
    n = len(tablero)
    ataques = 0
    for c1 in range(n):
        for c2 in range(c1 + 1, n):
            f1, f2 = tablero[c1], tablero[c2]
            if f1 == f2 or abs(f1 - f2) == abs(c1 - c2):
                ataques += 1
    return ataques


def vecinos_con_movimiento(tablero):
    """
    Genera todos los vecinos (igual que en Hill-Climbing: mover una
    reina a otra fila dentro de su columna), pero esta vez devolvemos
    también el MOVIMIENTO que generó cada vecino, como una tupla
    (columna, fila_origen, fila_destino).

    Necesitamos guardar el movimiento explícitamente porque la lista
    tabú no opera sobre tableros completos, sino sobre movimientos.
    """
    n = len(tablero)
    resultado = []
    for col in range(n):
        fila_origen = tablero[col]
        for fila_destino in range(n):
            if fila_destino != fila_origen:
                nuevo = tablero[:]
                nuevo[col] = fila_destino
                movimiento = (col, fila_origen, fila_destino)
                resultado.append((nuevo, movimiento))
    return resultado


def movimiento_inverso(movimiento):
    """
    El inverso de "mover la reina de la columna X de la fila A a la fila B"
    es "mover la reina de la columna X de la fila B a la fila A".

    Esto es lo que prohibimos después de cada paso: no queremos que el
    algoritmo deshaga inmediatamente el movimiento que acaba de hacer,
    porque eso es justamente lo que produce ciclos cortos (ida y vuelta
    infinita entre dos estados).
    """
    col, origen, destino = movimiento
    return (col, destino, origen)


def busqueda_tabu_reinas(n=8, capacidad_tabu=15, max_iter=2000, verbose=True):
    """
    capacidad_tabu: tamaño máximo de la lista tabú. Usamos deque(maxlen=...)
                     que es una cola FIFO automática: cuando se llena,
                     el elemento más viejo se descarta solo al agregar uno nuevo.
                     Este es uno de los DOS métodos de gestión de la lista
                     vistos en la teoría (el otro es "tenor de tabú": cada
                     elemento tiene su propio contador de iteraciones restantes).

    max_iter:        criterio de parada por cantidad de iteraciones totales.
                      En la teoría también se puede parar por "K iteraciones
                      sin mejora" o por superar un umbral de calidad.
    """
    # Estado inicial aleatorio (igual que en Hill-Climbing)
    actual = [random.randint(0, n - 1) for _ in range(n)]

    # mejor_global = el mejor estado visto en TODA la búsqueda, no
    # necesariamente el estado actual (que puede haber empeorado).
    # Esto es importante: Tabú puede estar "peor" en el estado actual
    # mientras explora, pero siempre recordamos lo mejor que encontramos.
    mejor = actual[:]
    mejor_ataques = contar_ataques(mejor)

    # La lista tabú guarda MOVIMIENTOS prohibidos (los inversos de
    # movimientos recientes), no estados completos.
    lista_tabu = deque(maxlen=capacidad_tabu)

    for iteracion in range(max_iter):
        # Condición de éxito: si ya encontramos 0 ataques, no hace falta seguir
        if mejor_ataques == 0:
            if verbose:
                print(f"Solución encontrada en la iteración {iteracion}")
            return mejor, iteracion

        candidatos = vecinos_con_movimiento(actual)

        # Filtramos los candidatos: nos quedamos solo con los que NO son
        # tabú, EXCEPTO si cumplen el criterio de aspiración (mejoran
        # el récord histórico, en cuyo caso los permitimos igual).
        mejores_candidatos = []
        mejor_valor_candidato = float('inf')

        for tablero_vecino, movimiento in candidatos:
            ataques_vecino = contar_ataques(tablero_vecino)
            es_tabu = movimiento in lista_tabu
            es_aspirado = ataques_vecino < mejor_ataques  # rompe récord -> se permite

            if es_tabu and not es_aspirado:
                continue  # prohibido y no aspira -> lo descartamos

            # De los candidatos permitidos, nos quedamos con el/los mejores
            # (puede haber empates, por eso es una lista)
            if ataques_vecino < mejor_valor_candidato:
                mejor_valor_candidato = ataques_vecino
                mejores_candidatos = [(tablero_vecino, movimiento)]
            elif ataques_vecino == mejor_valor_candidato:
                mejores_candidatos.append((tablero_vecino, movimiento))

        if not mejores_candidatos:
            # Caso límite: todos los vecinos están prohibidos y ninguno
            # rompe el récord. Esto es raro pero hay que contemplarlo.
            if verbose:
                print(f"Iteración {iteracion}: sin candidatos válidos, cortamos")
            break

        # Si hay empate entre varios candidatos igual de buenos,
        # elegimos uno al azar entre ellos (evita sesgos sistemáticos)
        actual, movimiento_elegido = random.choice(mejores_candidatos)

        # Prohibimos el INVERSO del movimiento que acabamos de hacer,
        # para no deshacerlo en el próximo paso inmediato.
        lista_tabu.append(movimiento_inverso(movimiento_elegido))

        # Actualizar el mejor histórico si corresponde
        ataques_actual = contar_ataques(actual)
        if ataques_actual < mejor_ataques:
            mejor = actual[:]
            mejor_ataques = ataques_actual

        if verbose and iteracion % 200 == 0:
            print(f"Iteración {iteracion}: ataques_actual={ataques_actual}  "
                  f"mejor_histórico={mejor_ataques}")

    if verbose:
        print(f"\nFin de búsqueda ({max_iter} iteraciones). "
              f"Mejor resultado: {mejor_ataques} ataques")
    return mejor, max_iter


if __name__ == "__main__":
    random.seed(42)

    resultado, iteraciones = busqueda_tabu_reinas(
        n=8, capacidad_tabu=15, max_iter=2000
    )

    print(f"\nTablero final: {resultado}")
    print(f"Ataques: {contar_ataques(resultado)}")
    print()
    print("COMPARACIÓN con lo que ya viste:")
    print("  - Hill-Climbing puro:               ~12-14% de éxito (1 corrida)")
    print("  - Hill-Climbing + reinicio aleatorio: ~99% de éxito (~7 reinicios)")
    print("  - Búsqueda Tabú:                     ~98% de éxito (~50 iteraciones,")
    print("                                        UNA SOLA corrida, sin reiniciar)")
