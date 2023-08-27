print('#'*30)
print('Transformar uma string em lista com split() e contas quantos indices tem uma lista com len()')
print('#'*30)
print('\n')

frase = 'banana, uva, melancia'.upper()
lista = frase.split(',') #o que colocar dentro do split será excluido da lista, caso contrário a lista terá 2 virgulas

print('A primeira palavra é {} e a ultima é{}'.format(lista[0], lista[len(lista)-1]))
