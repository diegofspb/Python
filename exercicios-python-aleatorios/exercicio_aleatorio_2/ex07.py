'''7. Dado duas listas, crie um algoritmo que retorne a interseção dos elementos das duas listas (ou seja, os
elementos que aparecem nas duas listas).
Exemplo de entrada: [1, 2, 3, 4], [3, 4, 5, 6]
Saída esperada: [3, 4]
'''

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
nova_lista = []

for i in range(len(lista1)):
    if lista1[i] in lista2:
        nova_lista.append(lista1[i])

print(nova_lista)


