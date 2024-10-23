def optimizar_rutas(rutas, distancias_max):
    rutas_validas = []
    
    for (origen, destino, distancia), distancia_max in zip(rutas, distancias_max):
        if distancia <= distancia_max:
            rutas_validas.append((origen, destino, distancia))
    
    return rutas_validas


rutas = [
    ("Madrid", "Barcelona", 620),
    ("Madrid", "Valencia", 350),
    ("Barcelona", "Valencia", 350)
]
distancias_max = [600, 400, 500]

rutas_optimizadas = optimizar_rutas(rutas, distancias_max)
print(rutas_optimizadas)
