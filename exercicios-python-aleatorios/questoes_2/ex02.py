'''2. Faça um algoritmo para ler 10 números e armazenar em um vetor VET, verificar e escrever se existem
números repetidos no vetor VET e em que posições se encontram.'''

import random

numeros = []

for i in range(0,10):
    numero = random.randint(1,10)
    numeros.append(numero)

numero_repetido = []

for numero in numeros:
    if numeros.count(numero)>1 and numero not in numero_repetido:    
        numero_repetido.append(numero)                 
        print(f'O número {numero} foi repetido {numeros.count(numero)} vezes e ocupa a posição \'{numeros.index(numero)}\' no vetor')

        