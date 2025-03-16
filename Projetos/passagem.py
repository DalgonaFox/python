# calcular número de passagens

print('Calculadora - Passe Estudantil')
print('\n----------------------------------------------')
aulas = int(input('Quantas aulas semanais você tem? -----> '))

print('\n----------------------------------------------')
print('Passe Estudantil Guarupass')
guarupass = int(input('Insira o seu saldo!\n'))
onibus = 2.55
print(f'Você consegue comprar {round(guarupass / onibus)} passagens e ir à {round(guarupass / (onibus * 2))} dias de aula, equivalentes a {round((guarupass / (onibus * 2))/ aulas)} semanas.')

print('\n----------------------------------------------')
print('Bilhete Único')
bilhete = int(input('Insira o seu saldo!\n'))
trem = 2.60
print(f'Você consegue comprar {round(bilhete / trem)} passagens e ir à {round(bilhete / (trem * 2))} dias de aula, equivalentes a {round((bilhete / (trem * 2))/ aulas)} semanas.')

print('\n----------------------------------------------')
print('TOP')
top = int(input('Insira o seu saldo!\n'))
treminteira = 5.20
print(f'Você consegue comprar {round(top / treminteira)} passagens e ir à {round(top / (treminteira * 2))} dias de aula, equivalentes a {round((top / (treminteira * 2))/ aulas)} semanas.')

print('\n----------------------------------------------')
print('Ribeirão Pires')
onibusribeirao = 7.95
print(f'Você consegue comprar {round(top / onibusribeirao)} passagens, ir e voltar {round(top / (onibusribeirao * 2))} vezes.')


