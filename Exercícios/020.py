# Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.

sexo = input("Qual é o seu sexo? Responda com 'M' ou 'F'. ")
idade = int(input('Qual é a sua idade? '))
if idade > 16 and idade < 69:
        if idade >=61:
            doar = input("Você já doou sangue? Responda com 'Sim' ou 'Não' ")
            if doar == 'Não':
                print('Você NÃO pode doar sangue!!!')
            else:
                peso = float(input('Qual é o seu peso em kg? '))
                if peso > 50:
                    saude = input("Você tem alguma doença, tomou vacina, fez cirurgia ou algum procedimento médico recentemente? Responda com 'Sim' ou 'Não' ")
                    if saude == 'Não':
                            alcool = input("Você consumiu bebida alcoólica nas últimas 12 horas? Responda com 'Sim' ou 'Não' ")
                            if alcool == 'Não':
                                sono = int(input("Quantas horas você dormiu na última noite? "))
                                if sono >= 6:
                                    comida = input("Você já comeu hoje? Responda com 'Sim' ou 'Não' ")  
                                    if comida == 'Sim':
                                        tatuagem = input("Você fez alguma tatuagem, maquiagem definitiva ou micropigmentação nos últimos 12 meses? Responda com 'Sim' ou 'Não' ")
                                        if tatuagem == 'Não':
                                            if sexo == 'F':
                                                gravidez = input("Você está grávida? Responda com 'Sim' ou 'Não' ")
                                                if gravidez == 'Não':
                                                        parto = input("Você teve filho nos últimos 12 meses? Responda com 'Sim' ou 'Não' ")
                                                        if parto == 'Sim':
                                                            amamentacao = input("Você ainda está amamentando? Responda com 'Sim' ou 'Não' ")
                                                            if amamentacao == 'Não':
                                                                print('Você pode doar sangue!')
                                                            else:
                                                                print('Você NÃO pode doar sangue!!!')
                                                        else:
                                                            print('Você pode doar sangue!')
                                                else:
                                                    print('Você NÃO pode doar sangue!!!')
                                            else:
                                                print('Você pode doar sangue!')
                                        else:
                                            print('Você NÃO pode doar sangue!!!')
                                    else:
                                        print('Você NÃO pode doar sangue!!!')
                                else:
                                    print('Você NÃO pode doar sangue!!!')
                            else:
                                print('Você NÃO pode doar sangue!!!')
                    else:
                        print('Você NÃO pode doar sangue!!!')
                else:
                    print('Você NÃO pode doar sangue!!!')
        else:
            peso = float(input('Qual é o seu peso em kg? '))
            if peso > 50:
                    saude = input("Você tem alguma doença, tomou vacina, fez cirurgia ou algum procedimento médico recentemente? Responda com 'Sim' ou 'Não' ")
                    if saude == 'Não':
                            alcool = input("Você consumiu bebida alcoólica nas últimas 12 horas? Responda com 'Sim' ou 'Não' ")
                            if alcool == 'Não':
                                sono = int(input("Quantas horas você dormiu na última noite? "))
                                if sono >= 6:
                                    comida = input("Você já comeu hoje? Responda com 'Sim' ou 'Não' ")  
                                    if comida == 'Sim':
                                        tatuagem = input("Você fez alguma tatuagem, maquiagem definitiva ou micropigmentação nos últimos 12 meses? Responda com 'Sim' ou 'Não' ")
                                        if tatuagem == 'Não':
                                            if sexo == 'F':
                                                gravidez = input("Você está grávida? Responda com 'Sim' ou 'Não' ")
                                                if gravidez == 'Não':
                                                        parto = input("Você teve filho nos últimos 12 meses? Responda com 'Sim' ou 'Não' ")
                                                        if parto == 'Sim':
                                                            amamentacao = input("Você ainda está amamentando? Responda com 'Sim' ou 'Não' ")
                                                            if amamentacao == 'Não':
                                                                print('Você pode doar sangue!')
                                                            else:
                                                                print('Você NÃO pode doar sangue!!!')
                                                        else:
                                                            print('Você pode doar sangue!')
                                                else:
                                                    print('Você NÃO pode doar sangue!!!')
                                            else:
                                                print('Você pode doar sangue!')
                                        else:
                                            print('Você NÃO pode doar sangue!!!')
                                    else:
                                        print('Você NÃO pode doar sangue!!!')
                                else:
                                    print('Você NÃO pode doar sangue!!!')
                            else:
                                print('Você NÃO pode doar sangue!!!')
                    else:
                        print('Você NÃO pode doar sangue!!!')
            else:
                print('Você NÃO pode doar sangue!!!')

else:
    print('Você NÃO pode doar sangue!!!')
    
'''
sexo = input("Qual é o seu sexo? Responda com 'M' ou 'F'. ")
idade = int(input('Qual é a sua idade? '))
doar = input("Você já doou sangue? Responda com 'Sim' ou 'Não' ")
peso = float(input('Qual é o seu peso em kg? '))
saude = input("Você tem alguma doença, tomou vacina, fez cirurgia ou algum procedimento médico recentemente? Responda com 'Sim' ou 'Não' ")
alcool = input("Você consumiu bebida alcoólica nas últimas 12 horas? Responda com 'Sim' ou 'Não' ")
sono = int(input("Quantas horas você dormiu na última noite? "))
comida = input("Você já comeu hoje? Responda com 'Sim' ou 'Não' ")  
tatuagem = input("Você fez alguma tatuagem, maquiagem definitiva ou micropigmentação nos últimos 12 meses? Responda com 'Sim' ou 'Não' ")
gravidez = input("Você está grávida? Responda com 'Sim' ou 'Não' ")
parto = input("Você teve filho nos últimos 12 meses? Responda com 'Sim' ou 'Não' ")
amamentacao = input("Você ainda está amamentando? Responda com 'Sim' ou 'Não' ")
'''

