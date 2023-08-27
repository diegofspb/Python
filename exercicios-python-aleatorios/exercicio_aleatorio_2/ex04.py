'''Dado uma lista de strings, crie um algoritmo que retorne a lista de strings ordenada por ordem
decrescente de tamanho.
Exemplo de entrada: ['casa', 'carro', 'abacate', 'pipoca']
Saída esperada: ['abacate', 'carro', 'casa', 'pipoca']'''

lista = ['casa', 'carro', 'abacate', 'pipoca']
nova_lista = []

for i in range(len(lista)):
    if len(lista[i])>len(lista[i-1]):
        nova_lista.insert(0,lista[i])
    else:
        nova_lista.append(lista[i])      

print(nova_lista)

