def inventario_productos():
    inventario = {}
    while True:
        print("\n1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        
        opcion = input("Seleccione opción: ")
        
        if opcion == "1":
            producto = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            inventario[producto] = cantidad
        
        elif opcion == "2":
            producto = input("Producto a actualizar: ")
            if producto in inventario:
                cantidad = int(input("Nueva cantidad: "))
                inventario[producto] = cantidad
        
        elif opcion == "3":
            producto = input("Producto a eliminar: ")
            inventario.pop(producto, None)
        
        elif opcion == "4":
            print(inventario)
        
        elif opcion == "5":
            break

inventario_productos()
