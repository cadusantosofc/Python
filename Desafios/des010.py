# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DOLARES ELA PODE COMPRAR. CONSIDERE US$1.00 = 3,27

# CONVERTENDO REAL BRASILEIRO EM DOLAR

dinheiro = float(input('Quanto você tem de dinheiro agora em reais ? '))

dolar = dinheiro / 3.27

print ('Com {:.2f} reais, você consegue comprar US$ {:.2f} dólares Americanos. ' .format(dinheiro, dolar ))

# CONVERTENDO DOLAR EM REAL BRASILEIRO

convert = float(input('Quantos Dólares você quer converter em reais ? '))

convert2 = convert * 3.27

print ('Seus {:.2f} Dolares convertidos em reais dariam {:.2f} R$ ' .format(convert, convert2))

