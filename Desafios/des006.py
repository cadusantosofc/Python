# crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

leia = int(input('Qual o numero: '))

d = leia * 2
tri = leia * 3
raiz = leia ** (1/2)

print ('\nO numero escolhido foi {} \nseu dobro é {} \nseu triplo é {} \ne sua raiz é {:.2f}' .format(leia, d, tri, raiz))

# 2 FORMA DE FAZER 

recebe = int(input('Qual o numero ? '))

print ('\n\nO numero escolhido foi {} \nSeu dobro é {} \nSeu triplo é {} \nSua raiz è {:.2f} '.format(recebe, (recebe*2),(recebe*3), (recebe**(1/2))))

