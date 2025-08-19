from random import randint

# Jogo de adivinhação com diversos gatilhos.
print('####### Inicio de Jogo #######')
print('---- Adivinhe o tesouro ----')
print(' --- Feito por Gabriel ----')
print('')

menor = 0
maior = 100 
random = randint(0,100)
chute = 0
chances = 10

while chute != random:
    chute = input(f'Chute um numero entre {menor} e {maior} ')
    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1
        if chute == random:
            print ('')
            print ('Parabens, você venceu. O número era {} e você ainda tinha {} chances.'.format(random, chances))
            print('')
            break
        else:
            print('')
            if chute > random:
                print (f'Você errou!!! \nDica: É um número menor que {chute}')
            else:
                print (f'Você errou!!! \nDica: É um número maior que {chute}')
            print("Você ainda tem {} chances.".format(chances))
            print("")
        if chances == 0:
            print("")
            print("Suas chances acabaram,você perdeu.")
            print(f'O valor esperado era {random}')
            print("")
            break


print('####### Fim de Jogo #######')
print('--- Obrigado por jogar ---')
