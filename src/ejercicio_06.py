import random
import math

def coordenadas_aleatorias():
    puntos = [(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(10)]
    dentro_circulo = []
    for x, y in puntos:
        if math.sqrt(x**2 + y**2) <= 5:
            dentro_circulo.append((x, y))
    return puntos, dentro_circulo

puntos, dentro = coordenadas_aleatorias()
print("Puntos:", puntos)
print("Dentro del círculo:", dentro)
