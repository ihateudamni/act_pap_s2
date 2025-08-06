def agenda_telefonica():
    agenda = {}
    while True:
        print("\n1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos")
        print("4. Eliminar contacto")
        print("5. Salir")
        
        opcion = input("Seleccione opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            agenda[nombre] = telefono
        
        elif opcion == "2":
            nombre = input("Nombre a buscar: ")
            print(agenda.get(nombre, "No encontrado"))
        
        elif opcion == "3":
            print(agenda)
        
        elif opcion == "4":
            nombre = input("Nombre a eliminar: ")
            agenda.pop(nombre, None)
        
        elif opcion == "5":
            break

agenda_telefonica()
