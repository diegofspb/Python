#8. Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado
#“calcular_media” que retorna a média das notas do aluno.

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas   
     
    def calcular_media(self):
        total = 0.0
        for nota in self.notas:
            total += nota
        media = total / len(self.notas)
        return media

aluno1 = Aluno("João", [2.5, 4.2, 5.2, 8.8, 3.0])

media = aluno1.calcular_media()

print(f"A média das notas de {aluno1.nome} é: {media:.2f}")
