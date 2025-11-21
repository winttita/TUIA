## Ejercicio de SISTEMA DE CALIFICACION DE ALUMNOS (POO) ################################################
class Alumno:
    def __init__(self, legajo: str, nombre: str) -> None:
        self.legajo = legajo
        self.nombre = nombre
        self.calificaciones: dict[str, float] = {}
        self.promedio: float = 0 # Atributo donde se guarda el promedio general del alumno
        
    def __str__(self) -> str:
        return f"Legajo: {self.legajo} | Nombre: {self.nombre} | Promedio: {self.promedio:.2f}"
    
    def agregar_calificaciones(self, materia: str, nota: float) -> None:
        if materia not in self.calificaciones:
            self.calificaciones[materia] = nota
            return
        else:
            print(f"La materia {materia} ya se encuentra con una nota cargada.")
            return
    
    def calcular_promedio(self) -> float:
        if not self.calificaciones:
            return 0
        else:
            self.promedio = sum(self.calificaciones.values()) / len(self.calificaciones)
            return self.promedio
    
class RegistroAcademico:
    def __init__(self) -> None:
        self.alumnos: dict[str, Alumno] = {}

    def matricular_alumno(self, alumno: Alumno) -> None:
        if alumno.legajo not in self.alumnos:
            self.alumnos[alumno.legajo] = alumno
            return
        else:
            print(f"El legajo {alumno.legajo} ya se encuentra cargado.")
            return
    
    def cargar_nota(self, legajo: str, materia: str, nota: float) -> None:
        if legajo not in self.alumnos:
            print(f"El legajo {legajo} no se encuentra cargado.")
            return
        else:
            self.alumnos[legajo].calificaciones[materia] = nota
            self.alumnos[legajo].calcular_promedio()
            #alumno_act = self.alumnos[legajo]
            #alumno_act.agregar_calificaciones(materia, nota)
            return
        
    def obtener_promedio_general(self) -> float:
        suma = 0.0
        for alumno in self.alumnos.values():
            suma += alumno.calcular_promedio()
        if not self.alumnos:
            return 0
        else:
            return suma / len(self.alumnos)
    
    def mostrar_registro(self) -> None:
        for alumno in self.alumnos.values():
            print(alumno)

# Crear un registro académico
registro = RegistroAcademico()

# Crear y matricular alumnos
alumno1 = Alumno("110-24", "Laura Paez")
alumno2 = Alumno("112-24", "Marcos Diaz")
registro.matricular_alumno(alumno1)
registro.matricular_alumno(alumno2)

# Cargar notas
registro.cargar_nota("110-24", "Programación II", 8.5)
registro.cargar_nota("110-24", "Bases de Datos", 7.0)
registro.cargar_nota("112-24", "Programación II", 9.0)

# Mostrar el registro
registro.mostrar_registro()

# Obtener promedio general
promedio_curso = registro.obtener_promedio_general()
print(f"\nPromedio general del curso: {promedio_curso:.2f}")