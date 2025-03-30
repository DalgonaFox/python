# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

expressao = input('Insira uma expressão matemática par análise.\n')
abre = expressao.count('(')
fecha = expressao.count(')')

if abre == fecha:
    print('Sua expressão está correta.')
elif abre > fecha:
    if abre - fecha == 1:
        print(f"Você esqueceu de fechar {abre - fecha} parênteses aberto com ')'")
    else:
        print(f"Você esqueceu de fechar {abre - fecha} parênteses abertos com ')'")
else:
    if fecha - abre == 1:
        print(f"Você esqueceu de abrir {fecha - abre} parênteses fechado com '('")
    else:
        print(f"Você esqueceu de abrir {fecha - abre} parênteses fechados com '('")