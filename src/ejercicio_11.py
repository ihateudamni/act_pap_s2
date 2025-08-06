def operaciones_conjuntos(lista1, lista2):
    c1 = set(lista1)
    c2 = set(lista2)
    return c1 | c2, c1 & c2, c1 - c2, c1 ^ c2

union, interseccion, diferencia, dif_sim = operaciones_conjuntos([1,2,3,4], [3,4,5,6])
print("Unión:", union)
print("Intersección:", interseccion)
print("Diferencia:", diferencia)
print("Diferencia simétrica:", dif_sim)
