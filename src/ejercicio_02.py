def sistema_calificaciones():

    calificaciones = []
    
    while True:
        entrada = input("Ingrese calificación: ")
        if entrada.lower() == 'fin':
            break
        try:
            nota = float(entrada)
            calificaciones.append(nota)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"Promedio: {promedio:.2f}")
        print(f"Nota más alta: {max(calificaciones)}")
        print(f"Nota más baja: {min(calificaciones)}")
    else:
        print("No se ingresaron calificaciones.")

sistema_calificaciones()
