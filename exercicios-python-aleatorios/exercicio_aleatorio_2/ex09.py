'''9. Dado uma lista de tuplas, onde cada tupla representa um ponto no espaço tridimensional (coordenadas
x, y e z), crie um algoritmo que retorne a distância total percorrida ao conectar todos os pontos na
ordem em que aparecem na lista.
Exemplo de entrada: [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
Saída esperada: 9.48 (aproximadamente)
'''

import math

pontos = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

distancia_total = 0
for i in range(len(pontos) - 1):
    x1, y1, z1 = pontos[i]
    x2, y2, z2 = pontos[i + 1]
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    distancia_total += d

print(distancia_total)