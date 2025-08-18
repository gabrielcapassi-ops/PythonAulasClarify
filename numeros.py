#tipos de numeros
naonumeros = "2" #string
idade = 38 # int (integer)
altura = 1.74 #float (decimal)

print(naonumeros + naonumeros)
print(idade + 2)
print("Minha idade é " + str(idade))

idade_usuario = input ("Qual é a sua idade?: ")
print("Você tem " + idade_usuario + " anos.")
resultado = int(idade_usuario) + 1
print("Ano que vem você terá " + str(resultado) + " Anos")

valor_a = 10
valor_b = 3

print("soma", valor_a + valor_b)
print("subtração", valor_a - valor_b)
print("multiplicação", valor_a * valor_b)
print("Divisão", valor_a / valor_b) #resultado em float
print("Divisão inteira", valor_a // valor_b) #descarta o decimal com duas \\
print("Resto da divisão", valor_a % valor_b) #modulo
print("Potência", valor_a ** valor_b) # a elevado ao b