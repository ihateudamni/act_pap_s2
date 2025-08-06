def carrito_compras():
 
    carrito = []
    
    while True:
        print("\n--- Carrito de Compras ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar productos")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            producto = input("Ingrese producto: ")
            carrito.append(producto)
            print(f"{producto} agregado al carrito.")
        
        elif opcion == "2":
            producto = input("Ingrese producto a eliminar: ")
            if producto in carrito:
                carrito.remove(producto)
                print(f"{producto} eliminado.")
            else:
                print("Producto no encontrado.")
        
        elif opcion == "3":
            print("Carrito actual:", carrito)
        
        elif opcion == "4":
            print("Saliendo del carrito.")
            break
        
        else:
            print("Opción inválida.")

carrito_compras()
