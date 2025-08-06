def filtrar_estudiantes(estudiantes):
    filtrados = []
    for nombre, edad, promedio in estudiantes:
        if promedio > 8.0:
            filtrados.append((nombre, edad, promedio))
    return tuple(filtrados)

datos = (("Ana", 20, 9.1), ("Luis", 22, 7.8), ("Marta", 21, 8.5))
print("Estudiantes filtrados:", filtrar_estudiantes(datos))
