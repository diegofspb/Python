print('#'*30)
print('Deletar espaços vazios + encontrar a primeira e ultima posição que aparece uma letra/palavra')
print('#'*30)
print('\n')

frase = input('Informe uma frase para saber o índice que está a primeira e ultima letra A\n').upper().strip()
# foi utilizado o .upper() pois caso a frase digitada esteja em minusculo, irá tudo para maiusculo ou vice/versa
# foi utilizado o .strip() para apagar os espaços vazios antes e depois do que for digitado!

print('Letra A aparece na PRIMEIRA posição = {} '.format(frase.find('A')))
print('Letra A aparece na ULTIMA posição = {} '.format(frase.rfind('A')))