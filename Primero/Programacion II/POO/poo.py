class Time :
    def __init__ ( self , hh : int , mm : int , ss : int ) -> None :
        self . hours = hh
        self . minutes = mm
        self . seconds = ss
    
    def increment ( self , seconds : int ) -> None :
        self . seconds = seconds + self . seconds
        
        while self . seconds >= 60:
            self . seconds = self . seconds - 60
            self . minutes = self . minutes + 1
        
        while self . minutes >= 60:
            self . minutes = self . minutes - 60
            self . hours = self . hours + 1

# Ejercicio 1 ## 1.1 #######################################################

class Point:
    """ representación de un punto en un plano cartesiano 2D """
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __eq__(self, other) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    ## Ejercicio 2 #######################################################
    def distancia(self, other: 'Point') -> float:
        dist = ((other.x - self.x) **2 + (other.y - self.y) ** 2) ** 0.5
        return dist
    
class Rectangle:
    def __init__(self, width: float, height: float, corner: Point) -> None:
        self.width = width
        self.height = height
        self.corner = corner

    def __str__(self) -> str:
        return '( width:' + str(self.width) + ', height:' + str(self.height) + ', corner:'+ str(self.corner) + ')'

    def __eq__(self, other: 'Rectangle') -> bool:
        if not insistance(other, Rectangle):
            return NotImplemented
        return self.width == other.width and self.height == other.heiht and self.corner.__eq__(other.corner)

## 1.2 #######################################################

import copy as c

def mover_rectangulo_mod(rect: 'Rectangle', dx: float, dy: float) -> None:

    rect.corner.x += dx
    rect.corner.y += dy

def mover_rectangulo_pura(rect: 'Rectangle', dx: float, dy: float) -> Rectangle:

    aux = c.deepcopy(rect)
    aux.corner.x += dx
    aux.corner.y += dy

    return aux

## 1.3 #######################################################

    # punto1 = Point(10, 20)
    # punto2 = Point(20, 30)

    # rec1 = Rectangle(20, 30, punto1)
    # rec2 = Rectangle(20, 40, punto2)

    # punto3 = punto1

## Ejercicio 3 #############################################################
class Automovil:
    def __init__(self, patente: str, marca: str, km = 0.0, nafta = 0.0) -> None:
        self.patente = patente
        self.marca = marca
        self.km = km
        self.nafta = nafta

    def avanzar(self, km_prox: float) -> None:
        self.km += km_prox
        if self.nafta < km_prox * 0.088:
            print("Es necesario cargar nafta para recorrer la cantidad deseadad de km.")
        else:
            self.nafta -= km_prox * 0.088 

    def cargar_nafta(self, carga_nafta) -> None:
        self.nafta += carga_nafta

## Ejercicio 4 #############################################################
class Robot:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.hist = []
        
    def mueve(self, orden: str) -> None:
        """
        Metodo utilizado para que el robot avance (1 unidad por vez), toma A: incremento en las x, R: decremento en las x,
        I: incremento en las y, D: decremento en las y.
        """
        match orden.upper():
            case 'A':
                self.x += 1
            case 'R':
                self.x -= 1
            case 'I':
                self.y += 1
            case 'D':
                self.y -= 1

    def posicion_actual(self) -> None:
        print(f"({self.x}, {self.y})")

    # mi_robot = Robot()
    # orden = input("Ingresa una orden: ")
    # while orden != 'fin':
    #     mi_robot.mueve(orden)
    #     mi_robot.posicion_actual()
    #     orden = input("Ingrese otra orden: ")
    
## Ejercicio 5 #############################################################
    def mueve_2(self, orden: str) -> None:
        ordenes = set("ARID")
        if set(orden.upper()).issubset(ordenes):
            print("La orden contiene caracteres invalidos. Reintente con A,R,I,D.")
            return
        else:
            for o in orden:
                match o.upper():
                    case 'A':
                        self.x += 1
                        self.hist.append('A') 
                    case 'R':
                        self.x -= 1
                        self.hist.append('R')
                    case 'I':
                        self.y += 1
                        self.hist.append('I')
                    case 'D':
                        self.y -= 1
                        self.hist.append('D')

    def obtener_historico_de_movimientos(self) -> None:
        print(self.hist)
    
    def como_volver(self) -> None:
        para_volver = []
        for m in self.hist:
            match m:
                    case 'A':
                        para_volver.append('R') 
                    case 'R':
                        para_volver.append('A')
                    case 'I':
                        para_volver.append('D')
                    case 'D':
                        para_volver.append('I')

        print(f"Para voler al origen (0, 0), ejecuta las siguientes ordenes: {para_volver[::-1]}")

