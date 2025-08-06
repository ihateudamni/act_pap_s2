def contador_palabras(frase):
    palabras = frase.lower().split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return dict(sorted(conteo.items(), key=lambda x: x[1], reverse=True))

texto = "Python es divertido y python es poderoso"
print(contador_palabras(texto))
