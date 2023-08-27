'''Dado uma lista de números, crie um algoritmo que retorne a soma dos números pares na lista.
Exemplo de entrada: [1, 2, 3, 4, 5, 6]
Saída esperada: 12'''

import random

soma = 0
numeros = []

for i in range(20):
    numero = random.randint(0,20)
    if numero%2==0:
        numeros.append(numero)
        soma += numero

print(f'A soma dos números pares: {numeros} = {soma}')
    
