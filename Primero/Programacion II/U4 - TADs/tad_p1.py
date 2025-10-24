## Ejercicio 1 ############################################################################################################################################

from typing import Any

class _Nodo:
    def __init__(self, dato: Any = None, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

    def ver_lista(nodo) -> None:
        """Recorre todos los nodos a través de sus enlaces, mostrando sus
        contenidos.
        """
        while nodo is not None:
            print(nodo)
            nodo = nodo.prox

class ListaEnlazada:
    """Modela una lista enlazada."""

    def __init__(self) -> None:
        """Crea una lista enlazada vacía."""
        # Referencia al primer nodo (None si la lista está vacía)
        self.prim = None
        # Cantidad de elementos de la lista
        self.len = 0

    def insert(self, i: int, x: Any) -> None:
        """Inserta el elemento x en la posición i.
        Si la posición es inválida, imprime un error y retorna inmediatamente.
        """
        if i < 0 or i > self.len:
            print("Posición inválida")
            return
        nuevo = _Nodo(x)
        if i == 0:
            # Caso particular : insertar al principio
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            # Buscar el nodo anterior a la posición deseada
            n_ant = self.prim
            for pos in range(1, i):
                n_ant = n_ant.prox
            # Intercalar el nuevo nodo
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo
        self.len += 1

    def pop(self, i: int | None = None) -> Any:
        """Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se muestra un mensaje de error y se
        retorna inmediatamente. Si no se recibe la posición, devuelve el
        último elemento.
        """
        if i is None:
            i = self.len - 1
        if i < 0 or i >= self.len:
            print(" Posición inválida ")
            return
        if i == 0:
            # Caso particular: saltear la cabecera de la lista
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            # Buscar los nodos en las posiciones (i -1) e (i)
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range(1, i):
                n_ant = n_act
                n_act = n_ant.prox
            # Guardar el dato y descartar el nodo
            dato = n_act.dato
            n_ant.prox = n_act.prox
            self.len -= 1
        return dato

    def remove(self, x: Any) -> None:
        """Borra la primera aparición del valor x en la lista.
        Si x no está en la lista, imprime un mensaje de error y retorna
        inmediatamente.
        """
        if self.len == 0:
            print("La lista esta vacía")
            return
        if self.prim.dato == x:
            # Caso particular: saltear la cabecera de la lista
            self.prim = self.prim.prox
        else:
            # Buscar el nodo anterior al que contiene a x (n_ant)
            n_ant = self.prim
            n_act = n_ant.prox
            while n_act is not None and n_act.dato != x:
                n_ant = n_act
                n_act = n_ant.prox
            if n_act is None:
                print("El valor no está en la lista.")
                return
            # Descartar el nodo
            n_ant.prox = n_act.prox
            self.len -= 1

    def __len__(self) -> int:
        """Muestra la longitud de la lista."""
        return self.len

    def __str__(self):
        """Muestra el contenido de la lista enlazada."""
        ret = '['
        n_ant = self.prim
        for no in range(self.len):
            ret += str(n_ant.dato) + ', '

        ret = ret[:-2] + ']'
        return ret
        
    def index(self, x: Any) -> int:
        nodo = self.prim
        i = 0
        while nodo is not None:
            if nodo.dato == x:
                return  i
            i += 1
            nodo = nodo.prox
        return -1

    def append(self, x: Any) -> None:
        n_ant = self.prim
        if n_ant is None:
            n_nuevo = _Nodo(x)
            self.prim = n_nuevo
            self.len += 1
        for no in range(self.len -1):
            n_ant = n_ant.prox
        n_nuevo = _Nodo(x)
        n_ant.prox = n_nuevo
        self.len += 1

## Ejercicio 2 ############################################################################################################################################

    def extend(self, lista: ListaEnlazada) -> None:
        n_ant = self.prim

        for i in range(self.len - 1):
            n_ant = n_ant.prox

        n_ant.prox = lista.prim

        self.len += lista.len

## Ejercicio 3 ############################################################################################################################################

    def remover_todos(self, x: Any) -> int:
        nuevo = _Nodo(x)
        ant = self.prim
        cant = 0
        pos = 0
        while ant.prox is not None:
            if nuevo.dato == ant.dato:
                self.pop(pos)
                cant += 1
                self.len -= 1
            ant = ant.prox
            pos += 1
        return cant

## Ejercicio 4 ############################################################################################################################################           

    def duplicar(self, x: Any) -> None:
        nuevo = _Nodo(x)
        ant = self.prim
        pos = 0
        while ant.prox is not None:
            if nuevo.dato == ant.dato:
                self.insert(pos+1, nuevo)
                self.len += 1
        return

## Ejercicio 5 ############################################################################################################################################

    def invertir_lista(self) -> None:
        invert = ListaEnlazada()
        ant = self.prim
        while ant.prox is not None:
            if not invert:
                invert.append(ant)
                ant = ant.prox
            else:
                invert.insert(0, ant)
                ant = ant.prox
        pass