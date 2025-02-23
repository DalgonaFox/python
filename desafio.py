tempo = int(input('Informe o tempo: '))
aceleração = int(input('Informe a aceleração: '))
so = int(input('Informe o espaço inicial: '))
vo = int(input('Informe a velocidade inicial: '))

mruv = so + vo * tempo + aceleração * (tempo ** 2)/2

print(f'A posição do objeto no tempo {tempo} é de {mruv} (m)')