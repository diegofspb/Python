'''5. Dado uma tupla de tuplas, onde cada tupla interna representa um intervalo de tempo (horário de início
e horário de término), crie um algoritmo que retorne a quantidade de horas total dos intervalos.
Exemplo de entrada: ((8, 12), (14, 18), (19, 22))
'''

horas = ((8, 12), (14, 18), (19, 22))
soma = 0

for i in horas:
    soma += (i[1]-i[0])

print(soma)