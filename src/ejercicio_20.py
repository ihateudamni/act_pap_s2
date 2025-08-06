def sistema_temperaturas():
    temperaturas = {}
    while True:
        print("\n1. Agregar ciudad")
        print("2. Agregar temperatura")
        print("3. Mostrar estadísticas")
        print("4. Salir")
        
        opcion = input("Seleccione opción: ")
        
        if opcion == "1":
            ciudad = input("Nombre de la ciudad: ")
            temperaturas[ciudad] = {}
        
        elif opcion == "2":
            ciudad = input("Ciudad: ")
            if ciudad in temperaturas:
                dia = input("Día de la semana: ")
                temp = float(input("Temperatura: "))
                temperaturas[ciudad][dia] = temp
        
        elif opcion == "3":
            for ciudad, datos in temperaturas.items():
                if datos:
                    promedio = sum(datos.values()) / len(datos)
                    print(f"{ciudad} - Promedio: {promedio:.2f}°C")
        
        elif opcion == "4":
            break

sistema_temperaturas()
