SELECT * FROM Customers
SELECT * FROM Orders
SELECT * FROM [Order Details]
SELECT * FROM Territories
SELECT * FROM Products
SELECT * FROM Categories
SELECT * FROM Employees

--------------------------------------- Ejercicio 1)_
--Se necesita obtener un listado de todos los pedidos con el nombre del cliente (nombre de la empresa).
SELECT C.CompanyName, O.OrderID
FROM Customers C
JOIN Orders O
ON C.CustomerID = O.CustomerID;

--------------------------------------- Ejercicio 2)_
--Se necesita saber la cantidad de pedidos que realizó cada cliente(ordenados por nombre de la empresa).
SELECT C.CompanyName, COUNT(*) AS CANTIDAD_PEDIDOS
FROM Orders O
JOIN Customers C
ON C.CustomerID = O.CustomerID
GROUP BY C.CompanyName
ORDER BY C.CompanyName;

--------------------------------------- Ejercicio 3)_
--Calcular el total y promedio de ventas por empleado.
SELECT E.EmployeeID, E.FirstName, E.LastName, AVG(UnitPrice * Quantity) AS PROMEDIO_VENTAS, SUM(UnitPrice * Quantity) AS TOTAL
FROM [Order Details] OD 
JOIN Orders O ON OD.OrderID = O.OrderID
JOIN Employees E ON E.EmployeeID = O.EmployeeID
GROUP BY E.EmployeeID, E.FirstName, E.LastName;

--------------------------------------- Ejercicio 4)_
--Mostrar los productos con ventas totales mayores a $10.000.
SELECT P.ProductID, P.ProductName, SUM(OD.UnitPrice * OD.Quantity) AS TOTAL
FROM [Order Details] OD
JOIN Products P ON P.ProductID = OD.ProductID
GROUP BY P.ProductID, P.ProductName
HAVING SUM(OD.UnitPrice * OD.Quantity) > 10000;

--------------------------------------- Ejercicio 5)_
--Obtener el primer y ultimo pedido de cada cliente.
SELECT C.CustomerID, C.CompanyName, MAX(O.OrderID) AS ULTIMO_PEDIDO, MIN(O.OrderID) AS PRIMER_PEDIDO
FROM Customers C 
JOIN Orders O ON C.CustomerID = O.CustomerID
GROUP BY C.CustomerID, C.CompanyName;

--------------------------------------- Ejercicio 6)_
--Mostrar un listado de los clientes que realizaron más de 20 pedidos.
SELECT C.CustomerID, C.CompanyName, COUNT(O.OrderID) AS Total_Pedidos
FROM Customers C 
JOIN Orders O ON C.CustomerID = O.CustomerID
GROUP BY C.CustomerID, C.CompanyName
HAVING COUNT(O.OrderID) > 20;

--------------------------------------- Ejercicio 7)_
--Obtener el promedio de cantidad pedida por producto y categoría.
SELECT P.ProductID, P.ProductName, C.CategoryName, AVG(OD.Quantity) AS Cantidad_Pedida
FROM [Order Details] OD
JOIN Products P ON P.ProductID = OD.ProductID
JOIN Categories C ON C.CategoryID = P.CategoryID
GROUP BY P.ProductID, P.ProductName, C.CategoryName
ORDER BY Cantidad_Pedida DESC;

--------------------------------------- Ejercicio 8)_
--Obtener las ventas totales por país de envío.
SELECT O.ShipCountry, SUM(OD.Quantity * OD.UnitPrice) AS Total_Ventas 
FROM Orders O
JOIN [Order Details] OD ON OD.OrderID = O.OrderID
GROUP BY O.ShipCountry
ORDER BY Total_Ventas DESC;

--------------------------------------- Ejercicio 9)_
--Obtener el Promedio de precios de productos por categoría.
SELECT C.CategoryID, C.CategoryName, AVG(P.UnitPrice) AS Promedios_precio
FROM Categories C
JOIN Products P ON P.CategoryID = C.CategoryID
GROUP BY C.CategoryID, C.CategoryName
ORDER BY Promedios_precio DESC;

--------------------------------------- Ejercicio 10)_
--Listado de clientes con pedidos enviados a más de un país.
SELECT C.CompanyName, COUNT(O.ShipCountry) AS PedidosAMasDeUnPais
FROM Customers C
JOIN Orders O ON O.CustomerID = C.CustomerID
GROUP BY C.CompanyName
HAVING COUNT(O.ShipCountry) > 1
ORDER BY PedidosAMasDeUnPais DESC;
