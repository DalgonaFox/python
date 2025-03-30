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

recipe = {
    "manteiga": 125,
    "acucar": 150,
    "mascavo": 100,
    "ovo": 1,
    "farinha": 210,
    "fermento": 4,
    "chocolate": 200,
    "baunilha": 4
}

stock = {
    "manteiga": 500,
    "acucar": 1000,
    "mascavo": 1000,
    "ovo": 20,
    "farinha": 1000,
    "fermento": 100,
    "chocolate": 1000,
    "baunilha": 30
}

prices = {
    "manteiga": 7,
    "acucar": 4,
    "mascavo": 20,
    "ovo": 20,
    "farinha": 6,
    "fermento": 4,
    "chocolate": 30,
    "baunilha": 4
}

cost_per_batch = sum((recipe[i] * prices[i]) / stock[i] for i in recipe)

max_batches = min(stock[i] // recipe[i] for i in recipe)

total_cost = sum(prices[i] for i in prices)

final_price = max_batches * cost_per_batch

print(f'Preço por fornada de cookie: R${round(cost_per_batch, 2)}')
print(f'Preço por unidade de cookie: R${round(cost_per_batch / 10, 2)}')
print(f'Quantas fornadas de cookie dá pra fazer? {max_batches}')
print(f'Gasto inicial: {total_cost}')
print(f'Custo final das fornadas: {final_price}')
print(f'Montante final se o cookie for R$4: {4 * 10 * max_batches}')
print(f'Lucro (gasto inicial): {(4 * 10 * max_batches) - total_cost}')
print(f'Lucro (gasto fornadas (sem sobras)): {(4 * 10 * max_batches) - final_price}')
print(f'Lucro (por fornada): {(4 * 10) - cost_per_batch}')

