CREATE DATABASE P2_EJ4
USE P2_EJ4
GO

CREATE TABLE PRODUCTO(
nro_prod varchar(4) NOT NULL,
nombre_prod varchar(20) NOT NULL,
color varchar(10) NOT NULL,
precio decimal(10,2),
CONSTRAINT PK_producto_nro_prod PRIMARY KEY (nro_prod),
CONSTRAINT CH_producto_color CHECK (color IN ('Rosa', 'Verde', 'Azul', 'Violeta', 'Negro', 'Blanco'))
);

INSERT INTO PRODUCTO (nro_prod, nombre_prod, color, precio) VALUES
('1225', 'Auris', 'Azul', 15.2)

select * from PRODUCTO
