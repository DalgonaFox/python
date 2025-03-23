# Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000

while True:
    num = int(input('\nDigite um número: '))
    if num == 0000:
        print('\nTchau!')
        break
    else:
        print(f'\nTabuada do {num}')
        for i in range (1, 11):
            print(f'{num} * {i} = {num * i}')

