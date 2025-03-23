# Escreva um programa que crie uma lista com os números de 1 a 10 e, em seguida, exiba apenas os números pares da lista.

lista = []

for i in range (1, 11):
    lista.append(i)

print('Números pares da lista: ')
for i in lista:
    if i % 2 == 0:
        print(f'{i}', end=' ')