'''12. Dado uma lista de dicionários, onde cada dicionário representa um filme com as chaves "título",
"ano" e "gênero", crie um algoritmo que retorne a lista de filmes ordenada primeiro por gênero e
depois por ano.

Exemplo de entrada: [{'título': 'O Poderoso Chefão', 'ano': 1972, 'gênero': 'drama'}, {'título': 'Pulp
Fiction', 'ano': 1994, 'gênero': 'drama'}, {'título': 'Indiana Jones e os Caçadores da Arca Perdida', 'ano':
1981, 'gênero': 'aventura'}, {'título': 'De Volta Para o Futuro', 'ano': 1985, 'gênero': 'aventura'}]

Saída esperada: [{'título': 'Indiana Jones e os Caçadores da Arca Perdida', 'ano': 1981, 'gênero':
'aventura'}, {'título': 'De Volta Para o Futuro', 'ano': 1985, 'gênero': 'aventura'}, {'título': 'O Poderoso
Chefão', 'ano': 1972, 'gênero': 'drama'}, {'título': 'Pulp Fiction', 'ano': 1994, 'gênero': 'drama'}]'''

filmes = [
    {
    'título': 'O Poderoso Chefão',
    'ano': 1972,
    'gênero': 'drama'}, 

    {'título': 'PulpFiction',
    'ano': 1994,
    'gênero': 'drama'},

    {'título': 'Indiana Jones e os Caçadores da Arca Perdida',
    'ano':1981,
    'gênero': 'aventura'},

    {'título': 'De Volta Para o Futuro',
    'ano': 1985,
    'gênero': 'aventura'}
]

filmes_ordenados = sorted(filmes, key=lambda filme: (filme['gênero'], filme['ano']))

print(filmes_ordenados)

'''A função sorted() em Python pode receber três argumentos opcionais:

iterable (obrigatório): O objeto iterável a ser ordenado, como uma lista, tupla, conjunto, etc.

key (opcional): Uma função que é usada para extrair uma chave de classificação para cada elemento do iterável. Essa chave é usada para ordenar os elementos. Se esse argumento não for fornecido, os elementos serão ordenados com base em sua posição natural na lista.

reverse (opcional): Um valor booleano que indica se os elementos devem ser ordenados em ordem decrescente. O padrão é False, ou seja, os elementos são ordenados em ordem crescente.'''