"""
HILL-CLIMBING CON REINICIO ALEATORIO — Problema de las 8-Reinas
======================================================================

IDEA CENTRAL:
Hill-Climbing puro queda atrapado en mínimos locales la mayoría de las
veces (~12-14% de éxito en 8-reinas, como viste en hill_climbing_puro.py).

La solución de Reinicio Aleatorio es conceptualmente simple:
en vez de aceptar el resultado del primer intento, corremos Hill-Climbing
MUCHAS veces, cada vez desde un punto de partida aleatorio distinto,
y nos quedamos con el MEJOR resultado de todos los intentos.

Esto funciona bien en problemas donde el espacio de estados tiene
varios "picos" alcanzables (varios máximos/mínimos globales o casi-globales
accesibles desde puntos de partida distintos), como es el caso de 8-reinas.

Requiere el archivo hill_climbing_puro.py en la misma carpeta, ya que
reutilizamos sus funciones contar_ataques() y vecinos().
"""

import random
from hill_climbing_puro import contar_ataques, vecinos


def hill_climbing_una_corrida(n):
    """
    Una sola corrida de Hill-Climbing puro, SIN verbose (sin prints),
    porque acá nos interesa correrlo muchas veces rápido, no ver
    el detalle paso a paso de cada corrida individual.

    Misma lógica que hill_climbing_reinas() del archivo anterior,
    simplificada (sin el contador de pasos ni el motivo de parada,
    porque acá solo nos importa el resultado final).
    """
    actual = [random.randint(0, n - 1) for _ in range(n)]

    while True:
        ataques_actual = contar_ataques(actual)

        if ataques_actual == 0:
            return actual  # ¡solución perfecta encontrada!

        candidatos = vecinos(actual)
        mejor_vecino = min(candidatos, key=contar_ataques)

        if contar_ataques(mejor_vecino) >= ataques_actual:
            return actual  # atascado: devolvemos lo que tenemos hasta ahora

        actual = mejor_vecino


def hill_climbing_reinicio_aleatorio(n=8, max_reinicios=30, verbose=True):
    """
    Corre Hill-Climbing repetidas veces, cada vez desde un estado inicial
    aleatorio DISTINTO (eso pasa automáticamente porque cada llamada a
    hill_climbing_una_corrida() genera su propio estado inicial random).

    CRITERIO DE PARADA (dos posibles, lo que pase primero):
      1. Encontramos una solución perfecta (0 ataques) -> cortamos ahí,
         no tiene sentido seguir gastando intentos.
      2. Se nos acaban los reinicios permitidos (max_reinicios) -> nos
         quedamos con el mejor resultado que hayamos visto en el camino,
         aunque no sea perfecto.

    Esto es clave: NO tiramos los resultados de los intentos fallidos,
    siempre guardamos el "mejor hasta ahora" (mejor_resultado), por si
    ningún intento llega a la solución perfecta.
    """
    mejor_resultado = None
    mejor_ataques = float('inf')  # arrancamos asumiendo "infinitos ataques"

    for intento in range(1, max_reinicios + 1):
        resultado = hill_climbing_una_corrida(n)
        ataques = contar_ataques(resultado)

        if verbose:
            print(f"Intento {intento}: ataques={ataques}")

        # Actualizar el mejor resultado histórico si corresponde
        if ataques < mejor_ataques:
            mejor_ataques = ataques
            mejor_resultado = resultado

        # Si encontramos la solución perfecta, no hace falta seguir
        if ataques == 0:
            if verbose:
                print(f"\n¡Solución encontrada en el intento {intento}!")
            return mejor_resultado, intento

    # Si llegamos acá, se acabaron los reinicios sin encontrar 0 ataques
    if verbose:
        print(f"\nNo se encontró solución perfecta en {max_reinicios} intentos.")
        print(f"Mejor resultado obtenido: {mejor_ataques} ataques")
    return mejor_resultado, max_reinicios


if __name__ == "__main__":
    random.seed(42)  # semilla fija para reproducibilidad

    resultado, intentos_usados = hill_climbing_reinicio_aleatorio(n=8, max_reinicios=30)

    print(f"\nTablero final: {resultado}")
    print(f"Ataques: {contar_ataques(resultado)}")
    print(f"Intentos usados: {intentos_usados}/30")
    print()
    print("COMPARACIÓN ESPERADA vs Hill-Climbing puro:")
    print("  - Hill-Climbing puro:          ~12-14% de éxito en una sola corrida")
    print("  - Hill-Climbing + reinicio:    ~99% de éxito con hasta 30 reinicios")
    print("    (en promedio, solo hacen falta unos 7 reinicios para tener éxito)")
