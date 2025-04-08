# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário, se por acaso a Carteira de trabalho for diferente de zero. O Dicionário receberá também o ano de contratação e o saláro. Calcule e apresente, além da idade, com quantos anos a pessoa vai se aposentar.

funcionarios = []

while True:
    funcionario = {}
    funcionario['Nome'] = str(input('Nome: '))
    funcionario['Ano de Nascimento'] = int(input('Ano de nascimento: '))
    funcionario['Sexo'] = str(input('Sexo (M/F): ')).strip().upper()[0]
    funcionario['Carteira de Trabalho'] = str(input('Possui Carteira de Trabalho? (S/N)')).strip().upper()[0]
    
    if funcionario['Carteira de Trabalho'] == 'S':
        funcionario['Ano de contratação'] = int(input('Ano de contratação: '))
        funcionario['Salário'] = int(input('Salário: '))
        funcionario['Idade'] = 2025 - int(funcionario['Ano de Nascimento'])
        if funcionario['Sexo'] == 'F':
            funcionario['Aposentadoria'] = int(funcionario['Idade']) + 30
            if int(funcionario['Aposentadoria']) < 58:
                funcionario['Aposentadoria'] = (58 - int(funcionario['Aposentadoria'])) + int(funcionario['Aposentadoria'])
        else:
            funcionario['Aposentadoria'] = int(funcionario['Idade']) + 35
            if int(funcionario['Aposentadoria']) < 60:
                funcionario['Aposentadoria'] = (60 - int(funcionario['Aposentadoria'])) + int(funcionario['Aposentadoria'])
        
        funcionarios.append(funcionario)
        print('Funcionário cadastrado.')
    else:
        print('Pessoa inelegível para dicionário.')

    escolha = str(input('Você quer continuar cadastrando pessoas? (S/N)\n')).strip().upper()[0]
    if escolha == 'N':
        break

for i in range (0, len(funcionarios)):
    print(f'O funcionário {[f['Nome'] for f in funcionarios]}', end=' ')
    print(f'tem {[f['Idade'] for f in funcionarios]} anos', end=' ')
    print(f'e vai se aposentar com {[f['Aposentadoria'] for f in funcionarios]} anos caso continue na mesma empresa.')