## Ejercicio 6 #############################################################

class Materia:
    def __init__(self, codigo: str, nombre: str, creditos: int ) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos

    def __str__(self) -> str:
        return f"{self.codigo} {self.nombre} ({self.creditos})"
    
class Carrera:
    def __init__(self, materias: list[Materia]) -> None:
        self.materias = materias
        self.aprobadas: dict[str, (Materia, int)] = {}

    def __str__(self) -> str:
        aprobadas = ""
        acum = 0
        for cod, (materia, nota) in self.aprobadas.items():
            aprobadas += str(cod) + " " + str(materia.nombre) + " (" + str(nota) + ") "
            acum += nota
        prom = "N/A" if not self.aprobadas else ( acum / len(self.aprobadas))
        return f"Creditos: {'0' if not self.aprobadas else acum} -- Promedio: {prom} -- Materias Aprobadas: {aprobadas}"
    
    def aprobar(self, cod: str, nota: int) -> None:
        for materia in self.materias:
            if cod == materia.codigo:
                self.aprobadas[cod] = (materia, nota)
                return
        print(f"La materia {cod} no es parte del plan de estudios.")
 
    # analisis2 = Materia("61.03", "Análisis 2", 8)
    # fisica2 = Materia("62.01", "Física 2", 8)
    # algo1 = Materia("75.40", "Algoritmos 1", 6)
    # c = Carrera([analisis2, fisica2, algo1])
    # print(c)
    # c.aprobar("95.14", 7)
    # c.aprobar("75.40", 10)
    # c.aprobar("62.01", 7)
    # print(c)

## Ejercico 7 #############################################################

class Cosa:
    def __init__(self, valor: any) -> None:
        self.valor = valor

    def __str__(self) -> str:
        return f"{self.valor}"

class Coleccion:
    def __init__(self) -> None:
        self.coleccion = []

    def agregar_cosa(self, cosa: Cosa):
        self.coleccion.append(cosa)

    def __str__(self) -> str:
        muestra = ""
        for cosa in self.coleccion:
            muestra += str(cosa) + " "
        return muestra

    # cosa = Cosa("Cosa 1")
    # cosa2 = Cosa("Cosa 2")
    # coleccion = Coleccion()
    # coleccion.agregar_cosa(cosa)

## Ejercicio 8 #############################################################

class Animales:
    def speak(self) -> None:
        print("Soy un Animal.")

    def talk(self) -> None:
        print(f"{self.speak}")
        
class Mamiferos(Animales):
    def speak(self) -> str:
        print("Soy un Mamifero.")

class Felinos(Mamiferos):
    def speak(self) -> str:
        print("Soy un Felino.")

class Canidos(Mamiferos):
    def speak(self) -> str:
        print("Soy un Canido.")

class Primates(Mamiferos):
    def speak(self) -> str:
        print("Soy un Primate.")

class Hacker(Primates):
    pass

## Ejercicio 9 #############################################################
class Entidad:
    def __init__(self, vida_inicial: int):
        self.vida = vida_inicial

class Enemigo(Entidad):
    pass

class Jugador(Entidad):
    def __init__(self, vida_inicial: int):
        super().__init__(vida_inicial)
        self.enemigos_golpeados = []

    def golpeado(self, cuanto: int):
        self.vida -= cuanto
    
    def golpear(self, enemigo: Enemigo, cuanto: int):
        self.golpeado(cuanto)
        self.enemigos_golpeados.append(enemigo)

## Ejercicio 10 #############################################################

class Billetera:
    porcentaje_reintegro = 0.3
    tope_reintegro = 5000

    def __init__(self, nro_cuenta: str) -> None:
        self.nro_cuenta = nro_cuenta
        self.saldo = 0
        self.reintegro_restante = 5000

    def cargar(self, cantidad: float) -> None:
        self.saldo += cantidad

    def pagar(self, cantidad: float) -> None:
        if self.saldo * self.porcentaje_reintegro <= self.reintegro_restante:
            self.saldo -= cantidad - (cantidad * self.porcentaje_reintegro)
            self.reintegro_restante -= cantidad * self.porcentaje_reintegro
        else:
            self.saldo -= cantidad
            
    def monto_descuento_pendiente(self) -> None:
        if self.reintegro_restante > 0 :
            print(self.reintegro_restante)
        else:
            print("No dispone de un monto para descuento.")

    # cuenta = Billetera("1202")
    # cuenta.cargar(15000)
    # cuenta.pagar(15000)
    # cuenta.monto_descuento_pendiente()
