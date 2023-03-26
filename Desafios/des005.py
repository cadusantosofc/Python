# FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR. 

# PRIMEIRA FORMA DE RESOLVER 

leia = int(input('Digite um valor: '))

v = leia - 1
w = leia + 1 

print ('O numero selecionado foi {} e o seu antecessor é {} e seu sucessor é {}' .format(leia, v, w))

# SEGUNDA FORMA DE RESOLVER 

valor = int(input('Digite o segundo valor ? '))

print ('Lendo o numero {}, Seu antecessor é {} e seu sucessor é {} '.format(valor, (valor-1), (valor+1)))

