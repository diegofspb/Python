#4. Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente
# métodos “depositar” e “sacar” para manipular o saldo.

class ContaBancaria:

    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
    
    def depositar(self, deposito):
        self.saldo = self.saldo + deposito
        return self.saldo 
       
    def sacar(self, saque):
        self.saldo = self.saldo - saque
        return self.saldo
    
conta = ContaBancaria(10, 'JOÃO')

novoSaldo = conta.depositar(10)
print(f'Após o depósito, novo saldo = {novoSaldo}')

novoSaldo = conta.sacar(30)
print(f'Após o saque, novo saldo = {novoSaldo}')