def calcular_promedios(estudiantes):
    promedios = {}
    
    for id_estudiante, materias in estudiantes.items():
        total_calificaciones = 0
        total_asignaturas = 0
        
        for calificaciones in materias.values():
            total_calificaciones += sum(calificaciones)
            total_asignaturas += len(calificaciones)
        
        
        promedio = total_calificaciones / total_asignaturas if total_asignaturas > 0 else 0
        promedios[id_estudiante] = promedio

   
    ranking = sorted(promedios.items(), key=lambda x: x[1], reverse=True)
    
    return ranking

estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

ranking = calcular_promedios(estudiantes)
print("Ranking de estudiantes basado en su promedio general:")
for id_estudiante, promedio in ranking:
    print(f"Estudiante ID {id_estudiante}: Promedio {promedio:.2f}")
