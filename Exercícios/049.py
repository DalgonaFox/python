# Crie um programa que tenha a função área(), que receba as dimensões de um muro retangular e mostra a área do terreno

def área(a,b):
    A = a * b
    print(A)
    return A

a = int(input('Digite a altura: '))
b = int(input('Digite a largura: '))
print('A área do muro retangular é', end=' ')
área(a,b)
