def analizar_encuestas(encuestas):
    resultados_frecuencia = {}

    for pregunta, respuestas in encuestas.items():
       
        frecuencia = {}
        for respuesta in respuestas:
            if respuesta in frecuencia:
                frecuencia[respuesta] += 1
            else:
                frecuencia[respuesta] = 1
        
      
        resultados_frecuencia[pregunta] = frecuencia

    return resultados_frecuencia


encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

resultados = analizar_encuestas(encuestas)
print(resultados)
