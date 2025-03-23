# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:
# 1 - Qual é o total gasto na compra
# 2 - Quantos produtos custam mais de R$1000,00
# 3 - Qual é o produto mais barato

barato = 99999999999999999999999
maisquemil = 0
total = 0
preco = 0

print('--- Carrinho de Compras ---')

while True:
    produto = input('Qual o nome do Produto? ')
    preco = int(input('Qual o preço dele? R$'))

    if preco < barato:
        barato = preco
        baratonome = produto
    if preco > 1000:
        maisquemil += 1
    total += preco

    escolha = input('Você quer continuar? S/N\n').strip().upper()[0]
    if escolha == 'N':
        break

print(f'O total gasto na compra foi R${total}.')
print(f'O produto mais barato da sua compra foi {baratonome}.')

if maisquemil == 1:
    print(f'{maisquemil} produto custa mais de R$ 1000,00.')
elif maisquemil > 1:
    print(f'{maisquemil} produtos custam mais de R$ 1000,00.')
else:
    print(f'Nenhum produto custa mais de R$ 1000,00.')
