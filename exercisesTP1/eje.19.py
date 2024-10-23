def calcular_goles_totales(resultados):
    total_anotados = 0
    total_recibidos = 0
    for goles in resultados.values():
        anotados, recibidos = goles
        total_anotados += anotados
        total_recibidos += recibidos
    return total_anotados, total_recibidos

# Ejemplo de uso
resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

anotados, recibidos = calcular_goles_totales(resultados)
print(f"Total de goles anotados: {anotados}")
print(f"Total de goles recibidos: {recibidos}")
