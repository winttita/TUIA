"""
3- Analice la columna 'age' que indica el rango de edad del encuestado. 
¿Qué cantidad de los encuestados que brindaron esta información pertenecen a los
rangos '<18 years old', '18-24 years old', '25-34 years old', '35-44 years old',
'45-54 years old', '55-64 years old' y '>65 years old', respectivamente? 
Para responder a esta pregunta implemente una función contar_rangos_edad que
reciba el nombre del archivo de datos de la encuesta y devuelva un diccionario 
que le ayude a contar la cantidad de respuestas de cada rango etario.
"""
import csv

# Consigna 3: Analizar la columna 'age'
def contar_rangos_edad(archivo:str) -> dict[str,int]:

  conteo = {}

  with open(archivo, 'r', encoding='utf-8') as resultados_encuesta:
    lector = csv.DictReader(resultados_encuesta)

    for encuestado in lector:
      edad = encuestado['age']
      if encuestado['age'] in conteo:
        conteo[edad] += 1
      else:
        conteo[edad] = 1

  return conteo

#Prueba
print("Conteo de rangos de edad:", contar_rangos_edad("C:/Users/fedew/Desktop/IA/Programacion I/TP FINAL/ETAPA 0/coffee_survey.csv"))

#Respuesta:
#Conteo de rangos de edad: {'18-24 years old': 461, '25-34 years old': 1986, '35-44 years old': 960, '55-64 years old': 187, '<18 years old': 20, '>65 years old': 95, '45-54 years old': 302}

"""
4- Analice la columna 'where_drink' que indica dónde toman café los encuestados. 
¿Qué diferencia encuentra entre esta columna de la anterior? 
¿Qué cantidad de los encuestados que respondieron a esta pregunta toman 
el café 'On the go', 'At a cafe', 'At the office', 'At home', 
'None of these', respectivamente? 
Para responder a esta pregunta implemente una función contar_lugares_consumo 
que reciba el nombre del archivo de datos de la encuesta y devuelva un diccionario 
que le ayude a contar la cantidad de respuestas de cada lugar de consumo.
"""
# Consigna 4: Analizar la columna 'where_drink'
def contar_lugares_consumo(archivo:str) -> dict[str,int]:
  
  conteo = {}

  with open(archivo, 'r', encoding='utf-8') as resultados_encuesta:
    lector = csv.DictReader(resultados_encuesta)

    for encuestado in lector:
      lugares = encuestado['where_drink'].split(sep=", ")
      for lugar in lugares:
        if lugar in conteo:
          conteo[lugar] += 1
        else:
          conteo[lugar] = 1

  return conteo

# Prueba
#print("Conteo de lugares de consumo:", contar_lugares_consumo("C:/Users/fedew/Desktop/IA/Programacion I/TP FINAL/ETAPA 0/coffee_survey.csv"))

#Respuesta:
#Conteo de lugares de consumo: {'On the go': 705, 'At a cafe': 1170, 'At the office': 1430, 'At home': 3644, 'None of these': 36}

"""
5- Analicen los códigos propuestos para responder a las consignas 3 y 4. 
Son similares, ¿verdad? Proponga una función procesamiento_columna, que recibiendo el nombre 
del archivo y el nombre de la columna a analizar, sirva para resolver los dos casos anteriores. 
La función debe devolver un diccionario con las cantidades asociadas a cada uno de los valores posibles 
de las respuestas brindadas por los encuestados.
"""
# Consigna 5: Función procesamiento_columna
def procesamiento_columna(archivo: str, columna:str) -> dict[str,int]:

  conteo = {}

  with open(archivo, 'r', encoding='utf-8') as resultados_encuesta:
    lector = csv.DictReader(resultados_encuesta)

    for encuestado in lector:
      if columna == 'where_drink':
        lugares = encuestado['where_drink'].split(sep=", ")
        for lugar in lugares:
          if lugar in conteo:
            conteo[lugar] += 1
          else:
            conteo[lugar] = 1
      elif columna == 'age':
        edad = encuestado['age']
        if edad in conteo:
          conteo[edad] += 1
        else:
          conteo[edad] = 1
      else:
        print("Columna incorrecta.")
      

  return conteo

# Prueba

#print("\nConteo de rangos de edad:", procesamiento_columna("C:/Users/fedew/Desktop/IA/Programacion I/TP FINAL/ETAPA 0/coffee_survey.csv", 'age'))
#print("\nConteo de lugares de consumo:", procesamiento_columna("C:/Users/fedew/Desktop/IA/Programacion I/TP FINAL/ETAPA 0/coffee_survey.csv", 'where_drink'))

#Respuestas:
#Conteo de rangos de edad: {'18-24 years old': 461, '25-34 years old': 1986, '35-44 years old': 960, '55-64 years old': 187, '<18 years old': 20, '>65 years old': 95, '45-54 years old': 302}
#Conteo de lugares de consumo: {'At a cafe': 1170, 'At the office': 1430, 'At home': 3644, 'On the go': 705, 'None of these': 36}

"""
6- Pruebe la función anterior, analizando las columnas 'cups' y 'brew'. ¿Funciona?
"""
def procesamiento_columna2(archivo: str, columna:str) -> dict[str,int]:

  conteo = {}

  with open(archivo, 'r', encoding='utf-8') as resultados_encuesta:
    lector = csv.DictReader(resultados_encuesta)

    for encuestado in lector:
      if columna == 'brew':
        tipos = encuestado['brew'].split(sep=", ")
        for tipo in tipos:
          if tipo in conteo:
            conteo[tipo] += 1
          else:
            conteo[tipo] = 1
      elif columna == 'cups':
        tazas = encuestado['cups']
        if tazas in conteo:
          conteo[tazas] += 1
        else:
          conteo[tazas] = 1
      else:
        print("Columna incorrecta.")
      

  return conteo

print("\nConteo de cups:", procesamiento_columna2("C:/Users/fedew/Desktop/IA/Programacion I/TP FINAL/ETAPA 0/coffee_survey.csv", 'cups'))
print("\nConteo de brew:", procesamiento_columna2("C:/Users/fedew/Desktop/IA/Programacion I/TP FINAL/ETAPA 0/coffee_survey.csv", 'brew'))

#Respuestas esperadas:
#Conteo de cups: {'Less than 1': 348, '2': 1663, '1': 1277, '3': 473, 'More than 4': 67, '4': 121}
#Conteo de brew: {'Pod/capsule machine (e.g. Keurig/Nespresso)': 336, 'Bean-to-cup machine': 84, 'Coffee brewing machine (e.g. Mr. Coffee)': 663, 'Pour over': 2295, 'Espresso': 1518, 'French press': 735, 'Instant coffee': 130, 'Other': 677, 'Coffee extract (e.g. Cometeer)': 186, 'Cold brew': 525}