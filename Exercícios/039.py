# Faça um programa que leia um número e retorne o fatorial !
# Ex: 4! = 4 x 3 x 2 x 1

num = int(input('Insira um número!\n'))
contador = num
resultado = num

print(f'{num}! = {num}', end=" ")
while contador > 1:
    contador = contador - 1
    resultado = resultado * (num - 1)
    print(f'x {num - 1}', end=" ")
    num = num - 1
    
print(f"= {resultado}")

