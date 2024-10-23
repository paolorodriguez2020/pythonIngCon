def configurar_perfiles(usuarios, **kwargs):
    perfiles = {}
    for usuario in usuarios:
        # Crear un array con las configuraciones aplicadas
        configuraciones = list(kwargs.values())
        perfiles[usuario] = configuraciones
    return perfiles

# Ejemplo de uso
usuarios = ["Ana", "Luis", "María"]
perfiles_configurados = configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False)
print(perfiles_configurados)
