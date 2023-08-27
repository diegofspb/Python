#7. Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário.
#Fibonacci o numero é o resultado da soma dos dois antecessores

numeroFinal = int(input("Digite um valor limite para contagem em fibonacci: ")) 

primeiroNumero = 0
segundoNumero = 1

for i in range(0, numeroFinal+1):

    print(primeiroNumero)
    terceiroNumero = primeiroNumero + segundoNumero   
    primeiroNumero = segundoNumero
    segundoNumero = terceiroNumero
    





