
print('*'*50)
print('Remover nomes duplicados')
print('*'*50)

nomes = 'diego,gustavo,sillas,diego'

lista = list(nomes.split(","))
nova_lista = []

for nome in lista:
    if nome not in nova_lista:
        nova_lista.append(nome)
    else:
        print(f'{nome} é um nome duplicado')

print(nova_lista)




