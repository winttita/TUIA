# TUIA — Tecnicatura Universitaria en Inteligencia Artificial

Repositorio académico con el material y los trabajos prácticos desarrollados a lo largo de la **Tecnicatura Universitaria en Inteligencia Artificial (TUIA)**, dictada por la **Facultad de Ciencias Exactas, Ingeniería y Agrimensura (FCEIA) de la Universidad Nacional de Rosario (UNR)**.

Incluye únicamente las materias que requieren desarrollo de código (programación, bases de datos, estadística aplicada, redes, ciencia de datos e inteligencia artificial), organizadas por año y cuatrimestre. Varios de los trabajos prácticos finales fueron realizados en grupo y se versionan en repositorios propios, integrados aquí como **submódulos de Git**.

---

## Cómo clonar el repositorio

Como este repositorio contiene submódulos, es necesario clonarlo indicando que se traigan también esos repositorios:

```bash
git clone --recurse-submodules https://github.com/winttita/TUIA.git
```

Si ya clonaste el repositorio sin esa opción, podés inicializar los submódulos después con:

```bash
git submodule update --init --recursive
```

---

## Estructura del repositorio

```
TUIA/
├── Primero/
│   ├── Entorno de Programacion/          # Linux, shell, control de versiones, Docker
│   ├── Programacion I/                   # Fundamentos de programación en Python
│   ├── Programacion II/                  # Recursión, POO, TADs, árboles y grafos
│   └── Bases de Datos I/                 # Modelo relacional, SQL, normalización
└── Segundo/
    ├── Bases de Datos II/                # Data warehousing, modelado dimensional, OLAP
    ├── Fundamento de Ciencia de Datos/   # Análisis y visualización de datos
    ├── Probabilidad y Estadistica/       # Probabilidad, inferencia y estimación
    ├── Programacion III/                 # Inteligencia artificial: búsqueda y juegos
    ├── Redes de Datos/                   # Redes, modelo OSI/TCP-IP, CCNA, APIs REST
    ├── Aprendizaje Automatico I/         # Regresión, clasificación, MLOps, redes neuronales
    ├── Mineria de datos/                 # Reducción de dimensionalidad, clustering, asociación
    ├── Procesamiento de Imagenes I/      # Filtrado espacial y frecuencial, morfología, color
    └── Procesamiento del Lenguaje Natural/ # Extracción de texto, vectorización, NLP
```

Cada carpeta de materia agrupa, según corresponda, los apuntes y resúmenes de cátedra organizados por unidad (`U0`, `U1`, `U2`...), notebooks de práctica, datasets de trabajo, y el o los trabajos prácticos finales.

---

## Materias por año

### Primer año

| Cuatrimestre | Materia | Contenido principal |
|---|---|---|
| 1° | [Entornos de Programación](./Primero/Entorno%20de%20Programacion/) | Introducción a Linux, terminal, Git y contenedores Docker |
| 1° | [Programación I](./Primero/Programacion%20I/) | Fundamentos de programación con Python |
| 2° | [Programación II](./Primero/Programacion%20II/) | Recursión, programación orientada a objetos, TADs, árboles y grafos |
| 2° | [Bases de Datos I](./Primero/Bases%20de%20Datos%20I/) | Modelo entidad-relación, SQL y normalización |

### Segundo año

| Cuatrimestre | Materia | Contenido principal |
|---|---|---|
| 1° | [Bases de Datos II](./Segundo/Bases%20de%20Datos%20II/) | Data warehouse, modelado dimensional, OLAP y explotación de datos |
| 1° | [Fundamentos de Ciencia de Datos](./Segundo/Fundamento%20de%20Ciencia%20de%20Datos/) | Manipulación, resumen, transformación y visualización de datos |
| 1° | [Probabilidad y Estadística](./Segundo/Probabilidad%20y%20Estadistica/) | Probabilidad, distribuciones muestrales, estimación e intervalos de confianza |
| 1° | [Programación III](./Segundo/Programacion%20III/) | Inteligencia artificial: búsqueda informada/no informada, juegos adversarios y CSP |
| 1° | [Redes de Datos](./Segundo/Redes%20de%20Datos/) | Modelos de red, direccionamiento IP, ruteo y APIs REST (orientado a CCNA) |
| 2° | [Aprendizaje Automático I](./Segundo/Aprendizaje%20Automatico%20I/) | Análisis exploratorio, modelos lineales de regresión y clasificación, comparación/ajuste de modelos, MLOps, introducción a redes neuronales |
| 2° | [Minería de Datos](./Segundo/Mineria%20de%20datos/) | Fundamentos de minería de datos, tipología de algoritmos, reducción de dimensionalidad |
| 2° | [Procesamiento de Imágenes I](./Segundo/Procesamiento%20de%20Imagenes%20I/) | Fundamentos de imagen digital, transformación y filtrado espacial/frecuencial |
| 2° | [Procesamiento del Lenguaje Natural](./Segundo/Procesamiento%20del%20Lenguaje%20Natural/) | Extracción y limpieza de texto, representación vectorial (frecuentista) |

> Las materias del 2° cuatrimestre de Segundo año corresponden al 4° cuatrimestre de la carrera y están en curso: su contenido se irá completando unidad por unidad a medida que avance la cátedra.

---

## Detalle de materias en curso (4° cuatrimestre)

