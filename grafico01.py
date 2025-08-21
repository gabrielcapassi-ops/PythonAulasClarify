import plotly.graph_objects as go

#dados do grafico

valores_x = [1,2,3,4,5]
valores_y = (11,12,13,14,15)

#criar o grafico de linha
fig = go.Figure(data=go.Scatter(x = valores_x, y = valores_y, mode = 'lines+markers', name = 'Linha'))


#Adicionando titulo e rotulo dos Eixos
fig.update_layout(
    title = 'Gráfico de Linhas Interativas',
    xaxis_title = "Eixo do X",
    yaxis_title = "Eixo do Y"
)

#exibir o grafico criado
fig.show()