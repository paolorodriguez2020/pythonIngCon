def estadisticas_ventas(ventas):
    total_ventas = sum(ventas)
    promedio_ventas = total_ventas / len(ventas) if len(ventas) > 0 else 0
    mes_maximo = ventas.index(max(ventas)) + 1  # +1 para que sea 1-12 en lugar de 0-11
    return {
        "total_ventas": total_ventas,
        "promedio_mensual": promedio_ventas,
        "mes_con_mayores_ventas": mes_maximo
    }

ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]
estadisticas = estadisticas_ventas(ventas_mensuales)
print(estadisticas)
