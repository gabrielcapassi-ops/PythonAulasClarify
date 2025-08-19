def minhaFuncao():
    print('Olá Clarify')

minhaFuncao()
minhaFuncao()

cidades = ['Sao Paulo','Osasco','Poa','São Bernardo do Campo']
cidades2 = ['Suzano' ,'mogi', 'Diadema', 'Mauá']
contador = 0

def minhaFuncaoMelhorada(local , giro):
    print(str(giro) + ' - ' + local)

for cidade in cidades:
    contador = contador + 1
    minhaFuncaoMelhorada(cidade, contador)

# contador = 0      --- nesse caso zera o próximo contador.

for cidade in cidades2:
    contador = contador + 1
    minhaFuncaoMelhorada(cidade, contador)