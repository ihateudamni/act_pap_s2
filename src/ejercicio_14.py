def sistema_votacion():
    votos = set()
    while True:
        voto = input("Ingrese candidato ('fin' para terminar): ")
        if voto.lower() == 'fin':
            break
        votos.add(voto)
    print("Candidatos votados:", votos)

sistema_votacion()
