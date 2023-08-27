#9. Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que começam com a letra 'A'.

nomes = ['ana', 'maria', 'joao', 'astronalta']
novaLista = []

for nome in nomes:
    if nome.startswith('a'):
        novaLista.append(nome)

print(novaLista)