import numpy as np

class fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def fila_vazia(self):
        return self.numero_elementos == 0

    def fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.fila_cheia():
            print('A fila está cheia')
            return
        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.fila_vazia():
            print('A fila já está vazia')
            return
        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade - 1:
            self.inicio = 0
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

print('O primeiro da fila..: ',fila1.primeiro())
print('================')
fila1.visualizar()
fila1.desenfileirar()
fila1.desenfileirar()
fila1.desenfileirar()
fila1.enfileirar(4)
print('O primeiro da fila..: ',fila1.primeiro())
fila1.visualizar()