
# Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue pedindo até que o usuário acerte o número. E no final, retorne também a quantidade de tentativas necessárias.

import random

num = random.randint(1, 10)
tentativas = 1
adivinha = int(input('Tente adivinhar um número de 1 a 10!\n'))

while adivinha != num:
    adivinha = int(input('Errou! tente novamente!\n'))
    tentativas += 1

print(f'Você acertou! Você tentou {tentativas} vezes.')