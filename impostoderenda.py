def calculadoraIr(salarioBruto):
    tabelaIr = [
        {'faixa':(0,1903.98),'aliquota':0,'deducao':0},
        {'faixa':(1903.99,2826.68),'aliquota':7.5,'deducao':142.8},
        {'faixa':(2826.69,3751.05),'aliquota':15,'deducao':354.80},
        {'faixa':(3751.06,4664.68),'aliquota':22.5,'deducao':636.13},
        {'faixa':(4664.69,float('inf')),'aliquota':27.5,'deducao':869.36}]
    imposto = 0
    for faixa in tabelaIr:
        if salarioBruto > faixa['faixa'][0] and salarioBruto <= faixa['faixa'][1]: #[0] significa a coluna primeira da faixa e [1] significa a segunda linha da coluna faixa
            imposto = (salarioBruto * faixa['aliquota']) / 100 - faixa['deducao']
            break
    return imposto
    
salarioBruto= float(input('Informe seu salario bruto'))
imposto = calculadoraIr(salarioBruto)
print(f'O imposto de renda devido é de R$ {imposto:.2f}')

