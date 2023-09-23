import numpy as np

#regras de 'fila':

    # a fila aqui é representada por uma lista com tamanho fixo representado por 'capacidade'
    # quando for incluído um elemento na lista, o novo elemento sempre irá para ultima posição
    # o primeiro elemento incluído na lista será o primeiro a ser retirado
    # quando um elemento é retirado da lista, sua posição é desconsiderada e a posição inicial representada por self.incio é interado +1 

#     exemplo:

#             lista ( a, b, c)   -> lista com CAPACIDADE = 3 elementos e contendo 3 elementos
# posições/indices    0  1  2

# exemplo: retira-se a letra 'a' que está na posição self.inicio = 0, então o self.inicio é interado +1 e passa a ser = 1, ou seja, o inicío agora é posição do 'b' ficando:

#             lista ( vazio, b, c)   -> lista com CAPACIDADE = 3 elementos e contendo 2 elementos
# posições/indices      0    1  2

# no código abaixo, quando se chega ao fim da lista = lista cheia, então tudo volta para o início representando um loop

class fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0 # posição do PRIMEIRO elemento da fila, apenas será usado na função 'desenfileirar'
        self.final = -1 # posição do ultimo elemento da fila, apenas será usado na função 'enfileirar'
        self.numero_elementos = 0  # contador de elementos
        self.valores = np.empty(self.capacidade, dtype=int) #biblioteca que cria uma lista vazia, que instalar usando o comando: pip install numpy

    def fila_vazia(self):
        return self.numero_elementos == 0

    def fila_cheia(self): #esta condição verifica se a fila está cheia, caso afirmativo não permite adição de numeros na fila
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor): # é responsável por adicionar um elemento à fila.
        if self.fila_cheia():
            print('A fila está cheia')
            return
        #self.final inicia com valor -1 , e capacidade por exemplo se for 2, então aqui ficará '-1 == 1 ?' e o loop só funcionará 2 vezes, pois o self.final vai andando
        # somando +1 por ciclo andando  -1, 0, 1 finalmente se igualiando ao self.capacidade que neste exemplo = 2 e no if abaixo sofre a diminuição, ficando 2-1 = 1
        if self.final == self.capacidade - 1:  
            self.final = -1
        self.final += 1 # quando chega aqui o self.final ganhar +1 e vai para o valor 0, pois -1 + 1 = 0
        self.valores[self.final] = valor # self.valores (lista de valores), recebe o primeiro valor na posição 0, depois na proxima interação receberá 1 e assim por diante
        self.numero_elementos += 1 

    def desenfileirar(self): # é responsável por remover o elemento da frente da fila (o primeiro elemento inserido)
        if self.fila_vazia():
            print('A fila já está vazia')
            return  
        #self.inicio inicia com valor 0 e não foi usado nenhuma vez nos códigos acima
        temp = self.valores[self.inicio] # a ideia é lançar isso no return, para mostrar o elemento que saiu da lista, pois o primeiro a entrar = ultimo a sair
        self.inicio += 1 #a ideia agora é que a posição inicial deixe de ser 0 que agora foi 'retirado da fila' e passe a ser 1 e assim por diante 
        if self.inicio == self.capacidade - 1:  #quando a posição inicial for exatamente a ultima posição, quer dizer que a lista foi 
            # enchida e depois esvaziada e agora volta para o 0 gerando uma espécie de loop
            self.inicio = 0 # self.inicio retorna a posição 0 e passa a sobrescrever o primeiro de novo gerando um loop
        else:
            self.numero_elementos -= 1
            return temp

    def primeiro(self):
        if self.fila_vazia():
            return -1
        else:
            return self.valores[self.inicio]

    def visualizar(self):
      print('Tamanho da Fila..: ', self.capacidade)
      print('Início da fila...: ', self.inicio)
      print('Final da fila....: ', self.final)
      print('Variável Nu. El..:', self.numero_elementos)
    
    def listageral(self):
      for i in range(self.capacidade):
        print(self.valores[i])


fila1 = fila(6)
fila1.enfileirar(9)
fila1.enfileirar(8)
fila1.enfileirar(2)
fila1.enfileirar(1)
fila1.enfileirar(5)
fila1.enfileirar(7)

print('================')
print('O primeiro da fila..: ',fila1.primeiro())
fila1.visualizar()
fila1.desenfileirar()
fila1.desenfileirar()
fila1.desenfileirar()
fila1.enfileirar(4)
print('================')
print('O primeiro da fila..: ',fila1.primeiro())
fila1.visualizar()