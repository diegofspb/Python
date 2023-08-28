#7. Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. Implemente um método
#chamado “detalhes” que retorna uma string com as informações do carro.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        mensagem = f'Marca do carro= {self.marca}\nModelo = {self.modelo}\nAno= {self.ano}'
        return mensagem

carro1 = Carro('fiat', 'uno', 1940)

print(carro1.detalhes())