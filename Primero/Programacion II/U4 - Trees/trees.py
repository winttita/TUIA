from typing import Any


def menor(item1: Any, item2: Any) -> Any:
    """Devuelve menor elemento entre dos valores."""
    if item1 > item2:
        return item2
    else:
        return item1


def mayor(item1: Any, item2: Any) -> Any:
    """Devuelve mayor elemento entre dos valores."""
    if item1 < item2:
        return item2
    else:
        return item1


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

    ## Ejercicio 3 ##################################################################################################################

    ## Recursivos ###############################################################################################################
    def preOrder(self) -> None:
        """Recorre el arbol nodo por nodo recursivamente en modo PreOrder.
        Primero la raiz, luego el hijo izquierdo y por ultimo el derecho (si es que los hay)."""

        print(self.cargo)

        if self.left is not None:
            self.left.preOrder()

        if self.right is not None:
            self.right.preOrder()

    def inOrder(self) -> None:
        """Recorre el arbol nodo por nodo recursivamente en modo inOrder.
        Primero el hijo izquierdo, luego la raiz y por ultimo el derecho (si es que los hay)."""

        if self.left is not None:
            self.left.inOrder()

        print(self.cargo)

        if self.right is not None:
            self.right.inOrder()

    def posOrder(self) -> None:
        """Recorre el arbol nodo por nodo recursivamente en modo posOrder.
        Primero el hijo izquierdo, luego el derecho (si es que los hay) y por ultimo la raiz."""

        if self.left is not None:
            self.left.posOrder()

        if self.right is not None:
            self.right.posOrder()

        print(self.cargo)

    ## Iterativos ###############################################################################################################
    def preOrderIter(self) -> None:
        """Recorre el arbol nodo por nodo iterativamente en modo PreOrder.
        Primero la raiz, luego el hijo izquierdo y por ultimo el derecho (si es que los hay)."""
        stack = Stack()
        stack.push(self.cargo)
        while not stack.isEmpty():
            actual = stack.pop()
            pass

    def inOrderIter(self) -> None:
        """Recorre el arbol nodo por nodo iterativamente en modo inOrder.
        Primero el hijo izquierdo, luego la raiz y por ultimo el hijo derecho (si es que los hay)."""
        pass

    def posOrderIter(self) -> None:
        """Recorre el arbol nodo por nodo iterativamente en modo posOrder.
        Primero el hizo izquierdo, luego el derecho (si es que los hay) y por ultimo la raiz."""
        pass


## Ejercicio 1 ##################################################################################################################
arbol1 = BinaryTree(2)  # SOLO TIENE LA RAIZ
arbol2 = BinaryTree(
    2, BinaryTree(3, BinaryTree(4, BinaryTree(5)))
)  # h = 3. Analogia con una lista de rango 3
arbol3 = BinaryTree(2, BinaryTree(3, BinaryTree(7), BinaryTree(15, BinaryTree(1))))
arbol4 = BinaryTree(
    50,
    BinaryTree(2, BinaryTree(3, BinaryTree(7), BinaryTree(15, BinaryTree(1)))),
    BinaryTree(20, BinaryTree(18), BinaryTree(25, BinaryTree(22))),
)


## Ejercicio 4 ##################################################################################################################
def copy(arbol: BinaryTree) -> BinaryTree | None:
    """Recibe un arbol y devuelve otro arbol identico (copiado) al que es pasado como parametro."""
    arbol2 = BinaryTree(arbol.cargo, arbol.left, arbol.right)
    return arbol2


## Ejercicio 5 ##################################################################################################################
def invertir(arbol: BinaryTree) -> None:
    """Intercambia los hijos derechos por los hijos izquierdos en todos los nodos."""
    if arbol is None:
        return
    arbol.left, arbol.right = arbol.right, arbol.left
    if arbol.left is not None:
        invertir(arbol.left)
    if arbol.right is not None:
        invertir(arbol.right)
    return


## Ejercicio 6 ##################################################################################################################
def sumatoria(arbol: BinaryTree) -> int:
    """Recibe un arbol binario que contiene numeros en sus nodos y devuelve la suma de todos estos."""
    total = arbol.cargo
    if arbol.left is not None:
        total += sumatoria(arbol.left)
    if arbol.right is not None:
        total += sumatoria(arbol.right)
    return total


## Ejercicio 7 ##################################################################################################################
def sumatoria_rango(
    arbol: BinaryTree, M: int, inicio: int, final: int, nivel: int = 0
) -> int:
    """Recibe un árbol binario A cuyos nodos contienen números y
    que dado un entero M, una clave inicio y una clave final, calcula la suma de todos los
    números del árbol que se encuentren entre inicio y final, a lo sumo hasta el nivel M."""
    suma = 0
    if nivel > M:
        return 0
    if inicio <= arbol.cargo <= final:
        suma = arbol.cargo
    if arbol.left is not None:
        suma += sumatoria_rango(arbol.left, M, inicio, final, nivel + 1)
    if arbol.right is not None:
        suma += sumatoria_rango(arbol.right, M, inicio, final, nivel + 1)
    return suma


## Ejercicio 9 ##################################################################################################################
class BSTree(BinaryTree):
    """Clase particular de Arbol Binario donde en cada nodo, el elemento de la izquierda es menor y el derecha mayor que el."""

    def __init__(self, cargo: Any, left: Any = None, right: Any = None):
        super().__init__(cargo, left, right)

    def menor_mayor(self) -> tuple:
        """Devuelve el menor y el mayor elemento del arbol."""
        nodo_act = self.cargo
        while nodo_act.left is not None:
            nodo_act = nodo_act.left
        menor = nodo_act
        while nodo_act.right is not None:
            nodo_act = nodo_act.right
        mayor= nodo_act

        return menor, mayor

    def buscar(self, elemento) -> bool:
        """Si el elemento esta en el arbol devuelve True sino, False."""
        if elemento == self.cargo:
            return True
        izq = False
        der = False
        if elemento > self.cargo and self.right is not None:
            der = self.right.buscar(elemento)
        if elemento < self.cargo and self.left is not None:
            izq = self.left.buscar(elemento)

        return izq or der

    def insertar(self, item: Any) -> None:
        """Inserta el item."""
        if item < self.cargo:
            if self.left is None:
                self.left = BSTree(item)
            else:
                self.right.insertar(item)
        elif item > self.cargo:
            if self.right is None:
                self.right = BSTree(item)
            else:
                self.right.insertar(item)
        return
