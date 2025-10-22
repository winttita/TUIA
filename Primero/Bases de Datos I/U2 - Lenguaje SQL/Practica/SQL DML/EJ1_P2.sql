USE empresa_basica

----------------------- a

SELECT nombre, apellido1, apellido2, dni
FROM DIRECTOR
WHERE dni = 33193456

SELECT nombre, apellido1 + ' ' + apellido2 AS APELLIDO, dni
FROM DIRECTOR
WHERE dni = 33193456

----------------------- b

SELECT 
	dptoid AS NUMERO_DEPARTAMENTO,
	COUNT(*) AS CANTIDAD_PROY
FROM PROYECTO
GROUP BY dptoid

----------------------- c

SELECT 
	TOP 1
	nombre, dni, sueldo
FROM EMPLEADO
WHERE dptoid = 1
ORDER BY sueldo DESC

----------------------- d

SELECT 
	AVG(sueldo)
FROM EMPLEADO
WHERE dptoid = 1

----------------------- e (ver subquery)

SELECT E.nombre, E.apellido1, P.horas, P.proyectoid
FROM PROYECTO_EMPLEADO AS P
INNER JOIN
	EMPLEADO AS E ON P.empleadoid = E.empleadoid
WHERE P.horas > 3 AND P.proyectoid = 1

----------------------- f

SELECT nombre, apellido1, fechanac
FROM EMPLEADO
WHERE fechanac <= '1980-12-31' and fechanac >= '1960-01-01'
