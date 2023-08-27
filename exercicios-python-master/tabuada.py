print('#'*20)
print('Tabuada')
print('#'*20)
print('#'*20)

numero = int(input('Informe um número para saber sua TABUADA \n'))
print('-'*20)
print(f'A tabuada de {numero} é: ')
a = 0
while a<10:
    a+=1
    multiplicar = numero*a    
    print(f'=> {numero} x {a} = {multiplicar}')

print('-'*20)


