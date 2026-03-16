USE TP_BDDI_FRANK_WINTER
GO

/* a. Mostrar información de los reclamos. Se desea saber la fecha de cada uno, 
el código del árbol asociado al reclamo, la cantidad de días que se tardó en 
asignar la tarea y la cantidad de días que se tardó en resolver el mismo. Si 
no tiene tarea asignada o no fue resuelto calcular los días hasta la fecha 
actual. */

ALTER VIEW V_Info_Reclamos AS
	SELECT
		R.fecha, R.FechaAsignacionTarea, A.codigo, 
		DATEDIFF(DAY, R.Fecha, ISNULL(T.FechaRealizado, GETDATE())) AS [Tiempo de Resolucion], 
		DATEDIFF(DAY, R.Fecha, ISNULL(R.FechaAsignacionTarea, GETDATE())) AS [Tiempo de Asignacion]
	FROM Reclamos R
	JOIN Arbol A ON A.idarbol = R.idarbol
	JOIN Tarea T ON T.idtarea = R.idtarea;

/* b.Resumen de tareas ya realizadas según su tipo. Se desea saber la fecha de 
la primer y última tarea de cada tipo y la cantidad de tareas realizadas.*/

CREATE VIEW V_Tareas_Realizadas AS
	SELECT TT.Descripcion, MIN(T.FechaRealizado) AS [Primera Fecha Realizada], MAX(T.FechaRealizado) AS [Ultima Fecha Realizada], COUNT(*) AS [CANTIDAD TAREAS]
	FROM Tarea T
	JOIN TipoTarea AS TT ON T.idTipoTarea = TT.idTipoTarea
	WHERE T.FechaRealizado <= GETDATE()
	GROUP BY TT.Descripcion;


