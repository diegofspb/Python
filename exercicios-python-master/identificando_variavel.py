#Este programa identifica o tipo da variável, se possui: espaços/numero/alfanumerico/maiusculo/minusculo/capitalizado, 

palavra = input('Informe uma palavra\n')

print(f'A Palavra que você digitou foi = {palavra} e o tipo primitivo dela é =', type(palavra))
print(f'O que você digitou possui espaço vazio ? =', palavra.isspace())
print(f'é um número ? =', palavra.isnumeric())
print(f'é alfabético? =', palavra.isalpha())
print(f'é ALFANUMÉRICO =', palavra.isalnum())
print('está em mainúsculo ? =', palavra.isupper())
print('está em minusculo ? =', palavra.islower())
print(f'é capitalizada ? =', palavra.istitle())

