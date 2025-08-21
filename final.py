import pandas as pd
import numpy as np

#Criar dados com o numpy
nomes = ['Caio','Myke','Gustavo','Joao','Gabriel','Luiz']

idades = np.random.randint(20,50, size=len(nomes)) #len é do python e ele server para trazer examente a quantidade da coluna selecionada no caso aqui "nomes"
salarios = np.random.randint(3000,10000, size=len(nomes))

#criar o dataframe com o pandas
df=pd.DataFrame({
    'Nome': nomes,
    'Idade': idades,
    'Salario': salarios
})

print ('\n 📊 Dataframe gerado')
print(df)

#adicionar nova coluna de imposto calculado
df['Imposto'] = df['Salario'] * 0.18
print('\n Dataframe com coluna de imposto:')
print(df)

#usando as funcoes do numpay no dataframe
print('\n idade Media do grupo:')
print(np.mean(df['Idade']))

#Media salarial do grupo
print('\nMedia Salarial do grupo:')
print(np.mean(df['Salario']))

#Filtrar com pandas pessoas com salario acima da media
media_salarial = np.mean(df['Salario'])
print('\nPessoas com o salario acima da media :')
print(df[df['Salario'] > media_salarial])

#Estattisticas resumidas
print('\n Resumo estatistico (pandas)')
print(df.describe())

#print('\n :')
#print(df)