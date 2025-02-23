# Crie um programa que leia um nome, e mostre o primeiro e o último nome

nome = input("Insira o seu nome completo: ")

espaco = (nome.find(' '))
total = len(nome)
espaco2 = (nome.rfind(' '))

print(nome.upper())
print(nome.lower())
print(len(nome))
print("Primeiro nome: " + nome[:espaco])
print("Último nome: " + nome[espaco2:])