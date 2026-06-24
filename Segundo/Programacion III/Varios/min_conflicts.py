"""
MIN-CONFLICTS — CSP con Búsqueda Local
=======================================

PARADIGMA DIFERENTE al Backtracking:
  Backtracking: asignación PARCIAL, nunca viola restricciones,
                retrocede cuando se atasca.
  Min-Conflicts: asignación COMPLETA desde el principio (aunque
                 viole restricciones), las arregla iterativamente.

ALGORITMO:
  1. Generar asignación completa aleatoria (puede tener conflictos)
  2. Repetir hasta solución o agotar pasos:
     a. Si no hay conflictos → retornar solución
     b. Elegir AL AZAR una variable en conflicto
     c. Asignarle el valor que MINIMICE sus conflictos

POR QUÉ FUNCIONA:
  La aleatoriedad en el paso (b) evita ciclos simples sin necesitar
  una lista tabú. Si hubiera que elegir la variable con MÁS conflictos
  determinísticamente, el algoritmo ciclaría entre los mismos estados.

CUÁNDO ES MEJOR QUE BACKTRACKING:
  En problemas con muchas soluciones distribuidas por el espacio
  (como N-Reinas), donde moverse al mínimo de conflictos casi siempre
  lleva rápido a una solución. Min-Conflicts resuelve N=1.000.000
  reinas en segundos — algo imposible para Backtracking.

CUÁNDO FALLA:
  En problemas con pocas soluciones y muchas restricciones cruzadas,
  puede quedar atrapado en mínimos locales (igual que Hill-Climbing),
  donde ninguna variable puede mejorar sin empeorar otra.
"""

import random


def contar_conflictos_reina(tablero, col, fila):
    """
    Cuenta cuántas reinas en el tablero atacan a la posición (col, fila).
    No cuenta la reina de la propia columna (nos interesa evaluar si
    poner la reina de esa columna en esa fila causa conflictos con el resto).
    """
    n = len(tablero)
    conflictos = 0
    for c in range(n):
        if c == col:
            continue
        f = tablero[c]
        # Misma fila o misma diagonal
        if f == fila or abs(f - fila) == abs(c - col):
            conflictos += 1
    return conflictos


def min_conflicts_reinas(n, max_pasos=50000):
    """
    Resuelve N-Reinas con Min-Conflicts.
    tablero[col] = fila donde está la reina de esa columna.

    Devuelve (tablero_solucion, pasos_usados) o (None, max_pasos) si falla.
    """
    # Asignación inicial: permutación aleatoria
    # (garantiza exactamente una reina por fila, reduciendo conflictos iniciales)
    tablero = list(range(n))
    random.shuffle(tablero)

    for paso in range(max_pasos):

        # Paso 2a: detectar qué columnas tienen al menos un conflicto
        en_conflicto = [
            col for col in range(n)
            if contar_conflictos_reina(tablero, col, tablero[col]) > 0
        ]

        if not en_conflicto:
            return tablero, paso   # sin conflictos → solución

        # Paso 2b: elegir UNA columna en conflicto AL AZAR
        # (la aleatoriedad evita ciclos sin necesitar lista tabú)
        col = random.choice(en_conflicto)

        # Paso 2c: evaluar cada fila posible para esa columna
        conflictos_por_fila = [
            contar_conflictos_reina(tablero, col, fila)
            for fila in range(n)
        ]

        # Quedarse con las filas que tienen el mínimo de conflictos
        min_conf = min(conflictos_por_fila)
        mejores_filas = [
            fila for fila in range(n)
            if conflictos_por_fila[fila] == min_conf
        ]

        # Si hay empate, elegir al azar (más diversificación)
        tablero[col] = random.choice(mejores_filas)

    return None, max_pasos   # agotó los pasos sin encontrar solución


if __name__ == "__main__":
    print("Min-Conflicts en N-Reinas")
    print(f"{'N':>6} {'Pasos':>10} {'Resultado':>12}")
    print("-" * 32)

    for n in [8, 50, 100]:
        random.seed(42)
        resultado, pasos = min_conflicts_reinas(n)
        estado = "OK" if resultado is not None else "FALLO"
        print(f"{n:>6} {pasos:>10,} {estado:>12}")

    print()
    print("COMPARACIÓN con Backtracking (sin heurísticas, N-Reinas):")
    print("  N= 8 → Backtracking: ~113 nodos | Min-Conflicts: ~15 pasos")
    print("  N=20 → Backtracking: ~200.000 nodos | Min-Conflicts: ~50 pasos")
    print()
    print("El crecimiento de Min-Conflicts es casi LINEAL en N-Reinas.")
    print("El de Backtracking sin heurísticas es EXPONENCIAL.")
