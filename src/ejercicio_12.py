def palabras_unicas():
    palabras = set()
    repetidas = set()
    
    while True:
        entrada = input("Ingrese palabra ('salir' para terminar): ")
        if entrada.lower() == 'salir':
            break
        if entrada in palabras:
            repetidas.add(entrada)
        palabras.add(entrada)
    
    print("Palabras únicas:", palabras)
    print("Repetidas:", repetidas)

palabras_unicas()
