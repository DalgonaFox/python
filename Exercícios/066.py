# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta

import random

quantidade = int(input('Quantos jogos serão gerados?\n'))
jogos = []
jogo = []

for i in range (0, quantidade):
    for i in range (1, 7):
        numeros = random.randint(1, 60)
        jogo.append(numeros)
    jogos.append(jogo[:])
    jogo.clear()

for i in range (0, quantidade):
    print(f'Jogo {i+1}: {jogos[i]}')
