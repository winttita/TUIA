from typing import Any

## Ejercicio 1 ##################################################################################################################
class BinaryTree:
    def __init__(self, cargo, left = None, right = None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

# arbol1 = BinaryTree(2) # SOLO TIENE LA RAIZ
# arbol2 = BinaryTree(2, BinaryTree(3, BinaryTree(4, 5))) # h = 3. Analogia con una lista de rango 3
# arbol3 = BinaryTree(2, BinaryTree(3, 5)) # h = 1

## Ejercicio 2 ##################################################################################################################
    def nodos(self):
        """Devuelve la cantidad de nodos del arbol."""
        pass
