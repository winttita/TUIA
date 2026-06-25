"""
COLONIA DE HORMIGAS (Ant Colony Optimization — ACO)
=====================================================

INSPIRACIÓN BIOLÓGICA:
  Las hormigas encuentran el camino más corto al alimento sin mapa ni
  coordinación central. Depositan feromona al caminar; la feromona se
  evapora con el tiempo. Los caminos cortos se recorren más seguido →
  acumulan más feromona antes de evaporarse → atraen más hormigas →
  retroalimentación positiva que converge al camino óptimo.

COMPONENTES:
  τ(i,j) = feromona en el arco i→j  (memoria colectiva histórica)
  η(i,j) = 1/distancia(i,j)          (visibilidad, intuición greedy)
  α      = peso de la feromona
  β      = peso de la visibilidad
  ρ      = tasa de evaporación (0 < ρ < 1)

FÓRMULA DE DECISIÓN (prob. de ir de i a j):
  P(i→j) = [τ(i,j)]^α · [η(i,j)]^β
            ──────────────────────────────
            Σₖ [τ(i,k)]^α · [η(i,k)]^β

CICLO DE FEROMONAS (orden importante):
  1. EVAPORACIÓN primero: τ(i,j) ← (1-ρ) · τ(i,j)
     → rutas malas son "olvidadas" gradualmente
  2. DEPÓSITO después: τ(i,j) ← τ(i,j) + 1/longitud_ruta
     → rutas cortas depositan más (Δτ = 1/long es mayor)

PARÁMETRO CRÍTICO:
  ρ (tasa de evaporación):
    - Baja (0.01): feromona acumulada fuerte → queda pegado a primeras rutas
    - Alta (0.95): casi sin memoria → pierde aprendizaje colectivo
    - Típico: 0.1 a 0.3
"""

import random
import math


def distancia(c1, c2):
    """Distancia euclidiana entre dos ciudades (x, y)."""
    return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)


def longitud_ruta(ruta, ciudades):
    """Longitud total del circuito, incluyendo vuelta al inicio."""
    n = len(ruta)
    return sum(
        distancia(ciudades[ruta[i]], ciudades[ruta[(i+1) % n]])
        for i in range(n)
    )


def aco_tsp(ciudades, n_hormigas=20, n_iter=100,
            alpha=1, beta=3, rho=0.1, verbose=True):
    """
    Resuelve TSP con ACO.

    ciudades: lista de tuplas (x, y)
    n_hormigas: cuántas soluciones se construyen por iteración
    n_iter:    iteraciones totales
    alpha:     peso de feromona (α=0 → ignora historia, solo greedy)
    beta:      peso de visibilidad (β=0 → ignora distancia, solo feromona)
    rho:       tasa de evaporación
    """
    n = len(ciudades)

    # Precalcular distancias para no recomputar en cada iteración
    dist = [[distancia(ciudades[i], ciudades[j])
             for j in range(n)] for i in range(n)]

    # Feromona inicial uniforme — ninguna ruta tiene ventaja al principio
    tau = [[1.0] * n for _ in range(n)]

    mejor_ruta = None
    mejor_long = float('inf')

    for iteracion in range(n_iter):
        rutas = []

        # FASE DE CONSTRUCCIÓN: cada hormiga construye una ruta completa
        for _ in range(n_hormigas):
            inicio = random.randint(0, n-1)
            ruta = [inicio]
            visitadas = {inicio}

            while len(ruta) < n:
                i = ruta[-1]

                # Calcular atractivo de cada ciudad no visitada
                probs = []
                for j in range(n):
                    if j not in visitadas:
                        feromona    = tau[i][j] ** alpha
                        visibilidad = (1.0 / dist[i][j]) ** beta
                        probs.append((j, feromona * visibilidad))

                # Selección probabilística tipo ruleta
                total = sum(p for _, p in probs)
                r = random.uniform(0, total)
                acum = 0
                for j, p in probs:
                    acum += p
                    if acum >= r:
                        ruta.append(j)
                        visitadas.add(j)
                        break

            rutas.append(ruta)

        # FASE DE ACTUALIZACIÓN DE FEROMONAS

        # Paso 1 — EVAPORACIÓN: todos los arcos pierden feromona
        # (rutas que no se refuercen serán "olvidadas")
        for i in range(n):
            for j in range(n):
                tau[i][j] *= (1 - rho)

        # Paso 2 — DEPÓSITO: cada hormiga refuerza su ruta
        # Δτ = 1/longitud → rutas cortas depositan más feromona
        for ruta in rutas:
            long = longitud_ruta(ruta, ciudades)
            delta = 1.0 / long
            for k in range(n):
                a, b = ruta[k], ruta[(k+1) % n]
                tau[a][b] += delta
                tau[b][a] += delta   # grafo no dirigido: ambas direcciones

            if long < mejor_long:
                mejor_long = long
                mejor_ruta = ruta[:]

        if verbose and iteracion % 20 == 0:
            print(f"Iter {iteracion:>3}: mejor longitud = {mejor_long:.2f}")

    return mejor_ruta, mejor_long


if __name__ == "__main__":
    random.seed(42)
    ciudades = [(random.randint(0, 100), random.randint(0, 100))
                for _ in range(10)]

    print(f"TSP con {len(ciudades)} ciudades")
    print("=" * 40)

    random.seed(0)
    ruta, longitud = aco_tsp(ciudades, n_hormigas=20, n_iter=100)

    print(f"\nMejor ruta:     {ruta}")
    print(f"Longitud total: {longitud:.2f}")
    print()
    print("DIFERENCIA CON GA:")
    print("  GA:  opera sobre representación completa (string de genes)")
    print("       → cruzamiento combina soluciones existentes")
    print("  ACO: construye soluciones incrementalmente ciudad por ciudad")
    print("       → la feromona guía cada decisión local")
