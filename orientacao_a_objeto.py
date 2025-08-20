class Carro:
    def __init__(self, cor, modelo,):
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0
        self.som = "bibiii" #nesse caso precisa estar como "" pois é texto.

    def acelerar (self, incremento):
        self.velocidade += incremento
        print(f' O carro {self.modelo} acelerou para {self.velocidade}')
    
    def parar (self):
        self.velocidade = 0
        print(f'O carro {self.modelo} parou. ')
    
    def buzinar (self):
        print(f' O carro {self.modelo} buzinou {self.som}')

    def desacelerar(self, decremento):
        if self.velocidade - decremento <- 0:
            self.velocidade = 0
        else:
            self.velocidade -= "drecremento"
            print(f"O carro {self.modelo} reduziu para {self.velocidade} km/h")

    

# criando um objeto carro
meu_carro = Carro("Amarelo", "Fusca") #aqui precisa colocar na mesma sequencia  da linha 2
carro_visita = Carro("Branco", "Celta")

meu_carro.acelerar(20)
meu_carro.acelerar(30)
meu_carro.parar()
meu_carro.buzinar()

carros = [
    Carro('Vermelho','Fox'),
    Carro('Cinza','Celta'),
    Carro('Branco','Versa'),
    Carro('Preto','Gol'),
    Carro('Verde','Onix')
]

for carro in carros:
    carro.acelerar(50)
    carro.buzinar()
   