# Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário digitar 0000. No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)

soma = 0
totalnum = 0

while True:
    num = int(input("Insira um número: "))
    if num == 0000:
        break
    else:
        totalnum += 1
        soma += num

print(f'Total de números digitados: {totalnum}')
print(f'Soma de todos os números digitados: {soma}')