# Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.

peso = float(input('Insira o seu peso em kg: '))
altura = float(input('Insira a sua altura em m: '))

imc = peso / (altura ** 2)

if imc >= 25:
    print('IMC acima do ideal.')
elif imc >= 18.5:
    print('IMC ideal!')
else:
    print('IMC abaixo do ideal.')