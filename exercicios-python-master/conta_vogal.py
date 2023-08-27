# 1. Escreva uma função chamada "conta_vogais" que receba uma string como parâmetro e retorne o
# número de vogais presentes nessa string. Considere que a string pode conter letras maiúsculas e
# minúsculas.

nome = 'diego'

def conta_vogais(nome):
    contador = 0
    nome.upper()
    for i in nome:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            contador += 1
    print(f'A palavra {nome} porrui {contador} vogais')


conta_vogais('teste_nome_com_vogais_para_contar')


