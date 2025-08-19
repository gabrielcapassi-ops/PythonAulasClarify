def divisão (a, b):
    try:
        resultado = a / b
        print(f'Resultado da divisão {a} por {b} é: {resultado}')
    except ZeroDivisionError:
        #se houver erro de divisão por zero o código entra dentro do except e é executado
        print('Erro: Não é possível dividir zero')
    except TypeError:
        #Caso algum valor nao seja um numero, esse except será executado
        print('Erro: Ambos os valores precisam ser numero')
    except Exception as erro:
        #Captura qualquer outro erro não trato nos anteriores.
        print('Erro inesperado:{erro}')
    else:
        # O bloco else é executado se o código dentro do try for bem sucedido (sem erro)
        print('Operação realizada com sucesso')
    finally:
        # O bloco finally é sempre executado, independente de erro ou sucesso.
        print( 'Processo de divisão finalizado')



# Teste 01: Divisão normal!
divisão (10,2)
# Teste 02: Divisão por Zero
divisão (10,0)
# Teste 03: Divisão com tipos invalidos
divisão (10, 'dois')
# Teste 04: Divisão com erro inesperado
divisão ('dez',2)
