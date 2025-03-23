# Crie um programa onde serão informados diversos valores em uma lista. Caso o número já exista ele não será adicionado. No final, serão exibidos todos os valores únicos em ordem crescente

lista = []

while True:
    num = int(input('Insira um número na lista: '))

    if num in lista:
        print('Esse número já existe na lista.')
    else:
        lista.append(num)

    escolha = input('Você quer inserir mais números na lista? S/N\n').strip().upper()[0]
    if escolha == 'N':
        break

print(sorted(lista))
