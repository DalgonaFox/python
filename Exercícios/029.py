# Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.

numero = int(input('Digite um número: '))

print(f'Tabuada do {numero}:')

for i in range (1, 11):
    tabuada = i * numero
    print(f'{numero} x {i} = {tabuada}')