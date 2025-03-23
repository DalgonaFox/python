# Crie uma função para verificar se um número é par ou ímpar

def parimpar(num):
    if num % 2 == 0:
        print('Esse número é par.')
    else:
        print('Esse número é ímpar.')

numero = int(input('Digite um número: '))
parimpar(numero)