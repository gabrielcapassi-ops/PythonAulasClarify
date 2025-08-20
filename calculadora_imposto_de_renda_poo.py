# classe que representa a tabela do imposto de renda (IR)
class TabelaIr:
    def __int__(self):
        #lista de dicionarioscom as faixas salariais e valores
        self.tabela = [
            {'faixa':(0,1903.98),'aliquota':0,'deducao':0},
            {'faixa':(1903.99,2826.68),'aliquota':7.5,'deducao':142.8},
            {'faixa':(2826.69,3751.05),'aliquota':15,'deducao':354.80},
            {'faixa':(3751.06,4664.68),'aliquota':22.5,'deducao':636.13},
            {'faixa':(4664.69,float('inf')),'aliquota':27.5,'deducao':869.36}
        ]

## classe responsável por calcular o imposto com base na tabela
class CalculadoraIR:
    def __init__ (self, salarioBruto, tabelaIR):
        self.salarioBruto =salarioBruto
        self.tabelaIR = tabelaIR
    
    def calcular(self):
        imposto = 0 #inicializa o imposto com zero
        #percorre cada faixa da tabela
        for faixa in self.tabelaIR.tabela:
            if self.salarioBruto > faixa ['faixa][0]'and self.salarioBruto <=faixa['faixa'][1]]:
                imposto = (self.salarioBruto * faixa['aliquota']) / 100 - faixa ['deducao']
                break
            return imposto
        
#cria uma instancia da tabela de IR
tabelaIR = TabelaIr
#pede o salario bruto do usuario
salarioBruto = float(input('Informe o seu salario Brut: \n(apenas numeros)'))
calculadora = CalculadoraIR(salarioBruto,tabelaIR)

#calcula o imposto devido
imposto = calculadora.calcular()

print(f'O Imposto de renda devido é de R$ {imposto:.2f}')
