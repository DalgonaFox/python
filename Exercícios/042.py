# Simulação de um Caixa Eletrônico Este programa simula um caixa eletrônico, permitindo que o usuário faça depósitos, saques e consulte o saldo da conta, e sair

opcao = 0

print('----------------------------------------')
print('Caixa Eletrônico')
print('1. Depositar\n2. Sacar\n3. Saldo\n4. Sair')
print('----------------------------------------')
saldo = 0

while opcao != 4:
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        deposito = float(input('Insira o valor do depósito: R$'))
        saldo = saldo + deposito
        print('----------------------------------------')
    elif opcao == 2:
        saque = float(input('Insira o valor do saque: R$'))
        if saque > saldo:
            print('Você não tem saldo suficiente.')
        else:
            saldo = saldo - saque
        print('----------------------------------------')
    elif opcao == 3:
        print(f'O seu saldo é de R${saldo}')
        print('----------------------------------------')
    elif opcao == 4:
        print('Até a próxima!')
        print('----------------------------------------')
    else:
        print('Insira um valor válido.')
        print('----------------------------------------')




