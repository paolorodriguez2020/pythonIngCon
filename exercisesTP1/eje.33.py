def hacer_reserva(reservas, fecha, nombre_huesped, habitacion, precio):

    if fecha in reservas:
       
        for reserva in reservas[fecha]:
            if reserva[1] == habitacion:  # Comparamos la habitación
                print(f"La habitación {habitacion} ya está reservada para esa fecha.")
                return False  # No se puede reservar la habitación
    else:
      
        reservas[fecha] = []
    
   
    reservas[fecha].append((nombre_huesped, habitacion, precio))
    print(f"Reserva realizada para {nombre_huesped} en la habitación {habitacion} el {fecha}.")
    return True


reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}


hacer_reserva(reservas, "2024-08-15", "María", 103, 160)  # Éxito
hacer_reserva(reservas, "2024-08-15", "Carlos", 101, 170)  # Fallo: habitación ocupada
hacer_reserva(reservas, "2024-08-17", "Ana", 104, 200)  # Éxito
