# Escreva um programa que peça ao usuário uma senha e verifique se ela está correta (a senha correta é "python123").

senha = input('Digite a senha correta: ')

if senha == 'python123':
    print('Senha correta!')
else:
    print('Senha errada. Tente novamente.')