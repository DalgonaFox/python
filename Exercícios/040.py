# Escreva um programa que leia um número n inteiro qualquer e mostra na tela os n primeiros elementos de uma Sequência de Fibonacci

n = int(input('Insira um número: '))
contador = 2
anterior = 1
atual = 1

print(f'Os {n} primeiros números da sequência de Fibonacci são:')

print(anterior, end='')
print(f', {atual}', end='')
while contador != n:
    proximo = atual + anterior
    print(f', {proximo}', end='')
    anterior = atual
    atual = proximo
    contador += 1
print('.')
