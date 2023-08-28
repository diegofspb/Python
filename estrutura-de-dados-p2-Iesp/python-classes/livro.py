#2. Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método
#chamado “detalhes” que retorna uma string com as informações do livro.

class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return print(f"O título: \'{self.titulo}\'\nAutor: \'{self.autor}\'")    
    
livro1 = Livro('O sonhador', 'EU')

livro1.detalhes()
