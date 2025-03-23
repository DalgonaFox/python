# Escreva um programa que crie uma lista vazia e permita que o usuário insira números nessa lista até que ele digite um número negativo. Em seguida, exiba a lista na tela.

lista = []

while True:
    num = int(input('Insira um número: '))
    if num < 0:
        break
    else:
        lista.append(num)

print(lista)
