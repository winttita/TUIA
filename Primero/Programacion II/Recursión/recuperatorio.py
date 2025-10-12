## Ejercicio 1 ######################################################################################
def contar_pacientes_rec(pacientes: list[dict[str: str]], sintoma: str) -> int:
    """ funcion que recibe como parametros una lista de pacientes con sintomas, y un sintoma para que luego cuente
    cuantos pacientes poseen este ultimo. """
    
    paciente_act = pacientes[0]
    sintomas_paciente = paciente_act.get("Sintomas", "")
    sintomas_act = [sint.strip() for sint in sintomas_paciente.split(',')]
    """ Lo mismo que hacer un 
    for sint in sintomas_act.split(','):
        sintomas_list.append(sint.strip())
    """

    paciente_contado = 0
    if not pacientes:
        return 0
    else:
        paciente_contado = 1 if sintoma in sintomas_act else 0
    return paciente_contado + contar_pacientes_rec(pacientes[1:], sintoma)

## Ejercicio 2 ######################################################################################
def registrar_pacientes(n: int)-> list[dict[str,str]]:
    lista_pac = []
    datos = ["Nombre","DNI","Síntomas"]
    for i in range(n): #O(n)
        print(f"Registrando paciente {i + 1}")
        pac = {}
        for j in range(3): # O(1)
            pac[datos[i]] = input(f"Ingrese {datos[i]} para paciente {i + 1}:")
            lista_pac.append(pac)
    return lista_pac

    # La complejidad de este algoritmo es # O(n)

## Ejercicio 3 ######################################################################################
class Paciente:

    def __init__(self, dni: str, nombre: str, edad: int, sintomas: str) -> None:
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.sintomas = sintomas

    def __str__(self) -> str:
        return f"Paciente: {self.nombre}\n DNI: {self.dni}\n Edad: {self.edad}\n Sintomas: {self.sintomas}"
    
class Hospital:
    def __init__(self) -> None:
        self.pacientes: dict[str, Paciente] = {}
    
    def agregar_paciente(self, paciente: Paciente) -> None:
        self.pacientes[paciente.dni] = paciente
    
    def eliminar_paciente(self, DNI: str) -> None:
        if DNI in self.pacientes:
            self.pacientes.pop(DNI)
        else:
            print("Paciente no encontrado.")
    
    def mostrar_pacientes(self) -> None:
        for paciente in self.pacientes.values():
            print(paciente)
    
    def contar_pacientes_con_sintoma(self, sintoma: str) -> int:
        cant_pacientes = 0
        for paciente in self.pacientes.values():
            if sintoma.lower() in paciente.sintomas.lower():
                cant_pacientes += 1
        return cant_pacientes