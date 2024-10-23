def analizar_tendencias(hashtags, tendencias, umbral):
    
    frecuencia_hashtags = {}
    for hashtag in hashtags:
        if hashtag in frecuencia_hashtags:
            frecuencia_hashtags[hashtag] += 1
        else:
            frecuencia_hashtags[hashtag] = 1

    
    hashtags_populares = []
    for hashtag, frecuencia in tendencias:
        if frecuencia > umbral:
            hashtags_populares.append(hashtag)
    
    return hashtags_populares


hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

umbral = 100
hashtags_mencionados = analizar_tendencias(hashtags, tendencias, umbral)
print(hashtags_mencionados)
