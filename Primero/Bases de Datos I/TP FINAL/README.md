# Trabajo Práctico 2025: Sistema de Gestión de Arbolado Público

Este repositorio contiene la resolución del Trabajo Práctico de **Bases de Datos I (2025)**. El proyecto consiste en el diseño e implementación de un modelo de base de datos relacional para la **Dirección General de Parques y Paseos del municipio de Rosario**.

## Escenario del Proyecto

El objetivo es informatizar la gestión del arbolado público, que incluye tareas de plantado, mantenimiento y cuidado de ejemplares en veredas y espacios verdes. El sistema permite administrar:

* **Inventario de Árboles:** Registro de especies, ubicación (coordenadas, parques, calles), estado de salud, altura y fecha de plantado.
* **Gestión de Cuadrillas:** Administración de equipos de trabajo y empleados (con datos de contacto y fecha de ingreso).
* **Planificación de Tareas:** Asignación de actividades (poda, remoción, etc.) a cuadrillas específicas, registro de fechas y comentarios post-tarea.
* **Reclamos Ciudadanos:** Seguimiento de reclamos recibidos por mail, motivos del reclamo y tiempos de resolución.

## Contenido del Repositorio

La solución abarca los siguientes puntos requeridos:

1.  **Modelo de Datos:**
    * Diagrama Entidad-Relación (DER) normalizado en **3FN**.
         * Link al DER --> https://www.drawdb.app/editor?shareId=136ac6a3d8b99b33fd0cafe26ec6e197

2.  **Scripts SQL:**
    * `DDL.sql`: Creación de la base de datos, tablas y restricciones.
    * `DML.sql`: Poblado de datos de prueba (Seed Data) con al menos:
        * 3 cuadrillas y 10 empleados.
        * 50 árboles de distintas especies y estados.
        * 20 tareas y 20 reclamos históricos para pruebas.

3.  **Consultas y Lógica de Negocio:**
    * **Queries complejas:** Reportes como "Cuadrilla con más tareas en Octubre 2025" o "Árboles más altos por especie".
    * **Vistas (Views):** Análisis de tiempos de respuesta en reclamos y resúmenes de tareas por tipo.
    * **Procedimientos Almacenados (Stored Procedures):** Lógica para detectar tareas pendientes y próximas fechas de ejecución por árbol.

## Tecnologías

**Motor de Base de Datos:** Microsoft SQL Server
**Herramientas:** SQL Server Management Studio (SSMS)

---
*Trabajo realizado para el segundo cuatrimestre de la TUIA - 2025*.
