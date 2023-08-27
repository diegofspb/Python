'''11. Dado uma lista de strings, crie um algoritmo que retorne a palavra mais frequente na lista.
Exemplo de entrada: ['azul', 'vermelho', 'verde', 'azul', 'vermelho', 'amarelo', 'azul']
Saída esperada: 'azul'''


cores_list = ['azul', 'vermelho', 'verde', 'azul', 'vermelho', 'amarelo', 'azul']
cores_dict = {}

for cor in cores_list:    
    cores_dict[cor] = cores_list.count(cor)

sorted_dict = dict(sorted(cores_dict.items(), key=lambda item: item[1], reverse=True))

for cor,quantidade in sorted_dict.items():    
    resposta = 'A cor {} é a cor que aparece mais vezes, ou seja, {} ocorrências'.format(cor, quantidade)
    break

print(resposta)
