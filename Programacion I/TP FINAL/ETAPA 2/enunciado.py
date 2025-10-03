"""
7- Definir una clase Consumidor que tenga los siguientes

Atributos:

    submission_id: Identificador único del consumidor.

    age: Rango de edad (str).

    gender: Género (str).

    cups: Número de tazas que consume por día (str).

    where_drink: Lugares donde consume café (list[str]).

    favorite: Café preferido (str).

    roast_level: Nivel de tueste (str).

    caffeine: Tipo de cafeína (str).

    education_level: Nivel de educación (str).

    employment_status: Estado o situación laboral (str).

Métodos:

    __init__: Para inicializar los atributos.

    __str__: Para representar al consumidor de manera legible.

Complete el siguiente código. Agregue todos los argumentos que necesite a los métodos.
"""
class Consumidor:

  def __init__(self, submission_id, age, gender,cups, where_drink, favorite, roast_level, caffeine, education_level, employment_status):
    self.submission_id = submission_id
    self.age = age
    self.gender = gender
    self.cups = cups
    self.where_drink = where_drink
    self.favorite = favorite
    self.roast_level = roast_level
    self.caffeine = caffeine
    self.education_level = education_level
    self.employment_status = employment_status

  def __str__(self):
        return (f"Consumidor ID: {self.submission_id}\n"
                f"Género: {self.gender}\n"
                f"Edad: {self.age}\n"
                f"Tazas diarias: {self.cups}\n"
                f"Lugar de consumo: {self.where_drink}\n"
                f"Tipo favorito: {self.favorite}")

"""
8- Implemente una función llamada cargar_consumidores que reciba como argumento 
el nombre del archivo de la encuesta y devuelva un diccionario donde la clave sea el 
submission_id (ID del consumidor) y el valor sea una instancia de la clase Consumidor.
"""
import csv

def cargar_consumidores(archivo:str) -> dict[str,'Consumidor']:
  
  Consumidores = {}
  
  
  with open(archivo, 'r', encoding='utf-8') as resultados_encuesta:
    lector = csv.DictReader(resultados_encuesta)

    for fila in lector:
        consumidor_n = Consumidor(fila['submission_id'],
                                  fila['age'], 
                                  fila['gender'], 
                                  fila['cups'], 
                                  fila['where_drink'], 
                                  fila['favorite'], 
                                  fila['roast_level'], 
                                  fila['caffeine'], 
                                  fila['education_level'], 
                                  fila['employment_status']
                                  )
        identificador = fila['submission_id']
        Consumidores[identificador] = consumidor_n
  
  return Consumidores

Consumidores = cargar_consumidores("C:/Users/fedew/Desktop/IA/Programacion I/TP FINAL/ETAPA 0/coffee_survey.csv")

"""
9- Implemente una función llamada filtrar_por_atributo_valor que reciba un diccionario de 
consumidores como el creado en el punto anterior, un nombre de atributo 
(cualquiera de los atributos presentes en la clase Consumidor) y un valor de dicho atributo 
como argumentos. La función debe recorrer el diccionario y filtrar los consumidores, 
devolviendo otro diccionario cuyos consumidores hayan pasado el filtro aplicado.
"""

def filtrar_por_atributo_valor(cons:dict[str,'Consumidor'], atributo:str, valor:str) -> dict[str,'Consumidor']:
   
  consumidores_filtrados = {}
  atributos = [
                "submission_id",
                "age",
                "gender",
                "cups",
                "where_drink",
                "favorite",
                "roast_level",
                "caffeine",
                "education_level",
                "employment_status"
              ]
  while True:
    if atributo not in atributos:
      atributo = input(f"Ingrese un atributo correcto, alguno de la siguiente lista:\t{atributos}")
    else:
       break
    
  for identificador, fila in cons.items():
     if getattr(fila, atributo) == valor:
        consumidores_filtrados[identificador] = fila

  return consumidores_filtrados

filtrados = filtrar_por_atributo_valor(Consumidores, "gender", "Latte")

for c in filtrados.values():
  print(c.submission_id, c.favorite)
  pass