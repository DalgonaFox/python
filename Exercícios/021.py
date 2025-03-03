# Escreva um programa que peça ao usuário um número de 1 a 7 e imprima o dia da semana correspondente (1 é segunda-feira, 2 é terça-feira, etc.).

dia = int(input('Digite um número de 1 a 7: '))

if dia == 1:
    print('Segunda-feira')
elif dia == 2:
    print('Terça-feira')
elif dia == 3:
    print('Quarta-feira')
elif dia == 4:
    print('Quinta-feira')
elif dia == 5:
    print('Sexta-feira')
elif dia == 6:
    print('Sábado')
elif dia == 7:
    print('Domingo')
else:
    print('Digite um número no intervalo correto >:(')