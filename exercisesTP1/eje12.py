def producto_mas_caro(productos):
    # Inicializar el producto más caro con el primer producto en la lista
    producto_caro = productos[0]
    
    # Iterar sobre los productos para encontrar el más caro
    for producto in productos:
        if producto[1] > producto_caro[1]:  # Comparar los precios
            producto_caro = producto
    
    return producto_caro

# Lista de productos
productos = [("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30)]

# Llamar a la función y mostrar el resultado
producto_caro = producto_mas_caro(productos)
print(producto_caro)
