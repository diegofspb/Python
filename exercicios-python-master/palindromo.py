print('#'*30)
print('Palindromo sem atalhos')
print('#'*30)
print('\n')

palavra = input('Digite uma palavra para saber se é PALÍNDROMO\n').strip().upper()
inverso = ''
for letra in range(len(palavra)-1, -1, -1):
    inverso += palavra[letra]

if palavra==inverso:
    print(f'{palavra} é PALÍNDROMO')
else:
    print(f'{palavra} NÃO é PALÍNDROMO')



    