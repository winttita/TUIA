"""
INFERENCIA EN CSP: Forward Checking y AC-3
===========================================

La inferencia reduce activamente los dominios de las variables
MIENTRAS se busca, eliminando valores que ya sabemos que van a
fallar antes de llegar a ellos. Hay dos niveles:

FORWARD CHECKING (FC):
  Cuando asignás una variable X, revisás solo los vecinos directos
  de X y eliminás valores incompatibles de sus dominios.
  Limitación: no ve conflictos entre variables futuras entre sí.

AC-3 (Arco Consistencia):
  Más potente. Cuando elimina un valor de Xᵢ, propaga en cadena
  revisando todos los vecinos de Xᵢ, y los vecinos de sus vecinos,
  hasta que no haya más cambios. Detecta inconsistencias que FC no ve.
"""

from collections import deque

# ══════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN DEL CSP — Australia
# ══════════════════════════════════════════════════════════════════════

VARIABLES = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
DOMINIO   = ['R', 'G', 'B']
VECINOS = {
    'WA':  ['NT', 'SA'],
    'NT':  ['WA', 'SA', 'Q'],
    'SA':  ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':   ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V':   ['SA', 'NSW'],
    'T':   [],
}


def es_consistente(var, valor, asignacion):
    for vecino in VECINOS[var]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False
    return True


# ══════════════════════════════════════════════════════════════════════
# FORWARD CHECKING
# ══════════════════════════════════════════════════════════════════════

def forward_checking(var, valor, asignacion, dominios):
    """
    Al asignar var=valor, eliminar ese valor de los dominios de
    los vecinos sin asignar. Si algún dominio queda vacío → fallo.
    Devuelve (exito, lista_de_eliminaciones) para poder deshacer.
    """
    eliminaciones = []

    for vecino in VECINOS[var]:
        if vecino not in asignacion:
            if valor in dominios[vecino]:
                dominios[vecino].remove(valor)
                eliminaciones.append((vecino, valor))

            if len(dominios[vecino]) == 0:
                # Dominio vacío → deshacer y reportar fallo
                for v, val in eliminaciones:
                    dominios[v].append(val)
                return False, []

    return True, eliminaciones


def deshacer_eliminaciones(eliminaciones, dominios):
    for var, valor in eliminaciones:
        dominios[var].append(valor)


def backtracking_FC(asignacion, dominios, nodos):
    if len(asignacion) == len(VARIABLES):
        return asignacion

    # MVR: variable con menos valores restantes
    sin_asignar = [v for v in VARIABLES if v not in asignacion]
    var = min(sin_asignar, key=lambda v: len(dominios[v]))

    for valor in dominios[var][:]:
        if es_consistente(var, valor, asignacion):
            nodos[0] += 1
            asignacion[var] = valor

            exito, eliminaciones = forward_checking(var, valor, asignacion, dominios)

            if exito:
                resultado = backtracking_FC(asignacion, dominios, nodos)
                if resultado is not None:
                    return resultado

            # Backtrack
            del asignacion[var]
            deshacer_eliminaciones(eliminaciones, dominios)

    return None


# ══════════════════════════════════════════════════════════════════════
# AC-3
# ══════════════════════════════════════════════════════════════════════

def revisar(xi, xj, dominios):
    """
    Elimina de dominio(xi) los valores sin soporte en dominio(xj).
    Un valor x tiene soporte si existe algún y en dominio(xj) compatible.
    En coloreado de mapas: compatible = colores distintos.
    Retorna True si eliminó algo.
    """
    eliminado = False
    for x in dominios[xi][:]:
        tiene_soporte = any(x != y for y in dominios[xj])
        if not tiene_soporte:
            dominios[xi].remove(x)
            eliminado = True
    return eliminado


def ac3(dominios):
    """
    Aplica arco-consistencia propagando en cascada.
    Modifica dominios in-place.
    Retorna False si detecta inconsistencia.
    """
    cola = deque()
    for var in VARIABLES:
        for vecino in VECINOS[var]:
            cola.append((var, vecino))

    while cola:
        xi, xj = cola.popleft()
        if revisar(xi, xj, dominios):
            if len(dominios[xi]) == 0:
                return False
            # Propagar: vecinos de xi pueden haber perdido soporte
            for xk in VECINOS[xi]:
                if xk != xj:
                    cola.append((xk, xi))

    return True


def backtracking_AC3(asignacion, dominios, nodos):
    if len(asignacion) == len(VARIABLES):
        return asignacion

    sin_asignar = [v for v in VARIABLES if v not in asignacion]
    var = min(sin_asignar, key=lambda v: len(dominios[v]))

    for valor in dominios[var][:]:
        if es_consistente(var, valor, asignacion):
            nodos[0] += 1
            asignacion[var] = valor

            # Guardar copia de dominios antes de modificar
            dominios_copia = {v: dominios[v][:] for v in VARIABLES}

            # Fijar dominio de var a {valor} y propagar con AC-3
            dominios[var] = [valor]
            if ac3(dominios):
                resultado = backtracking_AC3(asignacion, dominios, nodos)
                if resultado is not None:
                    return resultado

            # Backtrack: restaurar dominios
            del asignacion[var]
            for v in VARIABLES:
                dominios[v] = dominios_copia[v]

    return None


# ══════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    for nombre, usar_ac3 in [
        ("Backtracking + Forward Checking", False),
        ("Backtracking + AC-3",             True),
    ]:
        dominios = {var: DOMINIO[:] for var in VARIABLES}
        nodos = [0]
        if usar_ac3:
            sol = backtracking_AC3({}, dominios, nodos)
        else:
            sol = backtracking_FC({}, dominios, nodos)
        print(f"\n{nombre}")
        print(f"  Solución:          {sol}")
        print(f"  Nodos explorados:  {nodos[0]}")

    print()
    print("DIFERENCIA CLAVE:")
    print("  FC  → solo mira vecinos directos de la variable asignada.")
    print("  AC-3 → propaga en cadena: si elimina un valor de Xi,")
    print("         revisa todos los vecinos de Xi, y sus vecinos, etc.")
    print("         Detecta conflictos entre variables futuras que FC no ve.")
