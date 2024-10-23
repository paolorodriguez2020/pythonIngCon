def actualizar_inventario(inventario, tienda, **kwargs):
    if tienda in inventario:
        for producto, cantidad in kwargs.items():
           
            if producto in inventario[tienda]:
              
                inventario[tienda][producto] += cantidad
            else:
                print(f"El producto '{producto}' no se encuentra en la {tienda}.")
    else:
        print(f"La tienda '{tienda}' no existe en el inventario.")

    return inventario


inventario = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}

estado_actual = actualizar_inventario(inventario, tienda="Tienda A", producto_1=10, producto_2=-5)
print(estado_actual)
