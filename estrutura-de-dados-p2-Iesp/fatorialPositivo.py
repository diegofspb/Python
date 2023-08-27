# 6. Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse número.

numero = int(input("Digite um número que é inteiro e positivo: "))

if numero < 0:
    print("O número tem que ser positivo.")
else:   
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}")
