# FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO

valor = int(input('Qual o preço com pontuação ? '))

# ex: 10,00 x 5 = 50 / 100 = 0.5 que é 10 reais - 0,5 = 9,5 reais

mult = 5 * valor
div = mult / 100
res = valor - div

print ('O valor com desconto fica em {} reais. Sendo o desconto de {} R$ ' .format(res, div))

