def crear_perfil(nombre, edad, email, **kwargs):
    # Crear un diccionario con la información básica
    perfil = {
        "nombre": nombre,
        "edad": edad,
        "email": email
    }
    # Agregar datos adicionales al diccionario
    perfil.update(kwargs)
    return perfil

# Ejemplo de uso
usuario_perfil = crear_perfil(nombre="Luis", edad=25, email="juan@mail.com", ciudad="Mendoza", telefono="123456789")
print(usuario_perfil)
