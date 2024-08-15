def analizar_temperaturas(temperaturas):
    if not temperaturas:  # Verificar si la lista está vacía
        return "No hay datos de temperaturas"
    
    # Calcular la temperatura media
    media = sum(temperaturas) / len(temperaturas)
    
    # Calcular la temperatura máxima y mínima
    maxima = max(temperaturas)
    minima = min(temperaturas)
    
    return media, maxima, minima

# Array de temperaturas
temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

# Llamar a la función y mostrar los resultados
media, maxima, minima = analizar_temperaturas(temperaturas)
print(f"Temperatura media del mes: {media:.2f}°C")
print(f"Temperatura máxima del mes: {maxima:.2f}°C")
print(f"Temperatura mínima del mes: {minima:.2f}°C")
