#4. Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.

listaNumeros = [5,4,8,11,55,2]

listaNumeros.sort()

print(f'O menor número da lista é {listaNumeros[0]} e o maior é {listaNumeros[len(listaNumeros)-1]}')