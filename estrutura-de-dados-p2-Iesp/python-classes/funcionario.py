# 10. Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um
# método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário
# do funcionário.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def aumentar_salario(self, aumento):
        self.salario = (self.salario * aumento)/100 + self.salario
        return self.salario
    
    def mensagem_sem_aumento(self):
        mensagem = f'{self.nome} é {self.cargo} e recebe um salário de R$ {self.salario}'
        return mensagem

    def mensagem_com_aumento(self):
        mensagem = f'{self.nome} recebeu um aumento e seu novo salário é = R$ {self.salario}'
        return mensagem
    
funcionario1 = Funcionario('João', 100, 'professor')

print(funcionario1.mensagem_sem_aumento())
funcionario1.aumentar_salario(20)
print(funcionario1.mensagem_com_aumento())
    