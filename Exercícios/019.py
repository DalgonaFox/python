# Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10, entre 10 e 20 ou maior que 20.

numero = float(input('Insira um número: '))

if numero <= 10:
    print(f'O número {numero} está entre 0 e 10!')
elif numero <= 20:
    print(f'O número {numero} está entre 10 e 20!')
else:
    print(f'O número {numero} é maior do que 20.')