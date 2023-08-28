nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

peso1 = 2
peso2 = 3
peso3 = 5

media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / 3

print("A média do aluno é= ", round(media,2))
