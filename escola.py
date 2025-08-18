
nome_aluno = input("Informe o nome do aluno: ")
tipo_escola= input("Estuda em colegio: \n [1]Publico \n [2] Particular")
nota01 = float(input("Digite a nota do bimeste 1:"))
nota02 = float(input("Digite a nota do bimeste 2:"))
nota03 = float(input("Digite a nota do bimeste 3:"))
nota04 = float(input("Digite a nota do bimeste 4:"))
freq_aluno = int(input("Qual a frequencia do aluno? "))
media_aluno= int((nota01+nota02+nota03+nota04) / 4 )

freq_corte = 70
media_corte = 7

'''
!= diferente
== igual
<= menor ou igual
>= maior ou igual
> maior
< menor
'''

if tipo_escola == "2":
    if media_aluno >= media_corte and freq_aluno >= freq_corte:
        resultado = "aprovado"
    else :
        resultado = "reprovado"

if tipo_escola == "1":
    if media_aluno >= media_corte or freq_aluno >= freq_corte:
        resultado = "aprovado"
    else :
        resultado = "reprovado"

if tipo_escola == "1" :
    tipo = "Publica"
else:
    tipo = "Particular"

print(f"Tipo: {tipo} \n - Frequencia de corte: {freq_corte} \n -Media de corte: {media_corte}")

print(f" Aluno {nome_aluno} com média de {media_aluno} e frequencia de {freq_aluno} foi {resultado} pela direção")