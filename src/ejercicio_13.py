def generar_conjuntos():
    pares = {x for x in range(2, 21, 2)}
    multiplos3 = {x for x in range(3, 31, 3)}
    return pares, multiplos3, pares | multiplos3, pares & multiplos3, pares - multiplos3

pares, multiplos3, union, inter, dif = generar_conjuntos()
print("Pares:", pares)
print("Múltiplos de 3:", multiplos3)
print("Unión:", union)
print("Intersección:", inter)
print("Diferencia:", dif)
