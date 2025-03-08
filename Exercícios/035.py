# Escreva um programa que leia o Nome, idade e sexo de 4 pessoas. No final mostre:
# A média de idade do grupo
# Qual é o homem mais velho
# Quantas mulheres têm menos de 20 anos

soma = 0
menosde20 = 0
homemvelho = 0

for i in range(1, 5):
    nome = input('Insira o nome: ').strip()
    idade = int(input('Insira a idade: '))
    sexo = input('Insira o sexo: ').strip().upper()[0]

    soma = soma + idade

    if sexo == 'F' and idade < 20:
        menosde20 = menosde20 + 1

    if sexo == 'M' and idade > homemvelho:
        homemvelho = idade
        nomevelho = nome

media = soma/4
print(f'A média de idade do grupo é {media}')
print(f'{menosde20} mulheres tem menos de 20 anos.')
print(f'O homem mais velho é o {nomevelho}')
