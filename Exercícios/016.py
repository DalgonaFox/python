# Escreva um programa que peça ao usuário dois números e imprima se eles são iguais ou diferentes.

numero1 = float(input('Insira o primeiro número: '))
numero2 = float(input('Insira o segundo número: '))

if numero1 == numero2:
    print(f'O número {numero1} e o número {numero2} são iguais!')
else:
    print(f'O número {numero1} e o número {numero2} são diferentes.')