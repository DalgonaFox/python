# Crie um programa onde o usuário possa digitar sete letras, e cadastre em uma única lista, que mantenha separado as consoantes das vogais

letras = []
vogais = []
consoantes = []

for i in range(1,8):
    letra = input('Insira uma letra(sem acentos): ').lower().strip()[0]
    if letra in 'aeiou':
        vogais.append(letra)
    else:
        consoantes.append(letra)

letras.append(vogais[:])
letras.append(consoantes[:])
print(letras)
print(letras[0])
print(sorted(vogais))



'''
palavras = [
    "abacate", "banana", "carro", "dado", "elefante", "fogo", "gato", "helicóptero", "igreja", "janela",
    "kiwi", "limão", "macaco", "navio", "olho", "pato", "queijo", "rosa", "sapato", "tigre",
    "uva", "vaca", "xadrez", "yoga", "zebra", "amarelo", "branco", "cinza", "dourado", "escuro",
    "frio", "grande", "humano", "inteligente", "jovem", "lindo", "mágico", "nobre", "ousado", "pequeno",
    "quente", "rápido", "simples", "tímido", "único", "verde", "xampu", "yoga", "zero",
    # Palavras adicionais
    "amigo", "bola", "cachorro", "doce", "eletricidade",
    "felicidade", "girafa", "hamburguer", "inverno", "jardim",
    "ketchup", "limonada", "melancia", "nariz", "ouro",
    "piano", "quadro", "raio", "sorvete", "telefone",
    "uísque", "viagem", "xadrez", "yoga", "zumbi"
]
'''