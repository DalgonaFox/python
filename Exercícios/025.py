# Crie um programa para jogar JOKEMPO, usando a função random.randint

import random

print('Vamos jogar JOKEMPO!')
print('Pedra = 1')
print('Papel = 2')
print('Tesoura = 3')

escolha = int(input('Digite o número correspondente à opção desejada: '))
computador = random.randint(1, 3)

print('Jo - Kem - Po !!!')

if escolha == 1:
    print('Você escolheu PEDRA.')
elif escolha == 2:
    print('Você escolheu PAPEL.')
elif escolha == 3:
    print('Você escolheu TESOURA.')
else:
    print('Você digitou um número inválido.')

if computador == 1:
    print('O computador escolheu PEDRA.')
elif computador == 2:
    print('O computador escolheu PAPEL.')
elif computador == 3:
    print('O computador escolheu TESOURA.')

# Você ganha

if escolha == 1 and computador == 3:
    print('Você ganhou com PEDRA contra a TESOURA! A pedra quebrou a tesoura!')
elif escolha == 3 and computador == 2:
    print('Você ganhou com TESOURA contra o PAPEL! A tesoura cortou o papel!')
elif escolha == 2 and computador == 1:
    print('Você ganhou com PAPEL contra a PEDRA! O papel embalou a pedra!')


# Você perde

if escolha == 3 and computador == 1:
    print('Você perdeu com TESOURA contra a PEDRA! A pedra quebrou a tesoura!')
elif escolha == 2 and computador == 3:
    print('Você perdeu com PAPEL contra a TESOURA! A tesoura cortou o papel!')
elif escolha == 1 and computador == 2:
    print('Você perdeu com PEDRA contra o PAPEL! O papel embalou a pedra!')

# Empate

if escolha == computador:
    print('Empate!')