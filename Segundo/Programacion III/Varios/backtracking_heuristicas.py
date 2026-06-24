"""
BACKTRACKING CON HEURÍSTICAS MVR, GRADO Y VLR
==============================================

Implementado sobre dos problemas:
  1. Coloreado de Australia (para ver el algoritmo paso a paso)
  2. N-Reinas (para ver el impacto real de las heurísticas en escala)

HEURÍSTICAS IMPLEMENTADAS:
  - MVR  (Mínimos Valores Restantes): elegir la variable con menos valores legales.
          Intuición: "primero en fallar" — detectar callejones sin salida antes.
  - Grado: desempate de MVR, elige la variable con más vecinos sin asignar.
          Intuición: mayor impacto hacia adelante en el grafo.
  - VLR  (Valor Menos Restrictivo): probar primero el valor que menos opciones
          elimina de los vecinos. Intuición: "primero en tener éxito".
"""

# ══════════════════════════════════════════════════════════════════════
# PROBLEMA 1: Coloreado de Australia
# ══════════════════════════════════════════════════════════════════════

VARIABLES = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
DOMINIO   = ['R', 'G', 'B']   # Rojo, Verde, Azul

VECINOS = {
    'WA':  ['NT', 'SA'],
    'NT':  ['WA', 'SA', 'Q'],
    'SA':  ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':   ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V':   ['SA', 'NSW'],
    'T':   [],   # Tasmania: sin vecinos, cualquier color válido
}


def es_consistente_australia(var, valor, asignacion):
    """Chequea que ningún vecino ya asignado tenga el mismo color."""
    for vecino in VECINOS[var]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False
    return True


def valores_legales_australia(var, asignacion, dominios):
    return [v for v in dominios[var]
            if es_consistente_australia(var, v, asignacion)]


def elegir_variable_sin_heuristica(asignacion, dominios):
    """Orden fijo: primera variable no asignada en la lista VARIABLES."""
    for var in VARIABLES:
        if var not in asignacion:
            return var


def elegir_variable_MVR(asignacion, dominios):
    """
    MVR con desempate por grado.
    Minimiza (valores_restantes, -grado) → menos valores Y más grado.
    """
    sin_asignar = [v for v in VARIABLES if v not in asignacion]

    def clave(var):
        restantes = len(valores_legales_australia(var, asignacion, dominios))
        grado = sum(1 for v in VECINOS[var] if v not in asignacion)
        return (restantes, -grado)

    return min(sin_asignar, key=clave)


def ordenar_valores_VLR(var, asignacion, dominios):
    """
    Ordena los valores de MENOS a MÁS restrictivo.
    Un valor es más restrictivo si elimina más opciones de los vecinos.
    """
    legales = valores_legales_australia(var, asignacion, dominios)

    def cuantos_elimina(valor):
        eliminados = 0
        for vecino in VECINOS[var]:
            if vecino not in asignacion:
                asignacion_temp = {**asignacion, var: valor}
                for v in dominios[vecino]:
                    if not es_consistente_australia(vecino, v, asignacion_temp):
                        eliminados += 1
        return eliminados

    return sorted(legales, key=cuantos_elimina)


def backtracking_australia(asignacion, dominios, usar_mvr, usar_vlr, nodos):
    if len(asignacion) == len(VARIABLES):
        return asignacion   # completa y consistente → solución

    # Decidir qué variable asignar
    if usar_mvr:
        var = elegir_variable_MVR(asignacion, dominios)
    else:
        var = elegir_variable_sin_heuristica(asignacion, dominios)

    # Decidir en qué orden probar los valores
    if usar_vlr:
        valores = ordenar_valores_VLR(var, asignacion, dominios)
    else:
        valores = valores_legales_australia(var, asignacion, dominios)

    for valor in valores:
        nodos[0] += 1
        asignacion[var] = valor

        resultado = backtracking_australia(
            asignacion, dominios, usar_mvr, usar_vlr, nodos)

        if resultado is not None:
            return resultado

        del asignacion[var]   # backtrack: deshacer la asignación

    return None   # ningún valor funcionó → señal de fallo hacia arriba


def resolver_australia(usar_mvr, usar_vlr, nombre):
    dominios = {var: DOMINIO[:] for var in VARIABLES}
    nodos = [0]
    sol = backtracking_australia({}, dominios, usar_mvr, usar_vlr, nodos)
    print(f"\n{nombre}")
    print(f"  Solución: {sol}")
    print(f"  Nodos explorados: {nodos[0]}")


# ══════════════════════════════════════════════════════════════════════
# PROBLEMA 2: N-Reinas (para ver el impacto en escala)
# ══════════════════════════════════════════════════════════════════════

def es_consistente_reinas(col, fila, asignacion):
    for col2, fila2 in asignacion.items():
        if fila2 == fila:
            return False   # misma fila
        if abs(fila2 - fila) == abs(col2 - col):
            return False   # misma diagonal
    return True


def valores_legales_reinas(col, asignacion, n):
    return [f for f in range(n)
            if es_consistente_reinas(col, f, asignacion)]


def backtracking_reinas(asignacion, n, usar_mvr, nodos):
    if len(asignacion) == n:
        return asignacion

    # Sin MVR: primera columna libre en orden
    # Con MVR: columna con menos filas legales disponibles
    if usar_mvr:
        col = min(
            [c for c in range(n) if c not in asignacion],
            key=lambda c: len(valores_legales_reinas(c, asignacion, n))
        )
    else:
        col = next(c for c in range(n) if c not in asignacion)

    for fila in valores_legales_reinas(col, asignacion, n):
        nodos[0] += 1
        asignacion[col] = fila
        resultado = backtracking_reinas(asignacion, n, usar_mvr, nodos)
        if resultado is not None:
            return resultado
        del asignacion[col]

    return None


if __name__ == "__main__":
    print("═" * 50)
    print("COLOREADO DE AUSTRALIA")
    print("═" * 50)
    resolver_australia(False, False, "Sin heurísticas (orden fijo)")
    resolver_australia(True,  False, "Solo MVR")
    resolver_australia(True,  True,  "MVR + VLR")

    print()
    print("═" * 60)
    print("N-REINAS: impacto de MVR a escala")
    print("═" * 60)
    print(f"{'N':>4} {'Sin MVR (nodos)':>20} {'Con MVR (nodos)':>20} {'Reducción':>12}")
    print("-" * 60)
    for n in [8, 12, 16, 20]:
        nodos_sin = [0]
        backtracking_reinas({}, n, False, nodos_sin)
        nodos_con = [0]
        backtracking_reinas({}, n, True, nodos_con)
        reduccion = (1 - nodos_con[0] / nodos_sin[0]) * 100
        print(f"{n:>4} {nodos_sin[0]:>20,} {nodos_con[0]:>20,} {reduccion:>11.1f}%")
