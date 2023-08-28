#3. Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até esse número.

numero = int(input("Informe um número para contarmos até ele :"))

for numeroPar in range(0, numero):
    if numeroPar%2 == 0 and numeroPar > 0:
        print(numeroPar)