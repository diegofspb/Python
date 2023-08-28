#3. Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método
#chamado “calcular_area” que retorna a área do retângulo.

class AreaRetangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        area = (self.base * self.altura) / 2
        return area
    
retangulo1 = AreaRetangulo(2,5)

print(f'A area de um retangulo com tamanho 2 e 5 é: {retangulo1.area()}')

