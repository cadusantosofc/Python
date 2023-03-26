# FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E MOSTRE NA TABELA A SUA TABUADA.

num = int(input('Digite um numeor a ser multiplicado pela tabuada: '))

one = num * 1
two = num * 2
tree = num * 3
four = num * 4
five = num * 5
six = num * 6
seven = num * 7
eigth = num * 8
nine = num * 9
ten = num * 10

print ('-'*15) 

print ('O valor {} e seus multiplos são: \n\n{} x  1 = {} \n{} x  2 = {} \n{} x  3 = {} \n{} x  4 = {} \n{} x  5 = {} \n{} x  6 = {} \n{} x  7 = {} \n{} x  8 = {} \n{} x  9 = {} \n{} x 10 = {}' .format(num, num, one, num, two, num, tree, num, four, num, five, num, six, num, seven, num, eigth, num, nine, num, ten ))

print ('-'*15)

# 2 FORMA DE FAZER

num2 = int(input('Digite um número para ver sua tabuada: '))

print ('-'*15)
print ('{} x {:2} = {}' .format (num2, 1, num2*1))
print ('{} x {:2} = {}' .format (num2, 2, num2*2))
print ('{} x {:2} = {}' .format (num2, 3, num2*3))
print ('{} x {:2} = {}' .format (num2, 4, num2*4))
print ('{} x {:2} = {}' .format (num2, 5, num2*5))
print ('{} x {:2} = {}' .format (num2, 6, num2*6))
print ('{} x {:2} = {}' .format (num2, 7, num2*7))
print ('{} x {:2} = {}' .format (num2, 8, num2*8))
print ('{} x {:2} = {}' .format (num2, 9, num2*9))
print ('{} x {:2} = {}' .format (num2, 10, num2*10))
print ('-'*15)

