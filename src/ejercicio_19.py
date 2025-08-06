def gestion_calificaciones():
    calificaciones = {}
    while True:
        print("\n1. Agregar estudiante")
        print("2. Agregar calificación")
        print("3. Calcular promedio")
        print("4. Salir")
        
        opcion = input("Seleccione opción: ")
        
        if opcion == "1":
            estudiante = input("Nombre del estudiante: ")
            calificaciones[estudiante] = []
        
        elif opcion == "2":
            estudiante = input("Estudiante: ")
            if estudiante in calificaciones:
                nota = float(input("Calificación: "))
                calificaciones[estudiante].append(nota)
        
        elif opcion == "3":
            estudiante = input("Estudiante: ")
            if estudiante in calificaciones and calificaciones[estudiante]:
                promedio = sum(calificaciones[estudiante]) / len(calificaciones[estudiante])
                print(f"Promedio: {promedio:.2f}")
        
        elif opcion == "4":
            break

gestion_calificaciones()
