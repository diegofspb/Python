#2. Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.


numero = float(input("Digite um número para saber se é Par ou Impar :"))

if numero%2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é Impar')
