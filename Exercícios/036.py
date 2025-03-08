# Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos

maiorpeso = 0
menorpeso = 1000

for i in range (1, 8):
    peso = float(input('Insira o peso: '))

    if peso > maiorpeso:
        maiorpeso = peso
    elif peso < menorpeso:
        menorpeso = peso

print(f'O maior peso foi: {maiorpeso} kg')
print(f'O menor peso foi: {menorpeso} kg')