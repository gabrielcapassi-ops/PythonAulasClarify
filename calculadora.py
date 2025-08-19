executar = True

def decisão():
    global executar
    repetir = input('Deseja realizar outra conta? ').lower
    if repetir == '1' or repetir == 'nao' :
        executar = False

while executar:
    escolhas = '''
    [1] ou [+] para Somar
    [2] ou [-] para Subtrair
    [3] ou [/] para Dividir
    [4] ou [*] para Multiplicar
    [5] para sair
    (ou digite sua opcao somar / substrair / multiplicar / dividir / sair )
    '''
    print(escolhas)
    operador = input("Qual sua opção?").lower()
    if  operador== '5' or operador == 'sair':
        print("... Saindo da calculadora. Obrigado por usar!")
        print('---------fim do Sistema --------')
        break
    valor01 = int(input("Escolha seu primeiro valor"))
    valor02 = int(input("Escolha seu segundo valor"))

    textinho = '''
    [1] Não, desejo sair!
    [2] Sim, desejo realizar outro calculo.
    (ou digite sim / nao)
    '''

    # ------------ operação soma -------
    if operador == '1' or operador == '+' or operador == 'somar':
        resultado = valor01 + valor02
        print (f'Resultado é: {resultado}')
        print(textinho)
        decisão()

         # ------------ operação subtração -------
    if operador == '2' or operador == '-' or operador == 'subtração':
        resultado = valor01 - valor02
        print (f'Resultado é: {resultado}')
        print(textinho)
        decisão()

         # ------------ operação divisão -------
    if operador == '3' or operador == '/' or operador == 'dividir':
        if valor02 == 0:
            print('Erro: divisão por 0 não é permitida!')
        else:
            resultado = valor01 / valor02
            print (f'Resultado é: {resultado}')
        print(textinho)
        decisão()

         # ------------ operação Multiplicação -------
    if operador == '4' or operador == '*' or operador == 'multiplica':
        resultado = valor01 * valor02
        print (f'Resultado é: {resultado}')
        print(textinho)
        decisão()