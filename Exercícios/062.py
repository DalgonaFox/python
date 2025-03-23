# Escreva um programa que crie duas listas com 5 números cada uma e exiba a soma dos elementos correspondentes das duas listas. Por exemplo, se as listas forem [1, 2, 3, 4, 5] e [5, 4, 3, 2, 1], o programa deve exibir [6, 6, 6, 6, 6].

lista1 = []
lista2 = []

for i in range (1, 6):
    num = int(input('Digite um número para a lista 1: '))
    lista1.append(num)
print('\n')

for i in range (1, 6):
    num = int(input('Digite um número para a lista 2: '))
    lista2.append(num)
print('\n')

soma = []

for i in range (0, 5):
    num = lista1[i] + lista2[i]
    soma.append(num)

print(soma)
