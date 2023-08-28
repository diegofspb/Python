#1. Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado “calcular_area” que retorna a área do círculo.

class Circulo:    

    def __init__(self, raio):        
        self.raio = raio        

    def calcular_area(self):
        pi = 3.14
        area = pi * (self.raio ** 2)
        return area
        
a = Circulo(3)
print(a.calcular_area())

            
        
