#Operações Matemáticas
'''
print(8 + 9)
print(584398 - 234)
print(56 * 6)
print(6546 / 6)
print(2 ** 4)


print('Olá, mundo!')

idade = 45
print(f'Sua idade é {idade}')


#Leitura de Dados
nome = input('Seu nome é: ')
print(f'Seu nome é {nome}.')
idade = input('Sua idade é: ')
print(f'Você tem {idade} anos.')


#Tipos de Dados
idade_1 = int(input(f'Digite a primeira idade: '))
idade_2 = int(input(f'Digite a outra idade: '))

soma_idades = idade_1 + idade_2
print(f'A soma das idades é igual a {soma_idades}')

#Strings
Senai = 'Luis Eulálio'
#Fatiamento
print(Senai[0])
print(Senai[3:7])
print(Senai[:5])
print(Senai[7:])

#Análise
print(len(Senai)) # Quantas letras ao todo
print(Senai.count('l')) # Frequência de termos
print(Senai.find('l')) # Onde está?

#Senai = Senai.upper()
print(Senai.upper())
print(Senai.lower())
print(Senai.replace('L', 'P'))
print(Senai)

nome = input('Nome: ').strip('na')
print(nome)

import time
time.sleep(1)

for i in range(1, 10):
    print('*')

for i in range(1, 10):
    print(i)

for i in range(10, 1, -1):
    print(i)



#While

while contador < 5:
    print('Oi')
    contador += 1
'''

contador = 0
resposta = 'S'

while resposta != 'N':
    print(f'O contador é {contador}')
    resposta = input('Deseja continuar? ').strip().upper()[0]
    contador += 1