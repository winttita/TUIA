#!/bin/python3
## Ejercicio 1 ######################################################################################
def contar_ocurrencias(l: list[int], n: int) -> int:
    if not l:
        return 0
    if n == l[0]:
        return 1 + contar_ocurrencias(l[1:], n)
    else:
        return contar_ocurrencias(l[1:], n)

# print(contar_ocurrencias([1,2,3,3,3,5,3,6,7,3,3], 3))

## Ejercicio 2 ######################################################################################
def f(n: int)-> None:
    for i in range(n): # O(n)
        print(f"Elemento {i}")
        for j in range(1, n + 1): # O(n + 1) = O(n)
            print(f"Sub-elemento {j} en la iteración {i}")
    for i in range(3,0,-1): # O(1) constante
        print(i)
    print("Salimos de la función!")
# La complejidad total del algoritmo es # O(n^2)

## Ejercicio 3 ######################################################################################
class Evento:

    def __init__(self,
    cod_evento: str,
    nombre: str,
    fecha: str,
    hora: str,
    capacidad: int
    ):
        self.cod_evento = cod_evento
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.capacidad = capacidad

    def __str__(self) -> str:
        return f"Codigo: {str(self.cod_evento)}, Nombre: {str(self.nombre)}, Fecha: {str(self.fecha)}, Capacidad: {str(self.capacidad)}"

class ReservaEvento:

    def __init__(self, dni_cliente: str, nombre_cliente: str, evento: Evento, nro_asist: int):
        self.dni_cliente = dni_cliente
        self.nombre_cliente = nombre_cliente
        self.evento = evento
        self.nro_asist = nro_asist

    def __str__(self) -> str:
        return f"DNI cliente: {str(self.dni_cliente)}, Nombre del Cliente: {str(self.nombre_cliente)}, Evento: {self.evento.__str__()}"

class SistemaEventos:

    def __init__(self):
        self.eventos = {}
        self.reservas = {}

    def agregar_evento(self, evento: Evento) -> None:
        if evento.cod_evento not in self.eventos:
            self.eventos[evento.cod_evento] = evento

    def eliminar_evento(self, cod_evento: str) -> None:
        if cod_evento in self.eventos:
            self.eventos.pop[cod_evento]
        if cod_evento in self.reservas:
            self.reservas.pop[cod_evento]

    def mostrar_evento(self) -> None:
        print("Los eventos disponibles en el sistema son: ")
        for evento in self.eventos.values():
            print("\n", evento)

    def devolver_capacidad_restante(self, codigo: str) -> int:
        if codigo in self.reservas.keys():
            cant_personas = 0
            for asist in self.reservas.nro_asist:
                cant_personas += 1
            return self.reservas.evento.capacidad - cant_personas

    def crear_reserva(self, dni_cliente: str, nombre_cliente: str, cod_evento: str, cant_lugares: int) -> None:
        if cod_evento not in self.eventos.keys():
            print(f"El evento {cod_evento} no es valido.")
            return None
        if cant_lugares > devolver_capacidad_restante(cod_evento):
            print(f"La cantidad maxima de reservas dispoibles es: {devolver_capacidad_restante(cod_evento)}")
            return None
        reservado = ReservaEvento(dni_cliente, nombre_cliente, self.eventos.get(cod_evento), cant_lugares)
        if cod_evento not in self.reservas.keys():
            self.reservas[cod_evento] = []
        self.reservas[cod_evento].append(reservado)

    def eliminar_reserva(self, dni_cliente, cod_evento) -> None:
        if cod_evento in self.reservas.keys():
            for reserva in self.reservas[cod_evento]:
                if reserva.dni_cliente == dni_cliente:
                    self.reservas[cod_evento].remove(reserva)
                    break    
        else:
            print(f"El evento {cod_evento} no es un evento reservado aun.")
            return None
