#6. Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um
#método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade
    
    def exibirMensagem(self):
        mensagem = f'Quero comprar uma {self.nome}, valor = {self.preco} e comprando {self.quantidade} o total fica= '
        return mensagem
    
produto1 = Produto('cadeira', 43, 2)

print(produto1.exibirMensagem(), produto1.calcular_total())

