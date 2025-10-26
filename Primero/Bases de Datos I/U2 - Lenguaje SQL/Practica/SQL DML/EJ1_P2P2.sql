-------------------------------------- Item a)_
SELECT nombre, apellido1+' '+apellido2 AS Apellido
FROM DIRECTOR
WHERE dni = 33193456;

-------------------------------------- Item b)_

SELECT COUNT(*) AS CANTIDAD_DE_PROY
FROM PROYECTO
WHERE dptoid = (SELECT dptoid
				FROM DPTO
				WHERE nombre = 'investigacion');

-------------------------------------- Item b)_ una mejor alternativa

SELECT D.nombre AS NOMBRE_DPTO, COUNT(*) AS CANT_PROY_DPTO
FROM DPTO AS D
INNER JOIN PROYECTO AS P
ON P.dptoid = D.dptoid
WHERE D.nombre = 'investigacion'
GROUP BY D.nombre;

-------------------------------------- Item c)_

SELECT nombre, dni, sueldo
FROM EMPLEADO AS E
WHERE sueldo = (SELECT MAX(sueldo)
				FROM EMPLEADO AS E
				INNER JOIN DPTO AS D
				ON D.dptoid = E.dptoid
				WHERE D.nombre = 'sede central');

-------------------------------------- Item d)_

SELECT AVG(sueldo) AS SUELDO_PROM_SEDE_CENTRAL
FROM EMPLEADO AS E
INNER JOIN DPTO AS D
ON E.dptoid = D.dptoid
WHERE D.nombre = 'sede central';

-------------------------------------- Item e)_

SELECT COUNT(*) AS CANT_EMPLEADOS
FROM PROYECTO_EMPLEADO AS P
WHERE P.horas > 2 AND P.proyectoid = (SELECT P.proyectoid
									  FROM PROYECTO AS P
									  WHERE P.nombre = 'ProductoX');

-------------------------------------- Item f)_

SELECT COUNT(*) AS CANT_EMPLE_1960_1980
FROM EMPLEADO AS E
WHERE E.fechanac >= '1960-01-01' AND E.fechanac <= '1980-01-01'