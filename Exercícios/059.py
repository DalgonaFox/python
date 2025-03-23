# Faça um programa com uma função maior e menor, que leia uma lista com 5 valores informados pelo usuário e retorne esses valores e a posição deles

def maior(lista):
    for i in range (0, len(lista)):
        print(f'Posição: {i}, Valor: {lista[i]}')

def menor(lista):
    for i in range ((len(lista) - 1), -1, -1):
        print(f'Posição: {i}, Valor: {lista[i]}')
    
valores = []
for i in range (1, 6):
    num = int(input('Insira um número na lista: '))
    valores.append(num)

print('\nPosição e Valor dos elementos em ordem decrescente:')
menor(sorted(valores))
print('\nPosição e Valor dos elementos em ordem crescente:')
maior(sorted(valores))