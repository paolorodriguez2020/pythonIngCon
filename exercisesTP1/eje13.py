def promedio_calificaciones(registro, matricula):
    # Verificar si la matrícula está en el registro
    if matricula not in registro:
        return "Matrícula no encontrada"
    
    # Obtener las calificaciones del estudiante
    estudiante = registro[matricula]
    calificaciones = estudiante["calificaciones"]
    
    # Calcular el promedio de las calificaciones
    total_calificaciones = sum(calificaciones.values())
    numero_materias = len(calificaciones)
    promedio = total_calificaciones / numero_materias
    
    return promedio

# Registro de estudiantes
estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

# Ejemplo de uso
matricula = 101
promedio = promedio_calificaciones(estudiantes, matricula)
print(f"El promedio de calificaciones para el estudiante con matrícula {matricula} es: {promedio:.2f}")
