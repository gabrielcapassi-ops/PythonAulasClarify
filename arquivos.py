import pandas as pd

#Carregar um arquivo do Excel (verificar extensão)
def carregarArquivoCsv(caminhoArquivo):
    try:
        #carrega os dados do arquivo xlsx em um data frame
        df = pd.read_csv(caminhoArquivo)
        print ('Arquivo carregado com sucesso!')
        #print(df.head())
        return df
    except Exception as errinho:
        print(f'erro: {errinho}')

def salvarArquivosCsv(df, caminhoSaida):
    df.to_csv(caminhoSaida, index=False)
    print(f'Arquivo salvo com sucesso em: {caminhoSaida}')

def salvarArquivoXlsx(df, caminhoSaida):
    df.to_excel(caminhoSaida, index=False)
    print(f'Arquivo salvo com sucesso em: {caminhoSaida}')

        
#definir onde está o arquivo a ser carregado
localarquivo = "C:/Users/integral/Desktop/Python_gabriel/base.csv"

df= carregarArquivoCsv(localarquivo)

df['Nova Coluna'] = df['Vendas'] * 2
#print(df.head())

#df['Media'] = (df['TV'] + df['Radio'] + df['Jornal']) / 3
df['Media'] = df[["TV", "Radio", "Jornal"]].mean(axis=1)

#print(df.head())
caminhoSaida = "C:/Users/integral/Desktop/Python_gabriel/novo_arquivo.csv"
# salvarArquivosCsv(df, caminhoSaida)

tipo = input('Deseja exportar para: \n1 - Excel\n2 - CSV')
nome = input('Qual é o nome do arquivo?')
caminhoPrincipal = 'C:/Users/integral/Desktop/Python_gabriel/'

if tipo == "1":
    salvarArquivoXlsx(df,f'{caminhoPrincipal}{nome}.xlsx')
elif tipo == "2":
    salvarArquivosCsv(df,f'{caminhoPrincipal}{nome}.csv')
else:
    print('Opção inválida. Selecione uma opção correta')

                