def filtrar_empleados(empleados, salario_minimo):
    empleados_filtrados = {}
    for id_empleado, info in empleados.items():
        nombre, edad, salario = info
        if salario > salario_minimo:
            empleados_filtrados[id_empleado] = info
    return empleados_filtrados

# Ejemplo de uso
empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

resultado = filtrar_empleados(empleados, 3000)
print(resultado)
