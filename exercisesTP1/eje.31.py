def publicar(nombre_usuario, texto_publicacion, etiquetas=None, **kwargs):
    # Asegurarse de que etiquetas sea una lista, si no se proporciona
    if etiquetas is None:
        etiquetas = []

    # Crear un diccionario con los detalles de la publicación
    publicacion = {
        "nombre_usuario": nombre_usuario,
        "texto": texto_publicacion,
        "etiquetas": etiquetas
    }
    
    # Agregar opciones adicionales al diccionario
    publicacion.update(kwargs)
    
    return publicacion

# Ejemplo de uso
detalles_publicacion = publicar(
    "Juan", 
    "Mi primer post!", 
    etiquetas=["#hola", "#primerPost"], 
    visibilidad="publica", 
    likes=100
)

print(detalles_publicacion)
