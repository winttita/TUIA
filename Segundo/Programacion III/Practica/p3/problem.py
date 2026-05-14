"""
Módulo con formulaciones de problemas de búsqueda.
"""

from typing import Any, List, Tuple
import copy
import random


class SearchProblem:
    """
    Clase genérica para una formulación de estados completa.
    Subclases deben implementar los métodos abstractos.
    """

    def estado_inicial(self) -> Any:
        """Devuelve el estado inicial."""
        raise NotImplementedError

    def acciones(self, estado: Any) -> List[Any]:
        """Devuelve la lista de acciones aplicables en el estado dado."""
        raise NotImplementedError

    def resultado(self, estado: Any, accion: Any) -> Any:
        """Devuelve el estado resultado de aplicar acción sobre estado."""
        raise NotImplementedError

    def valor_objetivo(self, estado: Any) -> float:
        """
        Devuelve el valor objetivo asociado al estado.
        """
        raise NotImplementedError

    def estado_aleatorio(self) -> Any:
        """Genera y devuelve un estado aleatorio del problema."""
        raise NotImplementedError


class EightPuzzleProblem(SearchProblem):
    """
    Formulación para el 8-puzzle.

    Estado: lista de 3 listas cada una con 3 enteros 0..8 (0 casilla vacía).
    Acciones: 'UP', 'DOWN', 'LEFT', 'RIGHT' (hacia donde se desplaza el 0).
    Valor objetivo: suma de distancias Manhattan de los tiles.
    """

    GOAL = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def __init__(self, initial: List[List[int]] = None):
        if initial is None:
            self._initial = self.estado_aleatorio()
        else:
            self._initial = copy.deepcopy(initial)

        # mapa de valor a posición objetivo
        self._pos_objetivo = {}
        for r in range(3):
            for c in range(3):
                v = self.GOAL[r][c]
                self._pos_objetivo[v] = (r, c)

    def estado_inicial(self) -> List[List[int]]:
        return copy.deepcopy(self._initial)

    def _buscar_cero(self, estado: List[List[int]]) -> Tuple[int, int]:
        for r in range(3):
            for c in range(3):
                if estado[r][c] == 0:
                    return r, c
        raise ValueError("Estado inválido: no contiene cero")

    def acciones(self, estado: List[List[int]]) -> List[str]:
        acts = []
        zr, zc = self._buscar_cero(estado)
        if zr > 0:
            acts.append("UP")
        if zr < 2:
            acts.append("DOWN")
        if zc > 0:
            acts.append("LEFT")
        if zc < 2:
            acts.append("RIGHT")
        return acts

    def resultado(self, estado: List[List[int]], accion: str) -> List[List[int]]:
        new_state = copy.deepcopy(estado)
        zr, zc = self._buscar_cero(estado)
        nr, nc = zr, zc
        if accion == "UP":
            nr -= 1
        elif accion == "DOWN":
            nr += 1
        elif accion == "LEFT":
            nc -= 1
        elif accion == "RIGHT":
            nc += 1
        else:
            raise ValueError(f"Acción inválida: {accion}")

        if not (0 <= nr < 3 and 0 <= nc < 3):
            raise IndexError("Movimiento fuera de límites")

        # intercambiar 0 con la casilla destino
        new_state[zr][zc], new_state[nr][nc] = new_state[nr][nc], new_state[zr][zc]
        return new_state

    def __contar_inversiones(self, perm: List[int]) -> int:
        """Cuenta el número de inversiones en una permutación."""
        inv = 0
        # sacar el 0 de la permutación
        perm = [x for x in perm if x != 0]
        for i in range(len(perm)):
            for j in range(i + 1, len(perm)):
                if perm[i] > perm[j]:
                    inv += 1
        return inv

    def __es_resoluble(self, perm: List[int]) -> bool:
        """Determina si una permutacion es resoluble."""
        return self.__contar_inversiones(perm) % 2 == 0

    def estado_aleatorio(self) -> List[List[int]]:
        perm = list(range(9))
        random.shuffle(perm)
        # asegurar que la permutación sea resoluble
        while not self.__es_resoluble(perm):
            random.shuffle(perm)
        return [perm[0:3], perm[3:6], perm[6:9]]

    def valor_objetivo(self, estado: List[List[int]]) -> int:
        """Suma de distancias Manhattan de cada ficha respecto al objetivo
        (0 ignorado)."""
        total = 0
        for r in range(3):
            for c in range(3):
                v = estado[r][c]
                if v == 0:
                    continue
                gr, gc = self._pos_objetivo[v]
                total += abs(r - gr) + abs(c - gc)
        return total


class EightQueensProblem(SearchProblem):
    """
    Formulación para las 8-reinas.

    Estado: lista de 8 enteros en 1..8; el i-ésimo elemento indica la fila
    de la reina en la columna i+1 (columnas indexadas 1..8).
    Acción: tupla (row, col) donde row en 1..8 y col en 1..8 indica mover la
    reina de la columna col a la fila row.
    Valor objetivo: número de pares de reinas que se atacan.
    """

    N = 8

    def __init__(self, initial: List[int] = None):
        if initial is None:
            self._initial = self.estado_aleatorio()
        else:
            if len(initial) != self.N:
                raise ValueError("Estado inicial debe tener longitud 8")
            self._initial = list(initial)

    def estado_inicial(self) -> List[int]:
        return list(self._initial)

    def acciones(self, estado: List[int]) -> List[Tuple[int, int]]:
        acts = []
        for col in range(1, self.N + 1):
            for row in range(1, self.N + 1):
                if estado[col - 1] != row:
                    acts.append((row, col))
        return acts

    def resultado(self, estado: List[int], accion: Tuple[int, int]) -> List[int]:
        row, col = accion
        if not (1 <= row <= self.N):
            raise ValueError("Fila fuera de rango")
        if not (1 <= col <= self.N):
            raise ValueError("Columna fuera de rango")
        new_state = list(estado)
        new_state[col - 1] = row
        return new_state

    def estado_aleatorio(self) -> List[int]:
        return [random.randint(1, self.N) for _ in range(self.N)]

    def valor_objetivo(self, estado: List[int]) -> int:
        """Cuenta pares de reinas que se atacan. 0 es solución."""
        conflictos = 0
        for i in range(1, self.N + 1):
            for j in range(i + 1, self.N + 1):
                ri = estado[i - 1]
                rj = estado[j - 1]
                if ri == rj:
                    conflictos += 1
                elif abs(ri - rj) == abs(i - j):
                    conflictos += 1
        return conflictos
