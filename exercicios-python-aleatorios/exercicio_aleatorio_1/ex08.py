
print('*'*50)
print('Palindromo')
print('*'*50)

palindromo = input('Escreva uma palavra para ver se é palindromo\n')

if palindromo==palindromo[::-1]:
    print(f'A palavra {palindromo} é um PALINDROMO')
else:
    print(f'A palavra {palindromo} NÃO é um PALINDROMO')