## Ejercicio 1 ############################################################################################################################################

from typing import Any
import math

def es_primo(x: int) -> bool:
        if not isinstance(x, int) or x <= 1:
            return False
        elif x == 2:
            return True
        else:
            for i in range(2,  x):
                if x % i == 0:
                    return False
            return True

class _Nodo:
    def __init__(self, dato: Any = None, prox=None) -> None:
        self.dato = dato
        self.prox = prox

    def __str__(self) -> str:
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

    def __str__(self) -> str:
        """Muestra el contenido de la lista enlazada."""
        ret = '['
        n_ant = self.prim
        for no in range(self.len):
            ret += str(n_ant.dato) + ', '
            n_ant = n_ant.prox
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
            return
        for no in range(self.len -1):
            n_ant = n_ant.prox
        n_nuevo = _Nodo(x)
        n_ant.prox = n_nuevo
        self.len += 1
        return

## Ejercicio 2 ############################################################################################################################################

    def extend(self, lista: 'ListaEnlazada') -> None:
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
        while ant is not None:
            if nuevo.dato == ant.dato:
                self.pop(pos)
                cant += 1
            ant = ant.prox
            pos += 1
        return cant

## Ejercicio 4 ############################################################################################################################################           

    def duplicar(self, x: Any) -> None:
        nuevo = _Nodo(x)
        ant = self.prim
        pos = 0
        while ant is not None:
            if nuevo.dato == ant.dato:
                self.insert(pos+1, nuevo.dato)
        return

## Ejercicio 5 ############################################################################################################################################

    def invertir_lista(self) -> None:
        invert = ListaEnlazada()
        act = self.prim
        while act is not None:
            if invert.prim is None:
                invert.append(act.dato)
                act = act.prox
            else:
                invert.insert(0, act.dato)
                act = act.prox
        self.prim = invert.prim
        return
    
## Ejercicio 7 ############################################################################################################################################

    def filtrar_primos(self) -> 'ListaEnlazada':
        primos = ListaEnlazada()
        act = self.prim
        ult = None
        while act is not None:
            if es_primo(act.dato):
                nuevo = _Nodo(act.dato)
                if primos.prim is None:
                    primos.prim = nuevo
                    ult = nuevo
                else:
                    ult.prox = nuevo
                    ult = nuevo
                primos.len += 1
            act = act.prox
        return primos
    
## Ejercicio 8 ############################################################################################################################################

    def insertar_palabra_despues(self, l: 'ListaEnlazada', palabra_objetivo: str, palabra_insertar: str) -> 'ListaEnlazada':
        l2 = ListaEnlazada()
        act = l.prim
        ult = None
        while act is not None:
            nuevo = _Nodo(act.dato)
            if l2.prim is None:
                l2.prim = nuevo
                ult = nuevo
            else:
                ult.prox = nuevo
                ult = nuevo
                
            if act.dato.upper() == palabra_objetivo.upper():
                extra = _Nodo(palabra_insertar)
                ult.prox = extra
                ult = extra
            act = act.prox
        return l2
## Ejercicio 9 ############################################################################################################################################

    def eliminar_palabra_con(self, l: 'ListaEnlazada', caracter: str) -> 'ListaEnlazada':
        l2 = ListaEnlazada()
        act = l.prim
        ult = None
        while act is not None:
            nodo = _Nodo(act.dato)
            if isinstance(act.dato, str):
                if caracter not in nodo.dato:                     
                    if l2.prim is None:
                        l2.prim = nodo
                        ult = nodo
                    else:
                        ult.prox = nodo
                        ult = nodo
            else:
                print(f"El dato: {act.dato} no es un caracter. Se omite.")
            act = act.prox
        return l2

## Ejercicio 6 ############################################################################################################################################
class _Nodo2:
    def __init__(self, dato: Any = None, prox = None, ant = None) ->None:
        self.dato = dato
        self.prox = prox
        self.ant = ant

    def __str__(self) -> str:
        return str(self.dato)

    def ver_lista(nodo) -> None:
        """Recorre todos los nodos a través de sus enlaces, mostrando sus
        contenidos.
        """
        while nodo is not None:
            print(nodo)
            nodo = nodo.prox

class ListaDoblementeEnlazada:
    """Modela una lista DOBLEMENTE enlazada."""

    def __init__(self) -> None:
        """Crea una lista enlazada vacía."""
        # Referencia al primer nodo (None si la lista está vacía)
        self.prim = None
        # Cantidad de elementos de la lista
        self.len = 0
        #Referencia al ultimo elemento de la lista (None si esta vacia)
        self.ult = None

    def insert(self, i: int, x: Any) -> None:
        """Inserta el elemento x en la posición i.
        Si la posición es inválida, imprime un error y retorna inmediatamente.
        """
        if i < 0 or i > self.len:
            print("Posición inválida")
            return
        nuevo = _Nodo2(x)
        if i == 0:
            if self.len == 0:
                self.prim = self.ult = nuevo
                return
            else:
                self.ult = nuevo
                return

            
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
        """
        Muestra la longitud de la lista
        """
        return self.len

    def __str__(self) -> str:
        """
            Muestra el contenido de la lista enlazada.
        """
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
            n_nuevo = _Nodo2(x)
            self.prim = n_nuevo
            self.len += 1
            return
        n_nuevo = _Nodo(x)
        self.ult.prox = n_nuevo
        self.len += 1
        return

    def extend(self, lista: 'ListaDoblementeEnlazada') -> None:
        self.ult.prox = lista.prim
        self.len += lista.len
        return
