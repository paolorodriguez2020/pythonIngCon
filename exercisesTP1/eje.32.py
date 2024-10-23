def simular_ventas(*ventas):
    total_ingresos = 0.0
    
    for venta in ventas:
        producto, cantidad_vendida, precio_por_unidad = venta
        total_ingresos += cantidad_vendida * precio_por_unidad
    
    return total_ingresos


total = simular_ventas(
    ("Producto A", 10, 15.0), 
    ("Producto B", 5, 25.0), 
    ("Producto C", 3, 50.0)
)

print(f"Total de ingresos generados: ${total:.2f}")
