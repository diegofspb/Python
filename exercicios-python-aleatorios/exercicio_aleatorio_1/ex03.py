print('*'*50)
print('Programa que solicite o nome e a idade do usuário e informe se ele pode dirigir um veículo')
print('*'*50)

nome = input('Informe seu nome!')
idade = int(input('Informe sua idade!'))


if idade>=18:
    print(f'{nome} é maior de idade e pode conduzir um veículo')
else:
    print(f'{nome} é menor de idade e não pode conduzir um veículo')