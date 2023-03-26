# DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE SUA MEDIA

nota1 = float(input('Qual a primeira nota ? '))
nota2 = float(input('Qual a segunda nota ? '))

resultado =  (nota1 + nota2) / 2

print ('A média entre {:.1f} e {:.1f} é: {:.1f}. ' .format(nota1, nota2, resultado))

