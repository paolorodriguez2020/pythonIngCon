def procesar_ventas(ventas):
    total_ventas = sum(ventas)
    promedio_ventas = total_ventas / len(ventas) if len(ventas) > 0 else 0
    return total_ventas, promedio_ventas

# Ejemplo de uso
ventas_diarias = [200, 450, 300, 400, 350, 500, 600]
total, promedio = procesar_ventas(ventas_diarias)
print(f"Total de ventas: {total}")
print(f"Promedio de ventas por día: {promedio}")
