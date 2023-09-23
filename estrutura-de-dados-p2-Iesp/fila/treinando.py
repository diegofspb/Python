import numpy as py

class fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = py.empty(self.capacidade, dtype=int)
    
    def fila_vazia(self):
        return self.numero_elementos == 0
    def fila_cheia(self):
        return self.capacidade == self.numero_elementos
    
    def enfileirar(self, valor):
        if self.fila_cheia():
            print("A fila está cheia")
            return 
        if self.final == self.capacidade -1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self, valor):
        if self.fila_vazia():
            return print("A fila está vazia")
        if self.inicio == self.capacidade-1:
            self.inicio = 0 
        self.inicio += 1
        self.numero_elementos -= 1 

    def verLista(self):
        for i in range(self.capacidade):
            print(self.valores[i])      


    def visualizar(self):
      
      print('Capacidade da Fila..: ', self.capacidade)
      print('Posição inicial da fila...: ', self.inicio)
      print('Posição Final da fila....: ', self.final)
      print('Numero de elementos..:', self.numero_elementos)
      print("*"*5)
    

fila1 = fila(5)
print("apenas exibindo a lista vazia")

fila1.verLista()
print("executando o enfileirar")
fila1.enfileirar(1)
fila1.visualizar()

fila1.desenfileirar(4)


fila1.desenfileirar(5)

print("executando o enfileirar")
fila1.enfileirar(6)
fila1.enfileirar(2)
fila1.enfileirar(8)
fila1.enfileirar(9)
fila1.visualizar()
fila1.desenfileirar(5)
fila1.verLista()


