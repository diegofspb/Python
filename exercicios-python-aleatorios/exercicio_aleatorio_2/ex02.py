'''2. Use um dicionário para armazenar os números favoritos de algumas pessoas. Escolha cinco colegas, e
pergunte quais seus número favoritos. Use seus nomes para serem as chaves de cada número favorito.
Ao final, exiba o nome de cada pessoas e seu número favorito.'''


colegas = {
    'rafael':43,
    'bruno':23,
    'maria':55,
    'joao':46,
    'fulano':41
    }

for chave, valor in colegas.items():
    print(f'{chave.upper()} possui o número favorito {valor}')