# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

saque = 0

print('--- Bem vindo ao Caixa Eletrônico. ---')
while True:
    saque = int(input('Quanto dinheiro você quer sacar? O valor não pode conter centavos.\nR$'))
    print(f'Você vai sacar R${saque}.')
    
    if saque >= 50:
        nota50 = saque // 50
        resto = saque % 50
        if nota50 != 0:
            print(f'Você vai ganhar {round(nota50)} cédulas de R$50', end='')

        if resto != 0:
            nota20 = resto // 20
            resto = resto % 20
            if nota20 != 0:
                print(f', {round(nota20)} cédulas de R$20', end='')

            if resto != 0:
                nota10 = resto // 10
                resto = resto % 10
                if nota10 != 0:
                    print(f', {round(nota10)} cédulas de R$10', end='')

                if resto != 0:
                    nota1 = resto // 1
                    if nota1 != 0:
                        print(f' e {round(nota1)} cédulas de R$1', end='.')
    elif saque >= 20:
        nota20 = saque // 20
        resto = saque % 20
        print(f'Você vai ganhar {round(nota20)} cédulas de R$20', end='')

        if resto != 0:
            nota10 = resto // 10
            resto = resto % 10
            if nota10 != 0:
                print(f', {round(nota10)} cédulas de R$10', end='')

            if resto != 0:
                nota1 = resto // 1
                print(f'e {round(nota1)} cédulas de R$1', end='.')
    elif saque >= 10:
        nota10 = saque // 10
        resto = saque % 10
        print(f'Você vai ganhar {round(nota10)} cédulas de R$10', end='')

        if resto != 0:
            nota1 = resto // 1
            print(f'e {round(nota1)} cédulas de R$1', end='.')
    else:
        nota1 = saque // 1
        print(f'Você vai ganhar {round(nota1)} cédulas de R$1', end='.')


    escolha = input('\n\nVocê quer sacar mais dinheiro? S/N\n').strip().upper()[0]
    if escolha != 'S' and escolha != 'N':
        print('Insira um valor válido.')

    if escolha == 'N':
        print('Obrigado por utilizar o Caixa Eletrônico.')
        break
