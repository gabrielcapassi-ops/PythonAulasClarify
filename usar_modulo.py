import operacoes #usa o arquivo salvo na mesma pasta operacoes.py
import meu_modulo #usa o arquivo salvo na mesma pasta "meu_modulo"

print(operacoes.somar(2,4))
print(meu_modulo.saudacao('Caio'))

try:
    print(operacoes.dividir(10,0))
except ValueError as erro:
    print(f'Erro ao dividir por zero: {erro}')

