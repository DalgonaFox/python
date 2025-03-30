# Escreva um programa que leia diversos alunos, crie um dicionário com as notas deles em três disciplinas: matemática, português e história. Em seguida, exiba a média das notas do aluno.

alunos = []

for i in range (1, 3):
    aluno = {}
    aluno['Nome'] = str(input('Nome: '))
    aluno['Matemática'] = int(input('Nota em Matemática: '))
    aluno['Português'] = int(input('Nota em Português: '))
    aluno['História'] = int(input('Nota em História: '))
    aluno['Média'] = (aluno['História'] + aluno['Matemática'] + aluno['Português'])/3
    alunos.append(aluno)

nomealuno = [a['Nome'] for a in alunos]
media = [a['Média'] for a in alunos]

for i in range (0, 2):
    print(f'Média do aluno {nomealuno[i]}: {media[i]}')
