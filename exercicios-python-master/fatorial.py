# 2. Crie uma função chamada "calcula_fatorial" que receba um número inteiro como parâmetro e retorne
# o seu fatorial. O fatorial de um número é o produto de todos os números inteiros de 1 até o próprio
# número.


def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)


numero = 8

resultado = fatorial(8)

print(f'O fatorial de {numero} é {resultado}')