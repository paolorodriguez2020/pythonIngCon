def calcular_promedio(*args):
    if len(args) == 0:
        return 0  # Devuelve 0 si no se proporcionaron notas
    return sum(args) / len(args)

# Ejemplo de uso
promedio = calcular_promedio(85, 90, 78, 92, 88)
print(f"El promedio de las notas es: {promedio}")
