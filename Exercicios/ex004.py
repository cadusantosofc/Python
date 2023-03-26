# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveissobre ela.

a = input ('Digite algo: ')

print ('o tipo primitivo desse valor é ', type(a))
print ('Só tem espaços ? ', a.isspace()) 
print ('É um número ? ', a.isnumeric())
print ('É alfa numérico ? ', a.isalnum())
print ('É alfabético ?' , a.isalpha())
print ('Está em maiúsculas ? ', a.isupper())
print ('Está em minúsculas ? ', a.islower())
print ('Está capitálizada ? ', a.istitle())
