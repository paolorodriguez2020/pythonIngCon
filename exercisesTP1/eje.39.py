def simular_mercado(precios_diarios, operaciones):
    total = 0
    acciones = 0  

    for operacion, dia in operaciones:
        if operacion == "compra":
           
            precio_compra = precios_diarios[dia]
            total -= precio_compra
            acciones += 1  
            print(f"Compra de 1 acción a {precio_compra} en el día {dia}. Total: {total}")
        elif operacion == "venta":
            if acciones > 0:  
                precio_venta = precios_diarios[dia]
                total += precio_venta
                acciones -= 1  
                print(f"Venta de 1 acción a {precio_venta} en el día {dia}. Total: {total}")
            else:
                print(f"No hay acciones para vender en el día {dia}.")

    
    return total


precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

beneficio_total = simular_mercado(precios_diarios, operaciones)
print(f"Beneficio o pérdida total: {beneficio_total}")
