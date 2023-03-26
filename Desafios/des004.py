# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçoes possiveis

leia = input ('Digite algo! ')

print ('O valor de {}'.format (leia ) ,'é Numérico ? R:', leia.isnumeric())
print ('O valor de {}'.format (leia ) ,'é Alfa Numérico ? R:', leia.isalnum())
print ('O valor de {}'.format (leia ) ,'é Alfabético ? R:', leia.isalpha())
print ('O valor de {}'.format (leia ) ,'é Espaçado ? R:', leia.isspace())
print ('O valor de {}'.format (leia ) ,'é Decimal ? R:', leia.isdecimal())
print ('O valor de {}'.format (leia ) ,'é Identificador ? R:', leia.isidentifier())