# Escreva um programa que leia uma frase, e mostre uma formatação adaptável de acordo com o tamanho da frase, coordenado por uma função
# Exemplo:
#       ----------------------------
#            Senai Show de bola
#       ----------------------------

def formatar(frase):
    quantidade = len(frase)
    print('-' * (10 + quantidade))
    print(' ' * 4, frase)
    print('-' * (10 + quantidade))

msg = input('Digite uma frase: ')
formatar(msg)