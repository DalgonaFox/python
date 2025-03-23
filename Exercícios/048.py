# Crie um programa que pede ao usuário para digitar dois números e, em seguida, divida o primeiro número pelo segundo número. No entanto, o programa deve ser capaz de lidar com a possibilidade de o usuário digitar um valor inválido, como uma string ou o número zero.
# ZeroDivisionError ; ValueError

n1 = input('Insira um número: ')
n2 = input('Insira outro número: ')

try:
    print(f'O resultado da divisão é {int(n1) / int(n2)}')
except ZeroDivisionError:
    print("Não se pode dividir nada por zero.")
except ValueError:
    print('Você digitou uma string em vez de um número.')
