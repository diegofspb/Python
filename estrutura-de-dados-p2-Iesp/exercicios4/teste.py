# 6. Escreva um programa que ordene um vetor de inteiros em ordem decrescente e, em seguida, conte
# quantos números pares e quantos números ímpares existem no vetor ordenado.

def numOrdenado(vetor):
    n = len(vetor)    
    for i in range(n):
        for j in range(n):
            if vetor[i] > vetor[j]:
                temp, vetor[i] = vetor[i], vetor[j]
                vetor[j] = temp
    return print("Numeros Ordenados = " + str(vetor))

def contParImpar(vetor):
    par = 0
    impar = 0
    for numero in vetor:
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1
    return print("Numero par = " + str(par) + " Numero impar = " + str(impar))

lista = [6,2,8,1,5]

numOrdenado(lista)
contParImpar(lista)


