# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo (sem considerar os espaços)
# Quantas letras tem o primeiro nome


nome = input("Insira o seu nome completo: ").strip()
espaco = (nome.find(' '))
espacos = (nome.count(' '))
total = len(nome)

print(nome.upper())
print(nome.lower())
print(total - espacos)
print(nome[:espaco])




