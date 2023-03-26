# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAM QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO. 

from random import choice

one = str (input ('Primeiro nome: '))
two = str (input ('Segundo nome: '))
tree = str (input ('Terceiro nome: '))
four = str (input ('Quarto nome: '))

lista = [one, two, tree, four] 
escolhido = choice(lista)

print ('O aluno escolhido foi {}' .format (escolhido))