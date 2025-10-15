## Ejercicio 1 ######################################################################################
def contar_pacientes_rec(pacientes: list[dict[str, str]], sintoma: str) -> int:
    
    paciente_act = pacientes[0]

    if not pacientes:
        return 0
    if sintoma in pacientes[0]["Sintomas"]:
        return 1 + contar_pacientes_rec(pacientes[1:], sintoma)
    else:
        return contar_pacientes_rec(pacientes[1:], sintoma)

def contar_pacientes_itera(pacientes: list[dict[str, str]], sintoma: str) -> int:
    cant = 0
    for paciente in pacientes:
        if sintoma in paciente["Sintomas"]:
            cant += 1
    return cant

## Ejercicio 2 ######################################################################################
def registrar_pacientes(n: int)-> list[dict[str,str]]:
    lista_pac = []
    datos = ["Nombre","DNI","Síntomas"]
    for i in range(n): #O(n) depende de la lista
        print(f"Registrando paciente {i + 1}")
        pac = {}
        for j in range(3): #O(1) ya que siempre se ejecutara 3 veces
            pac[datos[i]] = input(f"Ingrese {datos[i]} para paciente {i + 1}:")
            lista_pac.append(pac)
    return lista_pac

    # La complejidad total del algoritmo es: 3n + 6 = O(n)

## Ejercicio 3 ######################################################################################
class Paciente:
    def __init__(self, dni: str, nombre: str, edad: int, sintomas: str) -> None:
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.sintomas = sintomas
    
    def __str__(self) -> str:
        return f"Paciente: {self.nombre}\n Edad: {self.edad}\n DNI: {self.dni}\n Sintomas: {self.sintomas}"
    
class Hospital:
    def __init__(self) -> None:
        self.pacientes: dict[str, Paciente] = {}
    
    def agregar_paciente(self, paciente: Paciente) -> None:
        if paciente.dni not in self.pacientes:
            self.pacientes[paciente.dni] = paciente
            return
        else:
            print("El paciente ya se encuentra ingresado.")
            return
    
    def eliminar_paciente(self, dni: str) -> None:
        if dni in self.pacientes:
            self.pacientes.pop(dni)
            return
    
    def mostrar_pacientes(self) -> None:
        for paciente in self.pacientes.values():
            print(paciente)
    
    def contar_pacientes_con_sintoma(self, sintoma: str) -> int:
        cant = 0
        for paciente in self.pacientes.values():
            if sintoma in paciente.sintomas:
               cant += 1
        return cant

# Ejemplo de uso
hospital = Hospital()
# Creando pacientes
paciente1 = Paciente("12345678", "Juan Perez", 30, "fiebre, tos")
paciente2 = Paciente("87654321", "Maria Lopez", 25,"dolor de oidos, fiebre")
hospital.agregar_paciente(paciente1)
hospital.agregar_paciente(paciente2)
# Mostrando pacientes
hospital.mostrar_pacientes()
# Contando pacientes con fiebre
print("Pacientes con fiebre:", hospital.contar_pacientes_con_sintoma("fiebre"))
# Eliminando un paciente
hospital.eliminar_paciente("12345678")