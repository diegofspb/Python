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

        aux = vetor[i] # preserva a posição atual do vetor para não ser colocado em outra posição evitando ser sobrescrito/perdido
        vetor[i] = vetor[indice_minimo] #posição do vetor vai caminhando, da posição 0 até a len(vetor)
        vetor[indice_minimo] = aux # quando encontrado o menor número da sequencia, ele é salvo na posição inical a posição que ele saiu recebe a posição maior

vetor=[5,7,4,3]
selecao_ordenacao(vetor)
print(vetor)