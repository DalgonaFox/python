# Crie um programa que leia uma frase e mostre:
# Quantas vezes aparece a letra “a”
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece na última vez

frase = input('Insira uma frase: ')

frase = frase.replace('A', 'a')
frase = frase.replace('á', 'a')
frase = frase.replace('ã', 'a')
frase = frase.replace('à', 'a')

totalas = frase.count('a')

print(totalas)

total = len(frase)

print(f'Primeiro a: {frase.find('a') + 1}')
print(f'Último a: {frase.rfind('a') + 1}')
