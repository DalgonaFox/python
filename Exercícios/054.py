# Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:
# Apenas os 3 primeiros mais assistidos
# Os últimos 2 mais assistidos
# A lista em ordem alfabética
# Em que posição está “O rei leão”

filmes = ('Avatar', 'Vingadores: Ultimato', 'Avatar: O Caminho da Água', 'Titanic', 'Star Wars: O Despertar da Força', 'Vingadores: Guerra Infinita', 'Homem-Aranha: Sem Volta Para Casa', 'Jurassic World', 'O Rei Leão', 'Os Vingadores', )

print('\nOs 3 primeiros filmes mais assistidos foram:')
for i in range (0, 3):
    print(filmes[i])

print('\n\nOs últimos 2 filmes mais assistidos foram:')
for i in range ((len(filmes) - 2), len(filmes)):
    print(filmes[i])

print('\n\nA lista de filmes em ordem alfabética é: ')
for i in sorted(filmes):
    print(i)

print(f"\nO filme 'O Rei Leão' está na posição {filmes.index('O Rei Leão')}")