'''1. Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20
números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.
'''
numeros = []
for numero in range(1,21):
    numeros.append(numero)

print(numeros[::-1])

