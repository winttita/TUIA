from typing import Any


class BinaryTree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

    ## Ejercicio 2 ##################################################################################################################
    def nodos(self) -> int:
        """Devuelve la cantidad de nodos del arbol."""
        total_nodos = 1
        if self.left is not None:
            total_nodos += self.left.nodos()
        if self.right is not None:
            total_nodos += self.right.nodos()
        return total_nodos

    def menor_mayor(self) -> tuple:
        """Devuelve el menor y el mayor elemento del arbol en una tupla."""
        mayor = self.cargo
        menor = self.cargo
        if self.left is not None and isinstance(self.left, BinaryTree):
            (menor_izq, mayor_izq) = self.left.menor_mayor()
            if menor_izq < menor:
                menor = menor_izq
            if mayor_izq > mayor:
                mayor = mayor_izq

        if self.right is not None and isinstance(self.right, BinaryTree):
            (menor_der, mayor_der) = self.right.menor_mayor()
            if menor_der < menor:
                menor = menor_der
            if mayor_der > mayor:
                mayor = mayor_der
        return (menor, mayor)

    def buscar(self, elemento: Any) -> bool:
        """Busca si un elemento esta o no en el arbol."""
        if self.cargo == elemento:
            return True
        valor_der = False
        valor_izq = False
        if self.left is not None and isinstance(self.left, BinaryTree):
            valor_izq = self.left.buscar(elemento)
        if self.right is not None and isinstance(self.right, BinaryTree):
            valor_der = self.right.buscar(elemento)
        if valor_der or valor_izq:
            return True
        return False

    def altura(self) -> int:
        """Calcula la altura del arbol, es decir, la distancia de la hoja mas lejana hasta la raiz."""
        pos_izq = 0
        pos_der = 0
        if self.left is not None:
            pos_izq += 1 + self.left.altura()
        if self.right is not None:
            pos_der += 1 + self.right.altura()
        altura = max(pos_der, pos_izq)
        return altura
        
## Ejercicio 1 ##################################################################################################################
arbol1 = BinaryTree(2)  # SOLO TIENE LA RAIZ
arbol2 = BinaryTree(2, BinaryTree(3, BinaryTree(4, BinaryTree(5))))  # h = 3. Analogia con una lista de rango 3
arbol3 = BinaryTree(2, BinaryTree(3, BinaryTree(5)))  # h = 1
