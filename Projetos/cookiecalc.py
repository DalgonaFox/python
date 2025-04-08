# Cookie Calculator

'''
Ingredientes:
125g manteiga
3/4 xícara de açúcar 150g
1/2 xícara de açúcar mascavo 100g
1 ovo
1 e 3/4 de xícara de farinha de trigo 210g
1 colher (chá) de fermento em pó 4g
200 g de chocolate meio amargo picado
1 colher (chá) de essência de baunilha 13g
'''

receita = {
    "manteiga": 125,
    "acucar": 150,
    "mascavo": 100,
    "ovo": 1,
    "farinha": 210,
    "fermento": 4,
    "chocolate": 200,
    "baunilha": 4
}

estoque = {
    "manteiga": 500,
    "acucar": 1000,
    "mascavo": 1000,
    "ovo": 20,
    "farinha": 1000,
    "fermento": 100,
    "chocolate": 1000,
    "baunilha": 30
}

precos = {
    "manteiga": 7,
    "acucar": 4,
    "mascavo": 20,
    "ovo": 20,
    "farinha": 6,
    "fermento": 4,
    "chocolate": 30,
    "baunilha": 4
}

custo_fornada = sum((receita[i] * precos[i]) / estoque[i] for i in receita)
max_fornadas = min(estoque[i] // receita[i] for i in receita)
custo_total = sum(precos[i] for i in precos)
preco_final = max_fornadas * custo_fornada

print(f'Preço por fornada de cookie: R${round(custo_fornada, 2)}')
print(f'Preço por unidade de cookie: R${round(custo_fornada / 12, 2)}')
print(f'Quantas fornadas de cookie dá pra fazer? {max_fornadas}')
print(f'Gasto inicial: {custo_total}')
print(f'Custo final das fornadas: {preco_final}')
print(f'Montante final se o cookie for R$4: {5 * 10 * max_fornadas}')
print(f'Lucro (gasto inicial): {(5 * 12 * max_fornadas) - custo_total}')
print(f'Lucro (gasto fornadas (sem sobras)): {(5 * 12 * max_fornadas) - preco_final}')
print(f'Lucro (por fornada): {(5 * 12) - custo_fornada}')

