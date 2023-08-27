print('#'*30)
print('Aluguel de Veículos')
print('#'*30)

print('Veículos disponíveis para alugar')
print('[1] Carro')
print('[2] Moto')
print('[3] Bicicleta')

veiculo = int(input('Escolha uma opção: '))
km = int(input('Quantos Quilômetros você deseja percorrer? '))
print('\n')

if (veiculo==1 or veiculo==2 or veiculo==3):

    if veiculo==1:
        print('Você escolheu um Carro!')
        print('O valor da km é R$1,27')
        preco = km*1.27           
    elif veiculo==2:
        print('Você escolheu uma Moto!')
        print('O valor da km é R$0,97')
        preco = km*0.97

    elif veiculo==3:
        print('Você escolheu uma Bicicleta!')
        print('O valor da km é R$0,23')
        preco = km*0.23

else:
    print('\n')
    print('Você não digitou uma opção válida tente novamente !')    
    print('\n')

round(preco,2)
print(f'Total do aluguel: R$ {preco}') 


