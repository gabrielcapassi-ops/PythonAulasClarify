import json, requests

nome = input('Qual o seu nome?')

localidade = 0

while localidade < 1 or localidade > 2:
    localidade = int(input('Você deseja selecionar uma localidade?   \n1) sim\n2) não'))

    if localidade == 1:
        uf = input("Qual estado você deseja buscar?  \n35) SP\n 33) RJ \n 31) MG \n43) RS \n 53) DF")
        resultado = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}?localidade{uf}')
    if localidade == 2:
         resultado = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}')
    
    print('''
          Escolha o período
          1) 1930
          2) 1940 - 1950
          3) 1950 - 1960
          4) 1960 - 1970
          5) 1970 - 1980
          6) 1980 - 1990
          7) 1990 - 2000
          8) 2000 - 2010
          ''')
    tempo = int(input('selecione o período: ')) - 1
    dados = json.loads(resultado.text)
    print(dados[0]['res'][tempo])