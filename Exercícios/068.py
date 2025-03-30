# Escreva um programa que crie um dicionário com as informações de 5 livros, como título, autor, ano de lançamento e número de páginas. Em seguida, exiba apenas os autores dos livros.

livros = []

for i in range (1, 6):
    livro = {}
    livro['Título'] = str(input('Título: '))
    livro['Autor'] = str(input('Autor: '))
    livro['Ano de lançamento'] = str(input('Ano de lançamento: '))
    livro['Num. páginas'] = str(input('Num. páginas: '))
    livros.append(livro)

autores = [l['Autor'] for l in livros]
print(f'Todos os autores: {autores}')
