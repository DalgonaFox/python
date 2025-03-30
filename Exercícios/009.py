# Escreva um programa que leia um tipo de dado e usando a função type(), retorne ao usuário, qual o tipo de dado informado
# Saída esperada: O dado é : <class ‘str’>

dado = input('Insira um dado. (pode ser numérico ou string.)\n')

try:
    dado = int(dado)
    tipodado = type(dado)
    print(f'O dado é: {tipodado}')
except:
    try:
        dado = float(dado)
        tipodado = type(dado)
        print(f'O dado é: {tipodado}')
    except:
        tipodado = type(dado)
        print(f'O dado é: {tipodado}')