
print('*'*50)
print('Aumento de salário')
print('*'*50)

salario = float(input('Informe o valor do seu salário!\n'))

if salario>=1500:
    salario = salario+(salario/10)
    round(salario,2)
    print(f'O novo salário com aumento de 10% é {salario}')
else:
    salario = salario+(salario/15)
    round(salario,2)
    print(f'O novo salário com aumento de 15% é {salario}')