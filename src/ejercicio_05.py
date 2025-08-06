def buscar_palabras(lista_palabras, letra):

    resultado = []
    for palabra in lista_palabras:
        for caracter in palabra:
            if caracter.lower() == letra.lower():
                resultado.append(palabra)
                break
    return resultado

palabras = ["perro", "gato", "casa", "mesa", "avión"]
letra = input("Ingrese la letra a buscar: ")
print("Palabras que contienen la letra:", buscar_palabras(palabras, letra))
