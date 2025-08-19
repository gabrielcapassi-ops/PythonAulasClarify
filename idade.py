executar = True

while executar:
        try:
            anoNasc = int(input('Em que ano você nasceu?'))
            anoAtual = int(input('Em que ano estamos?'))
            idade = anoAtual - anoNasc
            print(f'Você tem: {idade} anos')
        except ValueError:
            print('Por favor, digite um numero valido para os anos')


        opcao = input('\nDeseja testar novamente? \nSim ou Não?').strip().lower()
        lista = ['não','n','nao']
        # ou pode usar if opcao in ['não','n','nao']:
        if opcao in lista:
            executar = False