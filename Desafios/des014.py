# Escreva um programa que converta uma temperatura digitada em ⁰C para ⁰F. 

temp = float(input('Qual a temperatura em ⁰C: '))

cels = 9 * temp / 5 + 32

print ('A temperatura convertida de ⁰C {} para ⁰F é {:.1f}  ' .format(temp ,cels))