### Aprendizaje Automático I
- `U0 - EDA`: análisis exploratorio de datos y correlación.
- `U1 - Introduccion al Aprendizaje Automatico`: apuntes de clase.
- `U2 - Regresion Lineal`: análisis descriptivo, gradiente descendiente, regularización, notebooks y datasets asociados.
- `TPs/` (submódulo): TP1 de Regresión Lineal con descenso de gradiente (informe y notebooks); TP2 aún no iniciado.

### Minería de Datos
- `U1 - Introduccion`: apuntes y dataset de ejemplo (IECM).
- `U2 - Reduccion de Dimensionalidad`: apuntes, script en Python y dataset (`star-dataset.csv`).

### Procesamiento de Imágenes I
- `Programa.pdf`: programa oficial de la cátedra.
- `U1 - Introduccion`: fundamentos de imagen digital, con código y ejercicios resueltos.
- `U2 - Transformacion y Filtrado`: filtrado espacial y frecuencial, con código, ejercicios y material extra.

### Procesamiento del Lenguaje Natural
- `U1 - Extraccion y Procesamiento de Texto`: apuntes, ejemplos de codificación de caracteres y notebooks de práctica.
- `U2 - Representacion Vectorial de Texto`: apuntes y notebook de vectorización frecuentista.
- `TPs/` (submódulo): TP1 de scraping (Playwright + BeautifulSoup) sobre una categoría de libros de Lectulandia, con diseño de extracción documentado, en desarrollo.
- Material adicional: diccionario de lunfardo para prácticas de normalización de texto, y guía de metodología de informes de la cátedra.

---

## Trabajos prácticos en submódulos

Los siguientes trabajos prácticos finales o grupales se desarrollan en equipo y se mantienen en repositorios independientes, integrados aquí como submódulos:

| Materia | Submódulo | Descripción |
|---|---|---|
| Bases de Datos I | [TP-Final-BDDI](https://github.com/winttita/TP-Final-BDDI) | Modelo relacional para la gestión del arbolado público de Rosario: inventario de árboles, cuadrillas, tareas y reclamos ciudadanos, con DDL, DML, vistas y procedimientos almacenados en SQL Server |
| Entorno de Programación | [TP-Final-EDP](https://github.com/winttita/TP-Final-EDP) | Aplicación containerizada con Docker, desarrollada en equipo: incluye scripts, modelo y documentación de despliegue |
| Bases de Datos II | [TP-Final-BDDII](https://github.com/winttita/TP-Final-BDDII) | Diseño de un Data Warehouse para una distribuidora de bebidas ficticia, con modelo dimensional, ETL y reportes en Power BI |
| Probabilidad y Estadística | [TP-Final-PyE](https://github.com/winttita/TP-Final-PyE) | Análisis estadístico en R sobre el dataset público de IMDb, siguiendo el ciclo PPDAC e intervalos de confianza |
| Programación III | [tuia-prog3](https://github.com/jqnag8/tuia-prog3) | Tres trabajos de inteligencia artificial en Python: solver de TSP (búsqueda local), Tateti con algoritmo Minimax y buscador de caminos (DFS/BFS/UCS/GBFS/A*) |
| Redes de Datos | [TP-Final-RDD](https://github.com/winttita/TP-Final-RDD) | Diseño e implementación de una API REST como trabajo final de la materia |
| Aprendizaje Automático I | [TP_AA1_Civetta_Fucci_Frank_Winter](https://github.com/valentinocivetta04/TP_AA1_Civetta_Fucci_Frank_Winter) | TP grupal: TP1 de regresión lineal con descenso de gradiente sobre dataset de precios de viviendas (en curso) |
| Procesamiento del Lenguaje Natural | [PLN_Grupo7_Civetta_Fucci_Frank_Winter](https://github.com/valentinocivetta04/PLN_Grupo7_Civetta_Fucci_Frank_Winter) | TP grupal: scraper con Playwright/BeautifulSoup para extraer metadatos y sinopsis de libros de una categoría de Lectulandia (en curso) |

> Al ser submódulos, su contenido puede tener su propio README con instrucciones de instalación y ejecución específicas.

---

## Tecnologías utilizadas

A lo largo de la carrera se trabajó con un conjunto variado de lenguajes y herramientas:

- **Lenguajes:** Python, SQL (T-SQL), R
- **Datos y BI:** Jupyter Notebook, pandas, scikit-learn, Power BI, SSIS
- **Bases de datos:** SQL Server, modelado relacional y dimensional
- **Redes:** Cisco Packet Tracer (CCNA)
- **Web scraping:** Playwright, BeautifulSoup
- **Infraestructura:** Docker, Git y GitHub (incluyendo submódulos)

---

## Sobre la carrera

La **Tecnicatura Universitaria en Inteligencia Artificial (TUIA)** es una carrera de pregrado de la FCEIA - UNR (Rosario, Argentina), con una duración de 2 años y medio (1800 horas totales), dictada de forma presencial y con materias organizadas por cuatrimestre. El ingreso es irrestricto, con un curso introductorio de apoyo, y la carrera es gratuita.

Forma Técnicos/as Universitarios/as en Inteligencia Artificial capacitados para diseñar y desarrollar sistemas y modelos de IA, con base en matemática, probabilidad y estadística, programación y bases de datos, y formación específica en ciencia de datos, minería de datos, aprendizaje automático, y procesamiento de imágenes, video y habla. El plan de estudios también habilita a coordinar equipos de trabajo y dirigir proyectos de pequeña o mediana escala dentro de este campo.

## Autor

**Federico** ([@winttita](https://github.com/winttita)) — Estudiante de la TUIA, FCEIA - UNR.
