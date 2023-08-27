print('#'*30)
print('Realizar uma pesquisa dentro de uma String')
print('#'*30)
print('\n')

frutas = str(input('Informe o nome de algumas frutas separadas por vírgula: ')).strip(',')

print('Existe a fruta UVA na variável do tipo string frutas ?: ',format('uva' in frutas))

#Resposta do format() será booleano