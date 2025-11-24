from typing import Any

class Grafo1:
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
    
class Grafo:
    """Conjunto de vértices (o nodos) y un conjunto de aristas (o arcos, o relaciones)."""
    def __init__(self) -> None:
        """Crea un grafo vacio."""
        self.adjacencias: dict{set} = {} 

    def add_node(self, vertice: Any) -> None:
        """Agrega un nodo al grafo."""
        if vertice not in self.adjacencias:
            self.adjacencias[vertice] = set()
        else:
            print(f"El vertice {vertice} ya existe.")
        return

    def add_edge(self, vertice1: Any, vertice2: Any) -> None:
        """Agrega una arista entre los vertices 1 y 2 pasados como argumento."""
        self.add_node(vertice1)
        self.add_node(vertice2)
        self.adjacencias[vertice1].add(vertice2)
        self.adjacencias[vertice2].add(vertice1)
        return
    
    def get_adjacent(self, vertice: Any) -> list[Any]:
        """Devuelve una lista de todos los vertices adyacentes al vetice pasado como argumento."""
        return list(self.adjacencias[vertice])

    def get_nodes(self) -> list[Any]:
        """Devuelve una lista con todos los vertices del grafo."""
        return list(self.adjacencias)

    def remove_node(self, vertice: Any) -> None:
        """Remueve el vertice (si existe) y tambien sus aristas adyacentes."""
        if vertice in self.adjacencias:
            for vecino in self.adjacencias[vertice]:
                self.adjacencias[vecino].remove(vertice)
            self.adjacencias.pop(vertice)
        else:
            print("El vertice no se encuentra en el grafo.")
        return

    def remove_edge(self, vertice1: Any, vertice2: Any) -> None:
        """Remueve (si es que existe) la arista entre el vertice1 y el vertice2."""
        if self.is_node(vertice1) in self.is_node(vertice2):
            if self.are_adyacent(vertice1, vertice2): # Se puede omitir esta validacion, ya que el metodo .discard() no falla si estos no son adjacentes.
                self.adjacencias[vertice2].discard(vertice1)
                self.adjacencias[vertice1].discard(vertice2)
        return

    def are_adyacent(self, vertice1: Any, vertice2: Any) -> bool:
        """Devuelve True si los vertices son adyacentes, de lo contrario devuelve False."""
        if vertice1 in self.adjacencias[vertice2]: # Al ser grafos simples, puedo preguntar por cualquiera de los vertices
            return True
        return False

    def is_node(self, vertice) -> bool:
        """Devuelve True si el vertice pertenece al grafo, False de lo contrario."""
        if vertice in self.adjacencias:
            return True
        return False

## Ejercicio 5 ##################################################################################################################
    def __eq__(self, G: 'Grafo') -> bool:
        """Permite comparar grafos por igualdad."""
        if not isinstance(G, Grafo):
            return False
        return self.adjacencias == G.adjacencias
        
        # if len(self.adjacencias) != len(G.adjacencias):
        #     return False
        # for vert_ext in G.adjacencias:
        #     if vert_ext not in self.adjacencias:
        #         return False
        #     if G.adjacencias[vert_ext] != self.adjacencias[vert_ext]:
        #         return False
        # return True
                

## Ejercicio 2 ##################################################################################################################
def get_edges(G: Grafo) -> list[str]:
    """Devuelve las aristas del grafo."""
    edges: set[set] = set()
    for v1 in G.get_nodes():
        for v2 in G.adjacencias[v1]:
            arista = frozenset({v1, v2})
            edges.add(arista)
    return [set(x) for x in list(edges)]

## Ejercicio 3 ##################################################################################################################
def is_subgraph(G: Grafo, H: Grafo) -> bool:
    """Devuelve true si H es un sub-grafo de G. De lo contrario devuelve False."""
    for vh in H.adjacencias:
        if vh not in G.adjacencias:
            return False
        for ah in H.adjacencias[vh]:
            if ah not in G.adjacencias[vh]:
                return False
    return True

## Ejercicio 4 ##################################################################################################################
def induce(G: Grafo | None, U: set) -> Grafo | None:
    """Devuelve un grafo G inducido por el conjunto U."""
    if G is None:
        return
    inducido = Grafo()    
    for vertice in U:
        inducido.add_node(vertice)
        if vertice in G.adjacencias:
            for v2 in G.adjacencias[vertice]:
                if v2 in U:
                    inducido.add_edge(vertice, v2)
    return inducido

## Ejercicio 6 ##################################################################################################################
def is_induced_subgraph(G: Grafo, H: Grafo) -> bool:
    """Devuelve true si H es un sub-grafo inducido de G para algun conjunto de vertices."""
    if not is_subgraph(G, H):
        return False
    vertices_h = set(H.adjacencias.keys())
    for vertice in H.adjacencias:
        aristas_h = H.adjacencias[vertice]
        aristas_g = G.adjacencias[vertice]
        comunes = vertices_h & aristas_g
        if aristas_h != comunes:
            return False
    return True

## Ejercicio 7 ##################################################################################################################
def is_complete(G: Grafo | None) -> bool | None:
    """Devuelve true si un grafo es completo, false de lo contrario."""
    if G is None:
        return
    conexiones = len(G.adjacencias.keys()) - 1 
    for vertice in G.adjacencias:
        if len(G.adjacencias[vertice]) != conexiones:
            return False
    return True

## Ejercicio 8 ##################################################################################################################
def subsets_size_k(l: list, k: int) -> list[set] | None:
    if not l:
        return None
    if k == 0:
        return []
    if len(l) == 0:
        pass
    


def has_clique(G: Grafo, k: int) -> bool:
    pass


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
