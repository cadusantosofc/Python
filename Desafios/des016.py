# CRIE UM PROGRAM QUE LEIA UM NUMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA. EX: DIGITE UM NUMERO 6.127. O NUMENRO 6.127 TEMA PARTE INTEIRA 6.

from math import trunc

valor = float(input('Digite um número: '))
inteiro = trunc (valor)

print ('O número {} tem a parte inteira {}.'.format(valor, trunc (inteiro)))

