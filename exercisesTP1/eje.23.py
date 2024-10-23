def actualizar_inventario(inventario, ventas):
    # Recorre cada índice y resta las ventas al inventario
    for i in range(len(inventario)):
        inventario[i] -= ventas[i]
    return inventario

# Ejemplo de uso
inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

inventario_actualizado = actualizar_inventario(inventario, ventas)
print(inventario_actualizado)
