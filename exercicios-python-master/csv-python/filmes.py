import csv
from pathlib import Path

filme_maior_publico = '' #nome do filme com maior publico = string
maior_publico = 0 #valor inteiro

caminho_csv = Path(__file__).parent/'filmes.csv'   #Path sever para identificar o caminho onde está o arquivo

with open(caminho_csv,'r', encoding = 'utf-8') as arquivo:  #parametro do with open é caminho, tipo da execução r=reader, encoding
   
    leitor = csv.reader(arquivo)
    next(leitor)     

    for linha in leitor:
        nome = linha[2]
        publico = float(linha[9])

        if (publico>maior_publico):
            maior_publico = publico
            filme_maior_publico = nome

print(f'O filme com maior público é: {filme_maior_publico} com público de {maior_publico} pessoas.')