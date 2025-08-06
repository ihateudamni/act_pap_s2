def combinar_listas(lista1, lista2):

    combinada = []
    for i in range(len(lista1)):
        combinada.append(lista1[i])
        combinada.append(lista2[i])
    return combinada

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
print("Lista combinada:", combinar_listas(l1, l2))
