from typing import Any

class Grafo:
    """Conjunto de vértices (o nodos) y un conjunto de aristas (o arcos, o relaciones)."""
    def __init__(self) -> None:
        """Crea un grafo vacio."""
        self.vertices = [] #Lista de vertices
        self.aristas = {} #Diccionario donde la clave es un vertice y el valor una lista con vertices con los que este forma una arista 

    def add_node(self, vertice: Any) -> None:
        """Agrega un nodo al grafo."""
        if vertice not in self.vertices:
            self.vertices.append(vertice)
            self.aristas[vertice] = []
        return

    def add_edge(self, vertice1: Any, vertice2: Any) -> None:
        """Agrega una arista entre los vertices 1 y 2 pasados como argumento."""
        self.add_node(vertice1)
        self.add_node(vertice2)
        if vertice1 not in self.aristas[vertice2]:
            self.aristas[vertice1].append(vertice2)
        if vertice2 not in self.aristas[vertice1]:
            self.aristas[vertice2].append(vertice1)
        return
    
    def get_adjacent(self, vertice: Any) -> list[Any]:
        """Devuelve una lista de todos los vertices adyacentes al vetice pasado como argumento."""
        return self.aristas[vertice]

    def get_nodes(self) -> list[Any]:
        """Devuelve una lista con todos los vertices del grafo."""
        return self.vertices

    def remove_node(self, vertice: Any) -> None:
        """Remueve el vertice (si existe) y tambien sus aristas adyacentes."""
        if vertice in self.vertices:
            self.vertices.remove(vertice)
            for vert in self.aristas[vertice]:
                self.aristas[vert].remove(vertice)
            self.aristas.pop[vertice]
        else:
            print("El vertice no se encuentra en el grafo.")
        return

    def remove_edge(self, vertice1: Any, vertice2: Any) -> None:
        """Remueve (si es que existe) la arista entre el vertice1 y el vertice2."""
        if vertice1 in self.aristas[vertice2]:
            if self.are_adyacent(vertice1, vertice2):
                self.aristas[vertice2].remove(vertice1)
                self.aristas[vertice1].remove(vertice2)
        return

    def are_adyacent(self, vertice1: Any, vertice2: Any) -> bool:
        """Devuelve True si los vertices son adyacentes, de lo contrario devuelve False."""
        if vertice1 in self.aristas[vertice2]: # Al ser grafos simples, puedo preguntar por cualquiera de los vertices
            return True
        return False

    def is_node(self, vertice) -> bool:
        """Devuelve True si el vertice pertenece al grafo, False de lo contrario."""
        if vertice in self.vertices:
            return True
        return False

    def get_edges
        
# Ejemplo de uso
grafo = Grafo()
grafo.add_node("A")
grafo.add_node("B")
grafo.add_node("C")
grafo.add_edge("A", "B")
grafo.add_edge("B", "C")
grafo.add_edge("C", "A")
print("Vértices:", grafo.get_nodes())
print("Aristas de A:", grafo.get_adjacent("A"))
print("Aristas de B:", grafo.get_adjacent("B"))
print("Aristas de C:", grafo.get_adjacent("C"))
