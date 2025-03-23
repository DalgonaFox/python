# Escreva um programa que crie uma lista com os números de 1 a 10 e, em seguida, exiba apenas os números ímpares da lista.

lista = []

print('Os números ímpares da lista são: ')
for i in range (1, 11):
    lista.append(i)

for i in lista:
    if i % 2 != 0:
        print(i)    