# Faça um programa que leia o nome e o QI de várias pessoas, guardando tudo e uma lista. No final mostre:
# Quantas pessoas foram cadastradas
# Uma listagem com as pessoas com o maior QI
# Uma listagem com as pessoas de menor QI

pessoas = list() 
dados = list()

for i in range(1, 11):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()

print(f'Pessoas cadastradas: {len(pessoas)}')

pessoas_maior = sorted(pessoas, reverse=True)[:3]
pessoas_menor = sorted(pessoas)[:3]

print(f'As 3 pessoas com maior QI: {[p[0] for p in pessoas_maior]}')
print(f'As 3 pessoas com menor QI: {[p[0] for p in pessoas_menor]}')