# Programa que itera sobre una tupla de coordenadas
coordenadas = ((1, 2), (3, 4), (5, 6))

for coordenada in coordenadas:
    # usando el desempaquetado de tuplas se asigna los valores a X & Y
    x, y = coordenada
    print("Coordenada:", coordenada)
    print("Valor de x:", x)
    print("Valor de y:", y)
    print("---")

print("¡Bucle for completado!")
