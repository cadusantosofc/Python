# escreva um programa que leia um valor em metros e o exiba convertido em centimentros e milimetros

valor = float(input('Digite o valor em metros: '))

cent = valor * 100

mil = valor * 1000

print (' Você converteu {} Metros em {:.0f} centimentos que da em torno de {:.0f} Milimetros' .format(valor, cent, mil))
