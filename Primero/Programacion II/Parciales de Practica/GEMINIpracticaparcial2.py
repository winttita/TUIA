## Ejericio 1 ######################################################################################
def es_palindromo_rec(cadena: str) -> bool:
    if len(cadena) < 2:
        return True
    elif cadena[-1] == cadena[0]:
        return es_palindromo_rec(cadena[1:-1])
    return False

def es_palindromo_itera(cadena: str) -> bool:
    cadena_inver = cadena[::-1]
    pos = 0
    while pos < len(cadena):
        if cadena[pos] == cadena_inver[pos]:
            pos += 1
        else:
            return False
    return True

#print(es_palindromo_rec("neuquen")) # Debería imprimir True
#print(es_palindromo_rec("hola"))    # Debería imprimir False
#print(es_palindromo_itera("a"))       # Debería imprimir True
#print(es_palindromo_itera(""))        # Debería imprimir True

## Ejercicio 3 ######################################################################################
class Producto:
    def __init__(self, sku: str, nombre: str, precio: float) -> None:
        self.sku = sku
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self) -> str:
        return f"Producto: {self.nombre} ${self.precio}"
    
class Electronico(Producto):
    def __init__(self, sku: str, nombre: str, precio: float, marca: str):
        super().__init__(sku, nombre, precio)
        self.marca = marca

    def __str__(self) -> str:
        return f"Producto: {self.nombre} ${self.precio} Marca: {self.marca}"
    
class Ropa(Producto):
    def __init__(self, sku: str, nombre: str, precio: float, talle: str):
        super().__init__(sku, nombre, precio)
        if talle.lower() in ["s", "m", "l"]:
            self.talle = talle
        else:
            print("chupame los dos huevos / baja de peso")

    def __str__(self) -> str:
        return f"Producto: {self.nombre} ${self.precio} Talle: {self.talle}"

class Inventario:
    def __init__(self) -> None:
        self.productos: dict[str, Electronico | Ropa] = {}
    
    def agregar_prod(self, producto: Producto | Electronico | Ropa) -> None:
        if producto.sku not in self.productos:
            self.productos[producto.sku] = producto
            return
        else:
            print("El prod ya se encuentra ingresado.")
            return
    
    def eliminar_prod(self, sku: str) -> None:
        if sku in self.productos:
            self.productos.pop(sku)
            return
    
    def buscar_por_sku(self, sku: str) -> Producto | None:
        if sku in self.productos:
            return self.productos[sku]
        else:
            return None

    def mostrar_inventario(self) -> None:
        for producto in self.productos.values():
            print(producto)

# Creación del sistema
inventario = Inventario()

# Creación y registro de productos
tv = Electronico("ELEC-001", "Smart TV 4K", 85000.0, "Samsung")
remera = Ropa("ROPA-001", "Remera de algodón", 7500.0, "M")
auriculares = Electronico("ELEC-002", "Auriculares Inalámbricos", 22000.0, "Sony")

inventario.agregar_prod(tv)
inventario.agregar_prod(remera)
inventario.agregar_prod(auriculares)

# Mostrar inventario
inventario.mostrar_inventario()
# Salida esperada (el orden puede variar):
# SKU: ELEC-001, Nombre: Smart TV 4K, Precio: 85000.0, Marca: Samsung
# SKU: ROPA-001, Nombre: Remera de algodón, Precio: 7500.0, Talle: M
# SKU: ELEC-002, Nombre: Auriculares Inalámbricos, Precio: 22000.0, Marca: Sony

# Eliminar un producto
inventario.eliminar_prod("ROPA-001")
print("\n--- Inventario después de eliminar ---")
inventario.mostrar_inventario()
