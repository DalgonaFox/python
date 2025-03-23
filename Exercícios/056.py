# Usando tuplas, leia um número de 0 a 15, e retorne esse número escrito por extenso

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze')

num = int(input('Insira um número de 1 a 15.\n'))
if num < 0 or num > 15:
    print('Insira um número dentro do intervalo de 0 e 15.')
    num = int(input('Insira um número de 1 a 15.'))

print(f"O número {num} escrito por extenso é '{extenso[num]}'.")