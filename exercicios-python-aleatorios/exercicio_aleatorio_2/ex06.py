'''6. Dado uma lista de dicionários, onde cada dicionário representa um produto com as chaves "nome",
"preço" e "quantidade", crie um algoritmo que retorne o valor total do estoque.
Exemplo de entrada: [{'nome': 'maçã', 'preço': 2.0, 'quantidade': 5}, {'nome': 'banana', 'preço': 1.5,
'quantidade': 10}]
Saída esperada: 25.0
'''

produto1 = {'nome':'uva','valor':12.5,'quantidade':50}
produto2 = {'nome':'refrigerante','valor':7.80,'quantidade':27}
produto3 = {'nome':'gelo','valor':4.57,'quantidade':41}

estoque = produto1['quantidade']+produto2['quantidade']+produto3['quantidade']

print(estoque)