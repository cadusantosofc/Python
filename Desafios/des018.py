# FAÇA UM PROGRAMA QUE LEIA UM TRIANGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ANGULO.

from math import sin, cos, tan, radians

ang = float(input('Digite o ângulo que você deseja: '))
seno = sin ( radians (ang))
cosseno = cos ( radians (ang))
tangente = tan ( radians (ang))

print ('O ângulo de {} tem o SENO de {:.2f}' .format (int (ang), seno))
print ('O ângulo de {} tem o COSSENO de {:.2f}' .format ( int (ang), cosseno))
print ('O ângulo de {} tem o TANGENTE de {:.2f}' .format (int (ang), tangente))


