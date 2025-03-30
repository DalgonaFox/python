# Escreva um programa que leia um tipo de dado e usando um método .isnumeric(), retorne ao usuário
# Saída esperada: O dado informado é número? TRUE / FALSE

dado = input('Insira um dado: ')
tipo = dado.isnumeric()

print(f'O dado informado é número? {tipo}')