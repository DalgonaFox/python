# Escreva um programa que crie um dicionário com as informações de 5 países, como nome, capital, população e idioma oficial. Em seguida, permita que o usuário digite o nome de um país e exiba suas informações.

paises = []

for i in range(1, 6):
    pais = {}
    pais['Nome'] = str(input('Insira o nome: '))
    pais['Capital'] = str(input('Insira a capital: '))
    pais['Idioma'] = str(input('Insira o idioma: '))
    pais['Populacao'] = str(input('Insira a população: '))
    paises.append(pais)

nomepais = str(input('Insira o nome do país que quer saber sobre: '))
nomes = [p['Nome'] for p in paises]

index = nomes.index(nomepais)
print(paises[index])