def organizar_eventos(*args):
    print("Lista de eventos:")
    for i, evento in enumerate(args, start=1):
        print(f"{i}. {evento}")

# Ejemplo de uso
organizar_eventos("Concierto", "Exposición de arte", "Conferencia")
