# Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar

numero = float(input('Insira um número: '))

if numero % 2 == 0:
    print(f'O número {numero} é par!')
else:
    print(f'O número {numero} é ímpar!')