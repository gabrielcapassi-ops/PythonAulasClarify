import pandas as pd

#criar um dataframe com o pandas e inserir dados
data = {
    'Nome' : ['Caio','Myke','Gustavo','Joao','Gabriel','Luiz'],
    'Idade':[38,35,22,39,37,44],
    'Salario': [3624,9876,6473,5684,9735,1562]
}
df = pd.DataFrame(data)

#Exibindo o 
print('\ndataframe')
print(df)


#selecionando uma coluna
print('\nColuna de nome')
print(df['Nome'])

#Filtrando linhas (ex:idade menor que 30)
print('\nPessoas com idade menor que 30')
print(df[df['Idade'] < 30])

#inserindo nova coluna
df['Imposto'] = df['Salario'] * 0.18
print('\nDataframe com nova coluna de imposto calculado')
print(df)

#Calculando a media de Salario
media_salarial = df['Salario'].mean()
print('\n Media do salario')
print(media_salarial)

#salvar o dataframe em um arquivo csv
df.to_csv('equipe.csv', index=False)