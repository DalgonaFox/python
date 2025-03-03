# Escreva um programa que peça ao usuário uma palavra e imprima se começa com vogal ou consoante.

palavra = input('Escreva uma palavra: ').strip().lower()[0]

if palavra in 'aeiouáàãâéèêíìîóòôõúùû':
    print('Sua palavra começa com vogal.')
else:
    print('Sua palavra começa com consoante.')