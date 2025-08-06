def eliminar_duplicados(lista):
    conjunto = set(lista)
    duplicados = len(lista) - len(conjunto)
    return conjunto, duplicados

resultado, cantidad = eliminar_duplicados([1,2,2,3,4,4,5])
print("Sin duplicados:", resultado)
print("Cantidad de duplicados:", cantidad)
