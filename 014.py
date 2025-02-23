# Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.

numero = float(input('Insira um número: '))

if numero >= 0:
    print(f'O número {numero} é positivo!')
else:
    print(f'O número {numero} é negativo...')