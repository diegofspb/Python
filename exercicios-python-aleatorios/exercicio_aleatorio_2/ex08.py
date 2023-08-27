'''8. Dado um dicionário com as chaves representando nomes de países e os valores sendo listas de nomes
de cidades, crie um algoritmo que retorne a cidade mais populosa de cada país em um novo
dicionário.
Exemplo de entrada: {'Brasil': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte'], 'EUA': ['Nova Iorque',
'Los Angeles', 'Chicago']}
Saída esperada: {'Brasil': 'São Paulo', 'EUA': 'Nova Iorque'}
'''

paises_cidades = {
    'Brasil': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte'],
    'EUA': ['Nova Iorque','Los Angeles', 'Chicago']
    }

cidades_populosas = {}

for pais,cidade in paises_cidades.items():
    cidades_populosas[pais] = cidade[0]

print(cidades_populosas)