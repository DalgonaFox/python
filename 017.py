# Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.

letra = input('Digite uma letra: ')

if letra == 'a' or letra == 'A':
    print(f'A letra {letra} é uma vogal!')
elif letra == 'e' or letra == 'E':
    print(f'A letra {letra} é uma vogal!')
elif letra == 'i' or letra == 'I':
    print(f'A letra {letra} é uma vogal!')
elif letra == 'o' or letra == 'O':
    print(f'A letra {letra} é uma vogal!')
elif letra == 'u' or letra == 'U':
    print(f'A letra {letra} é uma vogal!')
else:
    print(f'A letra {letra} é uma consoante.')