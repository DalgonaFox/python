'''
#Operações Matemáticas

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


contador = 0
resposta = 'S'

while resposta != 'N':
    print(f'O contador é {contador}')
    resposta = input('Deseja continuar? ').strip().upper()[0]
    contador += 1


while True:
    print('1. Opção X \n'
          '2. Opção Y \n'
          '3. Sair')
    menu = int(input('Digite a escolha: '))

    if menu == 3:
        break


try:
    # código que pode gerar uma exceção
    x = 10 / 0

except ZeroDivisionError:
    # código a ser executado caso ocorra uma exceção do tipo ZeroDivisionError

    print("Erro: divisão por zero")
    


def mostraLinha():
    print('-*-' * 10)

mostraLinha()

def titulo(msg):
    print('-*-' * 10)
    print(msg)
    print('-*-' * 10)
titulo('Olá')

def Soma(a,b):
    S = a + b
    print(S)
    return S

Soma(1,30)


# Variável composta
# IMUTÁVEL
# Representado por ()
# Seguem a mesma estrutura de fatiamento das Strings
# Podem ser deletados por del(lanche)
# sorted() - coloca a tupla em ordem alfabética
lanche = ('Suco', 'Coxinha', 'Pizza')

carro = ('Ferrari', 'Vermelha', '2023')
print(carro)

for ele in carro:
   print(ele)

for count in range(0, len(carro)):
   print(carro[count])

for pos, carac in enumerate(carro):
   print(f'Ordem de compra {carac} Cod: {pos}')


carro = ['Ferrari', 'Vermelha', '2023']
carro [1] = 'Amarelo'
carro.append('Gasolina')     # cria no final da lista
carro.insert(1, '797 cv ')   # insere na posição 1
carro.pop(1)                 # remove o item na posição 1
carro.remove('Vermelha')     # remove o valor 'vermelha'
len(carro)                   # retorna o tamanho da lista
'''

Aluno = list()           # Lista principal
dados = list()           # Lista secundária

for c in range(0, 3):
   dados.append(str(input('Nome: ')))  # Coleta de dados LS
   dados.append(int(input('Idade: ')))
   Aluno.append(dados[:]) #Inserção da cópia na LP
   dados.clear()

print(Aluno)

# Dicionários

# Índices literais
# Identificados por chaves {}

dados = {'nome':'Luis', 'idade':52}
print(dados['nome'])
print(dados['idade'])

dados['sexo'] = 'M'
# del dados['idade'] 

print(dados.values())    # Retorna os valores Luis, 52
print(dados.keys())      # Retorna nome, idade
print(dados.items())     # Retorna tudo

carro = dict ()
concessionaria = list ()


for c in range(0, 3):
    carro['nome'] = str(input('Nome do Carro '))
    carro['ano'] = int(input('Ano do Carro '))
    concessionaria.append(carro.copy())
