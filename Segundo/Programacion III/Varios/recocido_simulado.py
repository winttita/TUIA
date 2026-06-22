"""
RECOCIDO SIMULADO (Simulated Annealing) — Problema de las 8-Reinas
======================================================================

INSPIRACION FISICA:
En metalurgia, el recocido consiste en calentar un metal y enfriarlo
LENTAMENTE para que sus átomos encuentren una estructura cristalina
estable (mínima energía). Si lo enfriás de golpe, queda una estructura
desordenada y débil.

El algoritmo traduce esto a búsqueda: arranca con una "temperatura" T
alta (acepta casi cualquier movimiento, incluso malos -> mucha
exploración) y la va bajando gradualmente (cada vez más exigente,
hasta comportarse casi como Hill-Climbing puro al final).

LA FORMULA CLAVE:
Cuando el vecino es PEOR que el estado actual, no se descarta
automáticamente. Se acepta con probabilidad:

    P(aceptar) = e^(ΔE / T)

donde ΔE = valor(vecino) - valor(actual) es NEGATIVO (porque empeora),
y T es la temperatura actual. A T alta, esta probabilidad es alta
incluso para ΔE muy negativo. A T baja, la probabilidad cae a casi 0
salvo que ΔE sea casi 0 (un empeoramiento mínimo).

IMPORTANTE - DIFERENCIA DE CONVENCION:
La fórmula clásica del libro está pensada para MAXIMIZAR (ΔE > 0 es
bueno). Como acá estamos MINIMIZANDO ataques, invertimos el signo de
ΔE en el código: definimos delta = ataques_actual - ataques_vecino,
así que delta > 0 significa "mejoró" (igual que en la convención de
maximización). Es un detalle de implementación, no un cambio conceptual.
"""

import math
import random


def contar_ataques(tablero):
    """Igual que en Hill-Climbing y Tabú: pares de reinas que se atacan."""
    n = len(tablero)
    ataques = 0
    for c1 in range(n):
        for c2 in range(c1 + 1, n):
            f1, f2 = tablero[c1], tablero[c2]
            if f1 == f2 or abs(f1 - f2) == abs(c1 - c2):
                ataques += 1
    return ataques


def vecino_aleatorio(tablero):
    """
    A diferencia de Hill-Climbing y Tabú (que generaban TODOS los vecinos
    y elegían el mejor), Recocido Simulado genera UN SOLO vecino al azar
    en cada paso. Esto es mucho más barato computacionalmente, y tiene
    sentido porque de todas formas no siempre vamos a aceptar el mejor
    (la decisión de aceptar o no depende de la probabilidad, no de
    comparar contra todas las alternativas).
    """
    n = len(tablero)
    nuevo = tablero[:]
    col = random.randint(0, n - 1)
    fila_nueva = random.randint(0, n - 1)
    nuevo[col] = fila_nueva
    return nuevo


def recocido_simulado_reinas(n=8, T_inicial=50, alpha=0.995, T_min=0.01, verbose=True):
    """
    T_inicial: temperatura de arranque. Alta = acepta muchos movimientos malos al principio.
    alpha:     factor de enfriamiento, entre 0 y 1. Con 0.995, la temperatura
               se reduce un 0.5% en cada iteración (enfriamiento geométrico/exponencial).
    T_min:     temperatura mínima -> criterio de parada.
    """
    actual = [random.randint(0, n - 1) for _ in range(n)]
    ataques_actual = contar_ataques(actual)

    mejor = actual[:]
    mejor_ataques = ataques_actual

    T = T_inicial
    iteracion = 0

    while T > T_min and mejor_ataques > 0:
        vecino = vecino_aleatorio(actual)
        ataques_vecino = contar_ataques(vecino)

        # delta > 0 significa que el vecino MEJORA (tiene menos ataques)
        delta = ataques_actual - ataques_vecino

        if delta > 0:
            # El vecino es mejor -> aceptar siempre, sin importar la temperatura
            actual = vecino
            ataques_actual = ataques_vecino
        else:
            # El vecino es igual o peor -> aceptar con probabilidad e^(delta/T)
            # Nota: delta <= 0 acá, así que e^(delta/T) está entre 0 y 1.
            probabilidad = math.exp(delta / T)
            if random.random() < probabilidad:
                actual = vecino           # aceptamos el movimiento "malo"
                ataques_actual = ataques_vecino

        # Actualizar el mejor histórico (independientemente de hacia dónde
        # se mueva 'actual', siempre recordamos lo mejor que vimos)
        if ataques_actual < mejor_ataques:
            mejor = actual[:]
            mejor_ataques = ataques_actual

        T *= alpha   # enfriar la temperatura geométricamente
        iteracion += 1

        if verbose and iteracion % 200 == 0:
            print(f"Iter {iteracion}: T={T:.3f}  ataques_actual={ataques_actual}  "
                  f"mejor_historico={mejor_ataques}")

    if verbose:
        motivo = "SOLUCION PERFECTA" if mejor_ataques == 0 else "TEMPERATURA AGOTADA"
        print(f"\nFin tras {iteracion} iteraciones ({motivo})")

    return mejor, iteracion


if __name__ == "__main__":
    random.seed(42)

    resultado, iteraciones = recocido_simulado_reinas(
        n=8, T_inicial=50, alpha=0.995, T_min=0.01
    )

    print(f"\nTablero final: {resultado}")
    print(f"Ataques: {contar_ataques(resultado)}")
    print()
    print("COMPARACIÓN con los algoritmos anteriores:")
    print("  - Hill-Climbing puro:                ~12-14% de éxito (1 corrida)")
    print("  - Hill-Climbing + reinicio aleatorio:  ~99% de éxito (~7 reinicios)")
    print("  - Búsqueda Tabú:                       ~98% de éxito (1 corrida, ~50 iter)")
    print("  - Recocido Simulado:                   correlo varias veces para ver su tasa")
