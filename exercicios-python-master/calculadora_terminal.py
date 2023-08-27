print('*'*10,'Caculadora','*'*10,'\n' )

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

escolha = input('Escolha uma opção: \n1 - Somar\n2 - Diminuir\n3 - Multiplicar\n4 - Dividir\n')


if escolha == '1':        
    operacao = '+'       
    resultado = n1+n2
elif escolha=='2':
    operacao = '-'
    resultado = n1-n2
elif escolha=='3':
    operacao = 'x'
    resultado = n1*n2
elif escolha=='4':
    operacao = '/'    
    resultado = n1/n2

print(f'Calculo: {n1} {operacao} {n2} = {round(resultado,2)}\n')