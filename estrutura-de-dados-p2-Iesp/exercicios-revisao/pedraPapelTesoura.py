#10. Crie um programa que simule o jogo "1, 2 e 3" entre o usuário e o computador. O
#programa deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do
#computador e determinar o vencedor.

import random

print(10*'#','Jogo de Pedra Papel e Tesoura',10*'#', end='')
print('Escolha uma das opções abaixo: ')
usuario = int(input('(1) - 1\n(2) - 2\n(3) - 3.\n '))
computador = random.randint(1,3)
# Escolha do usuário
if usuario == 1:
    escolhaUsuario = 'pedra'
elif usuario == 2:
    escolhaUsuario = 'papel'
elif usuario == 3:
    escolhaUsuario = 'tesoura'
# Escolha do Computador
if computador == 1:
    escolhaComputador = 'pedra'
elif computador == 2:
    escolhaComputador = 'papel'
elif computador == 3:
    escolhaComputador = 'tesoura'
#lógica do jogo
if escolhaUsuario == escolhaComputador:
    print(f'Empate, os dois escolheram: {escolhaUsuario}')
elif escolhaUsuario == 'pedra':
    if escolhaComputador == 'papel':
        print(f"O usuário escolheu {escolhaUsuario} e o computador escolheu {escolhaComputador}, então o ** Computador Vence! ** ")
    else:
        print(f"O usuário escolheu {escolhaUsuario} e o computador escolheu {escolhaComputador}, então o ** Usuário Vence! ** ")
elif escolhaUsuario == 'papel':
    if escolhaComputador == 'tesoura':
        print(f"O usuário escolheu {escolhaUsuario} e o computador escolheu {escolhaComputador}, então o ** Computador Vence! ** ")
    else:
       print(f"O usuário escolheu {escolhaUsuario} e o computador escolheu {escolhaComputador}, então o ** Usuário Vence! ** ")
elif escolhaUsuario == 'tesoura':
    if escolhaComputador == 'pedra':
        print(f"O usuário escolheu {escolhaUsuario} e o computador escolheu {escolhaComputador}, então o ** Computador Vence! ** ")
    else:
       print(f"O usuário escolheu {escolhaUsuario} e o computador escolheu {escolhaComputador}, então o ** Usuário Vence! ** ")
else:
    print("Escolha errada!\n Digite: (1) - 1\n(2) - 2\n(3) - 3")
