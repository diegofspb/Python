#5. Faça um programa que leia uma lista de números e retorne a média dos números pares.


listaNumeros = [52,22,35,45,844,115,2112]

numeroPar = 0
contador = 0

for i in listaNumeros:
    if i %2 == 0:
        numeroPar += i
        contador += 1 

media = numeroPar / contador

print('A média dos números pares é =', media)