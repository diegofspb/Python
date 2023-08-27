'''Use um dicionário para armazenar informações sobre uma pessoa que você conheça. Armazene seu
primeiro nome, o sobrenome, a idade e a cidade em que ela vive. Você deverá ter chaves como
primeiro_nome, sobrenome, idade, e cidade. Por fim, mostre cada informação armazenada em seu
dicionário.
'''

cadastro = {
    'nome':'Rafael',
    'sobrenome':'Silva',
    'idade':'42',
    'cidade':'São Paulo'
    }

print(f'{cadastro["nome"]} {cadastro["sobrenome"]} possui {cadastro["idade"]} anos e mora na cidade de {cadastro["cidade"]}')