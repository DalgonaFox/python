# Escreva um programa que crie um dicionário com os nomes e preços de 5 produtos. Em seguida, exiba o produto mais barato e o mais caro.

produtos = []

for i in range (1, 6):
    produto = {}
    produto['Nome'] = str(input('Nome: '))
    produto['Preço'] = str(input('Preço: '))
    produtos.append(produto)

barato = min(p['Preço'] for p in produtos)
caro = max(p['Preço'] for p in produtos)

print(f'O produto mais barato é: {[p['Nome'] for p in produtos if p['Preço'] == barato]}')
print(f'O produto mais caro é: {[p['Nome'] for p in produtos if p['Preço'] == caro]}')