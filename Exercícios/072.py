# Crie um programa que leia o nome, sexo e idade de vários Alunos, guardando os dados de cada aluno em um dicionário e todos os dicionários em uma lista. No final mostre:
# Quantas pessoas foram cadastradas
# A média de idade do grupo
# Uma lista com todas as mulheres
# Uma lista com todas as pessoas com idade acima da média

alunos = []
soma = 0

while True:
    aluno = {}
    aluno['Nome'] = str(input('Nome: '))
    aluno['Sexo'] = str(input('Sexo (M/F): ')).strip().upper()[0]
    aluno['Idade'] = str(input('Idade: '))
    soma += int(aluno['Idade'])
    alunos.append(aluno)
    
    continuar = input('Você quer continuar?(S/N) \n').strip().upper()[0]
    if continuar == 'N':
        break

mediaidade = soma/len(alunos)
mulheres = [a['Nome'] for a in alunos if a['Sexo'] == 'F']
idadeacima = [a['Nome'] for a in alunos if int(a['Idade']) > mediaidade]

print(f'\nTemos um total de {len(alunos)} pessoas cadastradas.')
print(f'A média de idade do grupo é: {mediaidade}')
print(f'Lista com todas as mulheres: {mulheres}')
print(f'Pessoas com idade acima da média: {idadeacima}')