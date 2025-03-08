# Escreva um programa que verifique se uma palavra é um palíndromo.

palavra = input('Escreva uma palavra: ').strip().lower().replace(' ', '')

if palavra in 'áàãâ':
    palavra.replace('á', 'a')
    palavra.replace('à', 'a')
    palavra.replace('ã', 'a')
    palavra.replace('â', 'a')
elif palavra in 'éèê':
    palavra.replace('é', 'e')
    palavra.replace('è', 'e')
    palavra.replace('ê', 'e')
elif palavra in 'íìî':
    palavra.replace('í', 'i')
    palavra.replace('ì', 'i')
    palavra.replace('î', 'i')
elif palavra in 'óòôõ':
    palavra.replace('ó', 'o')
    palavra.replace('ò', 'o')
    palavra.replace('ô', 'o')
    palavra.replace('õ', 'o')
elif palavra in 'úùû':
    palavra.replace('ú', 'u')
    palavra.replace('ù', 'u')
    palavra.replace('û', 'u')

reverso = palavra[::-1].strip().lower()

total = int(len(palavra)) - 1
print(total)

aux = ''
for i in range(total, -1, -1):
    aux += palavra[i]

if aux == palavra:
    print('É palindromo')
else:
    print('Não é')

'''
print('Isso é um palíndromo? Vamos descobrir!')
if palavra == reverso:
    print('Essa palavra é um palíndromo.')
else:
    print('Essa palavra NÃO é um palíndromo.')
'''

# Correção

pontos = 0

for i in range(0, len(palavra)):
    if palavra[i] == palavra[-i -1]:
        pontos = pontos + 1

if pontos == len(palavra):
    print('É um palíndromo')
else:
    print('Não é')