# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois, deve mostrar para cada palavra, suas vogais

palavras = ('flor', 'girassol', 'menino', 'namorado', 'python')

for i in palavras:
    print(f'\nA palavra {i} tem as vogais', end=': ')
    if i.find('a') != -1:
        print('a ', end='')
    if i.find('e') != -1:
        print('e ', end='')
    if i.find('i') != -1:
        print('i ', end='')
    if i.find('o') != -1:
        print('o ', end='')
    if i.find('u') != -1:
        print('u')