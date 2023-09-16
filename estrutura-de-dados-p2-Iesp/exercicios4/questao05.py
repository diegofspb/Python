# 5. Implemente uma função que aceite um vetor de números inteiros e remova todos os elementos
# duplicados, retornando o vetor resultante sem duplicatas.

def numeroOrdenado(vetor):    
    n = len(vetor)
    for i in range(n):
        for j in range(n):           
            if vetor[i] < vetor[j]:
                temp, vetor[i] = vetor[i], vetor[j]
                vetor[j] = temp
    return vetor

def removerDuplicados(vetor):
    novoVetor = []
    for numero in vetor:
        if numero not in novoVetor:
            novoVetor.append(numero)
    return novoVetor

vetor = [3,5,5,7,2]

ordenado = numeroOrdenado(vetor)
removerNumeroDuplicado = removerDuplicados(ordenado)
print(removerNumeroDuplicado)
