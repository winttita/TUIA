/* Creamos la tabla DEPARTAMENTO. 
NroDep es la Clave Primaria (CP)[cite: 2652, 2598].
*/
CREATE TABLE DEPARTAMENTO (
    NroDep INT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL 
    );

/* Creamos la tabla EMPLEADO.
Legajo es la Clave Primaria (CP)[cite: 2654, 2598].
NroDep es Clave Externa (CE) que referencia a DEPARTAMENTO[cite: 2662, 2668].
*/
CREATE TABLE EMPLEADO (
    Legajo INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Sexo CHAR(1),
    FechaNac DATE,
    Sueldo DECIMAL(10, 2),
    NroDep INT,
    FOREIGN KEY (NroDep) REFERENCES DEPARTAMENTO(NroDep) 
    );

/* Insertamos datos en DEPARTAMENTO [cite: 2652] */
INSERT INTO DEPARTAMENTO (NroDep, Nombre)
VALUES
    (7, 'Finanzas'),
    (5, 'Ventas'),
    (1, 'Contaduría'),
    (8, 'Compras'),
    (4, 'Administración');

/* Insertamos datos en EMPLEADO [cite: 2654] */
INSERT INTO EMPLEADO (Legajo, Nombre, Sexo, FechaNac, Sueldo, NroDep)
VALUES
    (27715, 'Botello Jaime', 'M', '1973-01-07', 17500, 5),
    (34019, 'Vizcarra, Francisco', 'M', '1957-05-05', 19100, 4),
    (10992, 'Jabbar Alicia', 'F', '1950-11-11', 14815, 5),
    (30180, 'Racedo Mario', 'M', '1973-01-07', 17500, 4),
    (18512, 'Gatsi Ana', 'F', '1947-01-21', 22550, NULL), /* Gatsi Ana tiene NroDep nulo [cite: 2654] */
    (21447, 'Calero Julia', 'F', '1983-03-03', 24500, 5),
    (29116, 'Armet María', 'F', '1961-07-12', 16482, 1);

SELECT Nombre, Sueldo
FROM EMPLEADO
where NroDep=4;

SELECT Nombre, Sueldo
FROM EMPLEADO
ORDER BY Sueldo DESC;

SELECT
    E.Nombre AS Empleado,
    D.Nombre AS Departamento
FROM
    EMPLEADO AS E
INNER JOIN
    DEPARTAMENTO AS D ON E.NroDep = D.NroDep;

SELECT
    NroDep,
    COUNT(*) AS CantidadEmpleados,
    AVG(Sueldo) AS SueldoPromedio
FROM
    EMPLEADO
WHERE
    NroDep IS NOT NULL /* Excluimos a Gatsi Ana para el promedio [cite: 1873] */
GROUP BY
    NroDep;
   
SELECT
    NroDep,
    AVG(Sueldo) AS SueldoPromedio
FROM
    EMPLEADO
GROUP BY
    NroDep
HAVING
    AVG(Sueldo) > 18500;

SELECT
    E.Nombre,
    D.Nombre AS Departamento
FROM
    EMPLEADO AS E
LEFT JOIN
    DEPARTAMENTO AS D ON E.NroDep = D.NroDep;

SELECT
    D.Nombre
FROM
    DEPARTAMENTO AS D
WHERE
    NOT EXISTS (
        SELECT 1
        FROM EMPLEADO AS E
        WHERE E.NroDep = D.NroDep
    );