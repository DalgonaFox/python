# Escreva um programa que imprima todos os números pares entre dois números fornecidos pelo usuário.

num_inicio = int(input('Insira o número de início: '))
num_final = int(input('Insira o número do final: '))

print(f'Esses são os números pares entre {num_inicio} e {num_final}')

if num_inicio % 2 == 0:
    for i in range(num_inicio, num_final, 2):
        print(i)
else:
    for i in range(num_inicio + 1, num_final, 2):
        print(i)