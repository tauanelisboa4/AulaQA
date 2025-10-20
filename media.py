# especificaçao do aluno
nome = input("Ola! qual é o seu nome?")

# notas do aluno
nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))
nota3 = float(input("digite a terceira nota:"))
nota4 = float(input("digite a quarta nota:"))

# calculo media do aluno
media = (nota1 + nota2 + nota3 + nota4) /4

# retorno
print(f"Ola, {nome}! sua media é: {media:.1f}pontos.")