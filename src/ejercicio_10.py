def sumar_tuplas(t1, t2):
    resultado = []
    for i in range(len(t1)):
        resultado.append(t1[i] + t2[i])
    return tuple(resultado)

print("Suma:", sumar_tuplas((1,2,3), (4,5,6)))