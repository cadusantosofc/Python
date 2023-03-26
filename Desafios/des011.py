# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA AREA E A QUANTIDADE DE TINTA NECESSARIA PARA CADA LITRO DE TINTA PINTA UMA AREA DE 2M²

largura = float(input('Qual a Largura da parede ? '))
altura = float(input('Qual a Altura da parede ? '))

area = largura * altura
tinta = area / 2

print ('-'*35)

print ('\nSua parede tem dimensão de {} x {} Corereto? \n\nSomando, o tamanho de sua parede é de {:.2f} M². \n\nPara isso você irá gastar nessa parede um total de {:.3f} ML de Tinta \n'. format(largura, altura, area, tinta))

print('-'*35)

