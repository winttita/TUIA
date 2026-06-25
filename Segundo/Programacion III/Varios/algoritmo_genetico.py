"""
ALGORITMO GENÉTICO (Genetic Algorithm — GA)
============================================

INSPIRACIÓN BIOLÓGICA:
  Darwin: los individuos más aptos tienen más chances de reproducirse
  y pasar sus genes. Con el tiempo, la población evoluciona.

TRADUCCIÓN AL ALGORITMO:
  Individuo    = solución candidata
  Genes        = representación de la solución (bits, permutación, etc.)
  Fitness      = qué tan buena es la solución (función objetivo)
  Selección    = individuos con mayor fitness tienen más chances de reproducirse
  Cruzamiento  = combinar genes de dos padres para generar hijos
  Mutación     = cambio aleatorio pequeño para mantener diversidad

CICLO:
  1. Población inicial aleatoria
  2. Evaluar fitness de cada individuo
  3. Seleccionar pares de padres (ruleta: prob ∝ fitness)
  4. Cruzar padres → hijos
  5. Mutar hijos con prob. baja
  6. Nueva generación → volver a 2

PARÁMETROS CRÍTICOS (calibrar experimentalmente):
  - Tamaño de población: más grande = más diversidad, más lento por generación
  - Prob. cruzamiento (~0.8): alta para explorar combinaciones nuevas
  - Prob. mutación (~0.01): baja para no destruir lo aprendido
    * Sin mutación: convergencia prematura si se pierde diversidad
    * Con demasiada: búsqueda aleatoria sin dirección
  - Generaciones: criterio de parada por tiempo/calidad
"""

import random

N_GENES = 20   # largo del string de bits


def fitness(individuo):
    """
    Función objetivo: contar unos en el string.
    Máximo posible = N_GENES (todos unos).
    """
    return sum(individuo)


def poblacion_inicial(tam_poblacion, n_genes):
    """Individuos aleatorios de bits."""
    return [
        [random.randint(0, 1) for _ in range(n_genes)]
        for _ in range(tam_poblacion)
    ]


def seleccionar(poblacion):
    """
    Selección por ruleta: probabilidad de ser elegido
    proporcional al fitness. Individuos malos también tienen
    alguna chance → mantiene diversidad genética.
    """
    fitnesses = [fitness(ind) for ind in poblacion]
    total = sum(fitnesses)

    if total == 0:
        return random.choice(poblacion)

    r = random.uniform(0, total)
    acumulado = 0
    for ind, f in zip(poblacion, fitnesses):
        acumulado += f
        if acumulado >= r:
            return ind
    return poblacion[-1]


def cruzar(padre_a, padre_b):
    """
    Cruce de un punto: elegir punto de corte al azar,
    cada hijo hereda inicio de un padre y final del otro.

    Padre A: [1 1 0 0 | 1 0 1 1]
    Padre B: [0 0 1 1 | 0 1 0 0]
    Hijo 1:  [1 1 0 0 | 0 1 0 0]
    Hijo 2:  [0 0 1 1 | 1 0 1 1]
    """
    punto = random.randint(1, len(padre_a) - 1)
    hijo1 = padre_a[:punto] + padre_b[punto:]
    hijo2 = padre_b[:punto] + padre_a[punto:]
    return hijo1, hijo2


def mutar(individuo, prob_mutacion):
    """
    Invertir cada bit con probabilidad prob_mutacion.
    Prob. baja (0.01) para no destruir lo aprendido,
    pero suficiente para introducir diversidad nueva.
    """
    return [
        gen if random.random() > prob_mutacion else 1 - gen
        for gen in individuo
    ]


def algoritmo_genetico(
    tam_poblacion=50,
    n_generaciones=100,
    prob_cruzamiento=0.8,
    prob_mutacion=0.01,
    verbose=True
):
    poblacion = poblacion_inicial(tam_poblacion, N_GENES)

    for gen in range(n_generaciones):
        mejor = max(poblacion, key=fitness)

        if verbose and gen % 10 == 0:
            fitnesses = [fitness(ind) for ind in poblacion]
            print(f"Gen {gen:>3}: mejor={fitness(mejor):>3}  "
                  f"promedio={sum(fitnesses)/len(fitnesses):.1f}  "
                  f"individuo={mejor}")

        # Criterio de parada: solución óptima encontrada
        if fitness(mejor) == N_GENES:
            if verbose:
                print(f"\nSolución óptima en generación {gen}!")
            return mejor, gen

        # Generar nueva población
        nueva_poblacion = []
        while len(nueva_poblacion) < tam_poblacion:
            padre_a = seleccionar(poblacion)
            padre_b = seleccionar(poblacion)

            if random.random() < prob_cruzamiento:
                hijo1, hijo2 = cruzar(padre_a, padre_b)
            else:
                hijo1, hijo2 = padre_a[:], padre_b[:]

            nueva_poblacion += [
                mutar(hijo1, prob_mutacion),
                mutar(hijo2, prob_mutacion)
            ]

        poblacion = nueva_poblacion[:tam_poblacion]

    mejor = max(poblacion, key=fitness)
    return mejor, n_generaciones


if __name__ == "__main__":
    random.seed(42)
    print(f"Problema: maximizar unos en string de {N_GENES} bits")
    print(f"Solución óptima: {[1]*N_GENES}  fitness={N_GENES}")
    print("=" * 60)
    resultado, generaciones = algoritmo_genetico()
    print(f"\nResultado final: {resultado}")
    print(f"Fitness: {fitness(resultado)}/{N_GENES}")
    print()
    print("NOTA SOBRE MUTACIÓN:")
    print("  0.0  → convergencia prematura (pierde diversidad)")
    print("  0.01 → punto óptimo empírico")
    print("  0.2  → búsqueda aleatoria (destruye lo aprendido)")
