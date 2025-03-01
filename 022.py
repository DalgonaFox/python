# Escreva um programa que peça ao usuário 5 notas, de 0 a 10 e imprima se a média, é insuficiente (menor que 6),
# suficiente (entre 6 e 7), bom (entre 7 e 9) ou excelente (9 ou maior).

nota1 = float(input('Digite a nota: '))
nota2 = float(input('Digite a nota: '))
nota3 = float(input('Digite a nota: '))
nota4 = float(input('Digite a nota: '))
nota5 = float(input('Digite a nota: '))

media = (nota1 + nota2 + nota3 + nota4 + nota5)/5

if media >= 9:
    print('Nota excelente.')
elif media >= 7:
    print('Nota boa.')
elif media >= 6:
    print('Nota suficiente.')
else:
    print('Nota insuficiente.')