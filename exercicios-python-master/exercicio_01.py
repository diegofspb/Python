# Desenvolva um programa que verifique e mostre os números entre 1.000 e 2.000 que, quando
# divididos por 11, produzam o resto igual a 5.

lista = []

for numero in range(1000,2000,1):
    if numero%11==5:        
        lista.append(numero)
    
print(f'\nA lista dos números que dividios por 11 produzem resto 5 é o total de {len(lista)} números, sendo eles:\n {lista} ')

