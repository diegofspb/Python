def selecao_ordenacao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

def encontrar_segundo_menor(vetor):
    selecao_ordenacao(vetor)
    resp=vetor[1]
    if vetor[0]==vetor[1]:
        resp=vetor[2]
    return resp

vetor=[5,7,3,3]
print(encontrar_segundo_menor(vetor))
print(vetor)