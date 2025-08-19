import requests, json

nome = input('Digite o nome que você quer pesquisar')
resposta = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}')

dados = json.loads(resposta.text)

print(dados[0]['res'][0])