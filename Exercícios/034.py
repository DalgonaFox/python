# Escreva um programa que leia 10 números, se for ímpar deve ser descartado, se não, deve ser agregado a uma soma

soma = 0
for i in range (1, 11):
    numero = int(input(f'Insira o {i}° número: '))
    if numero % 2 == 0:
        soma = soma + numero

print(soma)