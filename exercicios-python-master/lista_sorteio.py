import random

print('#'*30)
print('Lista de Sorteio de Nomes')
print('#'*30)

def menu():    
    print('[1] - Incluir um nome')
    print('[2] - Sortear')
    print('[3] - Exibir lista')
    print('[4] - Sair') 
    print('\n')  
    
condicao = True
nomes = []

while condicao:

    print('\n') 
    menu()
    opcao = int(input('Escolha a Opção: '))

    if opcao==1 or opcao==2 or opcao==3 or opcao==4:

        if opcao==1:
            nome = input('Digite um nome: ')
            nomes.append(nome)
            print(f'O nome "{nome}" foi adicionado a lista')                
        if opcao==2:
            escolhido = random.choice(nomes)        
            print(f'O nome escolhido foi {escolhido}')            
        if opcao==3:
            print('A lista possui os seguintes nomes:')
            for i in nomes:
                print(i)            
        if opcao==4:
            print('Fim do programa')    
            condicao = False        

        print('\n')        
    else:
        print('Você não escolheu uma opção válida!')
        
    
   




