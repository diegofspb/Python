print('*'*50)
print('Programa que calcule a média aritmética de 4 notas e informe se o aluno foi aprovado (média maior ou igual a 7) ou reprovado.')
print('*'*50)

nome = input('Informe o nome do Aluno\n')
n1 = int(input('Informe a PRIMEIRA nota!\n'))
n2 = int(input('Informe a SEGUNDA nota!\n'))
n3 = int(input('Informe a TERCEIRA nota!\n'))
n4 = int(input('Informe a QUARTA nota!\n'))

media = (n1+n2+n3+n4)/4

if media>=7:
    print(f'O aluno {nome} possui média {media} e está APROVADO\n')
else:
    print(f'O aluno {nome} possui média {media} e está REPROVADO\n')