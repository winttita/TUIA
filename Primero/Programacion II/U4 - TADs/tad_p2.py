from typing import Any
## Ejercicio 1 ##################################################################################################################
class Stack:
    """Representa una pila con las operaciones de apilar, desapilar y verificar si esta vacia."""

    def __init__(self) -> None:
        """Crea una pila vacia"""
        self.items: list[] = []

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
    
    def isEmpty(self) -> bool:
        """Devuelve True si la pila esta vacı́a, y False si no."""
        if self.items:
            return False
        return True

    
