from typing import Any
from tad_p1 import ListaEnlazada

## Ejercicio 1 ##################################################################################################################
class Stack:
    """Representa un stack con las operaciones de apilar, desapilar y verificar si esta vacia."""

    def __init__(self) -> None:
        """Crea una pila vacia"""
        self.items: list[Any] = []

    def push(self, item: Any) -> None:
        """Agrega un item al stack"""
        self.items.append(item)
        return

    def pop(self) -> Any:
        """Desapila un elemento y lo devuelve. Si la pila esta vacı́a, imprime un mensaje de error y termina la ejecucion inmediatamente."""
        if self.isEmpty():
            print("La pila esta vacia")
            return
        return self.items.pop()
    
    def peek(self) -> Any:
        """Analogo al .pop(), este metodo devuelve el el ultimo elemento de la pila, sin sacarlo de esta (desapilarlo)."""
        if self.isEmpty():
            print("La pila esta vacia")
            return
        return self.items[-1]
        
    def isEmpty(self) -> bool:
        """Devuelve True si la pila esta vacı́a, y False si no."""
        if self.items:
            return False
        return True

## Ejercicio 2 ##################################################################################################################
class LinkedStack:
    """Representa un stack con las operaciones de apilar, desapilar y verificar si esta esta vacia. Implementamos con una ListaEnlazada"""

    def __init__(self) -> None:
        """Crea una pila vacia"""
        self.items = ListaEnlazada()
    
    def push(self, item: Any) -> None:
        """Agrega un item al stack"""
        self.item.append(item)
        return
    
    def pop(self) -> Any:
        """Desapila un elemento y lo devuelve. Si la pila esta vacı́a, imprime un mensaje de error y termina la ejecucion inmediatamente."""
        if self.items.is_empty():
            print("Error, la pila esta vacia.")
            return
        else:
            return self.items.pop() 
    
    def isEmpty(self) -> bool:
        """Devuelve True si la pila esta vacı́a, y False si no."""
        if self.items.prim is None:
            return True
        else:
            return False

## Ejercicio 3 ##################################################################################################################
class PilaConMaximo(Stack):

    def __init__(self) -> None:
        """Crea una pila vacia."""
        super().__init__()
        self.maximos = Stack()

    def push(self, item: int) -> None:
        """Agrega un item a la pila y ademas si este es mayor que el ultimo de la pila "Maximos", tambien lo agrega a esta ultima."""
        super().push(item)
        if self.maximos.isEmpty():
            self.maximos.push(item)
            return
        elif self.maximos.peek() < item:
            self.maximos.push(item)
            return
    
    def pop(self) -> Any:
        """Desapila un elemento y lo devuelve. Si la pila esta vacı́a, imprime un mensaje de error y termina la ejecucion inmediatamente."""
        return super().pop()
    
    def obtener_maximo(self) -> int:
        """Devuelve el item con valor maximo de la pila."""
        return self.maximos.pop()
