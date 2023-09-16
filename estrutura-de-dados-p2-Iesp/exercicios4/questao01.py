def selecao_ordenacao(vetor):
    n = len(vetor)
    for i in range(n):

        indice_minimo = i

        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j  # no primeiro ciclo o 'i' sempre é = 0 e o 'n' percorre todos os numeros do vetor,
                                   # ou seja, o indice_minimo salvará a posição [j] que contém o menor número de todo vetor
                                   # caso o menor número esteja na posição 0 que é a posição do [i], então o indice_minimo 
                                   # ficará com o valor padrão que é o próprio [i], conforme atribuição na linha 5

        aux = vetor[i] # guarda a posição atual 'i' que está sendo comparada com a proxima posição i+1 
        vetor[i] = vetor[indice_minimo] #posição atual 'i' recebe o menor valor do vetor que foi encontrado através do indice_minimo = j
        # isso vai caminhando, primeiro compara posição i=0 e procura o menor valor e salva na posição 0, depois i=1 e por ai vai até terminar
        vetor[indice_minimo] = aux # aux está com o vetor atual vetor[i], caso ele não seja o menor da posição atual 

vetor=[5,7,4,3]
selecao_ordenacao(vetor)
print(vetor)