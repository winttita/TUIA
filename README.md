# TUIA — Tecnicatura Universitaria en Inteligencia Artificial

Repositorio académico con el material y los trabajos prácticos desarrollados a lo largo de la **Tecnicatura Universitaria en Inteligencia Artificial (TUIA)**, dictada por la **Facultad de Ciencias Exactas, Ingeniería y Agrimensura (FCEIA) de la Universidad Nacional de Rosario (UNR)**.

Incluye únicamente las materias que requieren desarrollo de código (programación, bases de datos, estadística aplicada y redes), organizadas por año y cuatrimestre. Varios de los trabajos prácticos finales fueron realizados en grupo y se versionan en repositorios propios, integrados aquí como **submódulos de Git**.

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
│   ├── Entorno de Programacion/      # Linux, shell, control de versiones, Docker
│   ├── Programacion I/               # Fundamentos de programación en Python
│   ├── Programacion II/              # Recursión, POO, TADs, árboles y grafos
│   └── Bases de Datos I/             # Modelo relacional, SQL, normalización
└── Segundo/
    ├── Bases de Datos II/            # Data warehousing, modelado dimensional, OLAP
    ├── Fundamento de Ciencia de Datos/ # Análisis y visualización de datos
    ├── Probabilidad y Estadistica/   # Probabilidad, inferencia y estimación
    ├── Programacion III/             # Inteligencia artificial: búsqueda y juegos
    └── Redes de Datos/               # Redes, modelo OSI/TCP-IP, CCNA, APIs REST
```

Cada carpeta de materia agrupa, según corresponda, los apuntes y resúmenes de cátedra, las prácticas de los distintos ejes temáticos, los parciales resueltos y el trabajo práctico final.

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

---

## Trabajos prácticos en submódulos

Los siguientes trabajos prácticos finales se desarrollaron en equipo y se mantienen en repositorios independientes, integrados aquí como submódulos:

| Materia | Submódulo | Descripción |
|---|---|---|
| Bases de Datos I | [TP-Final-BDDI](https://github.com/winttita/TP-Final-BDDI) | Modelo relacional para la gestión del arbolado público de Rosario: inventario de árboles, cuadrillas, tareas y reclamos ciudadanos, con DDL, DML, vistas y procedimientos almacenados en SQL Server |
| Entorno de Programación | [TP-Final-EDP](https://github.com/winttita/TP-Final-EDP) | Aplicación containerizada con Docker, desarrollada en equipo: incluye scripts, modelo y documentación de despliegue |
| Bases de Datos II | [TP-Final-BDDII](https://github.com/winttita/TP-Final-BDDII) | Diseño de un Data Warehouse para una distribuidora de bebidas ficticia, con modelo dimensional, ETL y reportes en Power BI |
| Probabilidad y Estadística | [TP-Final-PyE](https://github.com/winttita/TP-Final-PyE) | Análisis estadístico en R sobre el dataset público de IMDb, siguiendo el ciclo PPDAC e intervalos de confianza |
| Programación III | [tuia-prog3](https://github.com/jqnag8/tuia-prog3) | Tres trabajos de inteligencia artificial en Python: solver de TSP (búsqueda local), Tateti con algoritmo Minimax y buscador de caminos (DFS/BFS/UCS/GBFS/A*) |
| Redes de Datos | [TP-Final-RDD](https://github.com/winttita/TP-Final-RDD) | Diseño e implementación de una API REST como trabajo final de la materia |

> Al ser submódulos, su contenido puede tener su propio README con instrucciones de instalación y ejecución específicas.

---

## Tecnologías utilizadas

A lo largo de la carrera se trabajó con un conjunto variado de lenguajes y herramientas:

- **Lenguajes:** Python, SQL (T-SQL), R
- **Datos y BI:** Jupyter Notebook, pandas, Power BI, SSIS
- **Bases de datos:** SQL Server, modelado relacional y dimensional
- **Redes:** Cisco Packet Tracer (CCNA)
- **Infraestructura:** Docker, Git y GitHub (incluyendo submódulos)

---

## Sobre la carrera

La **Tecnicatura Universitaria en Inteligencia Artificial (TUIA)** es una carrera de pregrado de la FCEIA - UNR (Rosario, Argentina), con una duración de 2 años y medio (1800 horas totales), dictada de forma presencial y con materias organizadas por cuatrimestre. El ingreso es irrestricto, con un curso introductorio de apoyo, y la carrera es gratuita.

Forma Técnicos/as Universitarios/as en Inteligencia Artificial capacitados para diseñar y desarrollar sistemas y modelos de IA, con base en matemática, probabilidad y estadística, programación y bases de datos, y formación específica en ciencia de datos, minería de datos, aprendizaje automático, y procesamiento de imágenes, video y habla. El plan de estudios también habilita a coordinar equipos de trabajo y dirigir proyectos de pequeña o mediana escala dentro de este campo.

## Autor

**Federico** ([@winttita](https://github.com/winttita)) — Estudiante de la TUIA, FCEIA - UNR.