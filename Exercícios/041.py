# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

contador = 0
totalnum = 0
soma = 0
maior = 0

num = int(input('Insira um número: '))
menor = num

while contador < 1:
    num = int(input('Insira um número: '))
    totalnum += 1
    soma += num

    if num > maior:
        maior = num

    if num < menor:
        menor = num

    fim = input('Você quer continuar? S/N ---> ').strip().upper()[0]
    if fim == 'N':
        contador +=1

print(f'A média de todos os números é {round(soma / totalnum)}\nO maior número é {maior}.\nO menor número é {menor}')