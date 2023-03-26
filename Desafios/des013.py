# FAÇA UM ALGORITMO QUE LEIA O SALARIO DE UM FUNCIONARIO E MOSTRE SEU NOVO SALARIO COM 15% DE AUMENTO.

salario = int(input('Qual o seu salario atual ? '))

soma = salario * 15
res = soma / 100
valor = salario + res

print ('O seu novo salario será de {} Reais. ' .format(valor))

