# Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder. Ao final deve mostrar a quantidade de vitórias.

import random

vitorias = 0
perda = 0

while True:
    escolha = int(input('1 - Par\n2 - Ímpar\n\nEscolha entre par ou ímpar: '))
    if escolha != 1 and escolha != 2:
        print('Escolha uma opção válida.')
        escolha = int(input('\nEscolha entre par ou ímpar: '))

    numjogador = int(input('Escolha um número entre 1 e 10: '))
    if numjogador > 10 or numjogador < 0:
        print('Escolha um número de 1 a 10.')
        numjogador = int(input('Escolha um número entre 1 e 10: '))

    numpc = random.randint(1, 10)
    print(f'O computador escolheu o número {numpc}.')

    parimpar = (numjogador + numpc) % 2

    if escolha == 1:
        if parimpar == 0:
            print(f'O número total é {numjogador + numpc}! Você ganhou pois o número é Par!\n')
            vitorias += 1
        else:
            print(f'O número total é {numjogador + numpc}! Você perdeu, pois o número é Ímpar!')
            perda += 1

    if escolha == 2:
        if parimpar == 0:
            print(f'O número total é {numjogador + numpc}! Você perdeu, pois o número é Par!')
            perda += 1
        else:
            print(f'O número total é {numjogador + numpc}! Você ganhou pois o número é Ímpar!\n')
            vitorias += 1

    if perda > 0:
        print('\nTchau, até a próxima!')
        break