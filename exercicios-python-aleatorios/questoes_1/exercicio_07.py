nome = ['Michael Jackson','Lady Gaga','Roberto Carlos','Axel Rose', 'Chico Tripa']
idade = [35,38,44,52,25]
email = ['michael@gmail.com','lady@gmail.com','roberto@gmail.com','axel@gmail.com','chico@gmail.com']

print('\n')
print('#'*15)
print('Cadastro de Usuário')
print('#'*15)
print('\n')


for indice in range(0,4,1):
   
    print(f'Nome:{nome[indice]}\nIdade:{idade[indice]}\nEmail: {email[indice]}\n')