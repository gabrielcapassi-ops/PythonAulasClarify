#exercicio

nome = input("Nome do Aluno ")
nota01 = float(input("Digite a nota do bimeste 1:"))
nota02 = float(input("Digite a nota do bimeste 2:"))
nota03 = float(input("Digite a nota do bimeste 3:"))
nota04 = float(input("Digite a nota do bimeste 4:"))

#efetua o calculo
media = (nota01 + nota02 + nota03 + nota04) / 4

#exibe o resultado
print(f"A media do Aluno {nome} é de {media}")