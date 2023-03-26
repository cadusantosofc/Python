# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$ 60 POR DIA E R$ 0.15 POR KM RODADO.

km = float(input('Quantos KM rodou com o carro ? '))
dias = int(input('Quantos dias foram percorridos com o carro ? '))

temp = dias * 60
data = km * 0.15

soma = data + temp

print ('Você irá pagar pelo carro alugado o valor de R$ {:.2f}' .format (soma))

