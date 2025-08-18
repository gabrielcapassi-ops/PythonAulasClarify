# Aula 01 : Tipos de dados e Variaveis

#-------Strings ( texto) -------
nome = 'Gabriel'
curso = "Python"
mensagem = "Bem vindo " + nome + " ao curso " + curso
print (mensagem)

# Agora vamos deixar o usuario digitar o seu nome
nome_usuario = input ("Digite o seu nome: ")
curso_usuario = input ('Qual o eu curso?: ')

# usando o f-string (forma mais moderna de formatar uma string)
mensagem2 = f"Olá {nome_usuario}, seja bem vindo ao curso de {curso_usuario}"
print (mensagem2)

#Algumas funcoes uteis de string
print(nome_usuario.upper()) #Maiusculo - sempre colocar parenteses branco
print(nome_usuario.lower()) #Minusculo - sempre colocar parenteses branco
print(nome_usuario.title()) #Primeiraletra de cada palavra maiscula - sempre colocar parenteses branco

# Tambem podemos repetir strings com o operador *
linha = '-' * 20
print(linha)
print("Exercicio concluido com sucesso")
print(linha)
