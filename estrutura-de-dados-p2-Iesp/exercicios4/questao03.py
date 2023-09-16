# 3. Escreva um programa que encontre o elemento máximo em um vetor de inteiros não ordenado sem
# usar a função `max()`. Em seguida, encontre o elemento mínimo sem usar a função `min()`.

def encontrar_maximo(vetor):
    maximo = vetor[0]
    for elemento in vetor:
        if elemento > maximo:
            maximo = elemento
    return maximo

def encontrar_minimo(vetor):
    minimo = vetor[0]
    for elemento in vetor:
        if elemento < minimo:
            minimo = elemento
    return minimo

def encontrar_max_min(vetor):
    minimo = vetor[0]
    maximo = vetor[0]
    for elemento in vetor:
        if elemento < minimo:
            minimo = elemento
        if elemento > maximo:
            maximo = elemento
    return maximo, minimo

vetor=[5,7,4,3]
print(encontrar_maximo(vetor))
print(encontrar_minimo(vetor))
#resp=encontrar_max_min(vetor)
#print(resp[0], resp[1])
