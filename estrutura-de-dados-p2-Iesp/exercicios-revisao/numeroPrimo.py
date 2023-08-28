# 8. Faça um programa que determine se um número é primo ou não.

numero = int(input("Digite um número: "))
contador = 0

for i in range(1, numero+1):
    if numero % i == 0:
        print(f'O número {numero} é divisível por {i}')
        contador += 1
    
if contador ==2:
    print(f'O numero {numero} é primo, pois só pode ser divido por dois numeros, 1 e ele mesmo')
else:
    print(f'O número {numero} não é primo, pois é divisível por {contador} numeros')