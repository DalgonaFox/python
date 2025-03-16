# Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:
# 1.	Somar
# 2.	Multiplicar
# 3.	Maior
# 4.	Novos números
# 5.	Sair do programa

opcao = 0
n1 = int(input('Insira um número: '))
n2 = int(input('Insira um número: '))
n3 = int(input('Insira um número: '))

print('Calculadora\n1. Somar\n2. Multiplicar\n3. Maior\n4. Novos números\n5. Sair do programa')

while opcao != 5:
    opcao = int(input('Escolha uma opção:\n'))
    if opcao == 1:
        print(f'{n1} + {n2} + {n3} = {n1+n2+n3}')
    elif opcao == 2:
        print(f'{n1} * {n2} * {n3} = {n1 * n2 * n3}')
    elif opcao == 3:
        if n1 > n2 and n1 > n3:
            print(f'{n1} é o Maior número.')
        elif n2 > n1 and n2 > n3:
            print(f'{n2} é o Maior número.')
        elif n3 > n1 and n3 > n2:
            print(f'{n3} é o Maior número.')
        elif n1 == n2 == n3:
            print(f'Todos os números são iguais.')
        elif n1 == n2:
            print(f'{n1} e {n2} são iguais.')
        elif n2 == n3:
            print(f'{n2} e {n3} são iguais.')
        elif n1 == n3:
            print(f'{n1} e {n3} são iguais.')
    elif opcao == 4:
        n1 = int(input('Insira um número: '))
        n2 = int(input('Insira um número: '))
        n3 = int(input('Insira um número: '))
    elif opcao == 5:
        print('Tchauzinho!')
    else:
        print('Opcão inválida!')
