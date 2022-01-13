# -*- coding: utf-8 -*-
# Programa: intervalo.py
# Programador:
# Data: 29/05/2016
# Este programa lê quatro notas de uma prova, calcula a maior e a
# menor nota e a diferença entre elas e imprime o resultado
# início do módulo principal
# descrição das variáveis utilizadas
# float nota1, nota2, nota3, nota4
# float maiornota, menornota, intervalo
 
# pré: nota1 nota2 nota3 nota4

# Passo 1. Leia as Notas
nota1, nota2, nota3, nota4 = map(float, input().split()) 
# Passo 2. Calcule a maior e a menor nota

if nota1 > nota2 and nota1 > nota3 and nota1 > nota4:
    maiornota = nota1
if nota2 > nota1 and nota2 > nota3 and nota2 > nota4:
    maiornota = nota2
if nota3 > nota1 and nota3 > nota2 and nota3 > nota4:
    maiornota = nota3
if nota4 > nota1 and nota4 > nota2 and nota4 > nota3:
    maiornota = nota4
if nota1 < nota2 and nota1 < nota3 and nota1 < nota4:
    menornota = nota1
if nota2 < nota1 and nota2 < nota3 and nota2 < nota4:
    menornota = nota2
if nota3 < nota1 and nota3 < nota2 and nota3 < nota4:
    menornota = nota3
if nota4 < nota1 and nota4 < nota2 and nota4 < nota3:
    menornota = nota4
# Passo 3. Calcule a variacao entre as notas
intervalo = maiornota - menornota
# Passo 4. Imprima o valor do intervalo
print('Maior nota: {0:4.1f}'.format(maiornota))
print('Menor nota: {0:4.1f}'.format(menornota))
print('Variação  : {0:4.1f}'.format(intervalo))

# pós: maiornota == max{nota1, nota2, nota3, nota4} and
#      menornota == min{nota1, nota2, nota3, nota4} and
#      intervalo == maiornota - segmaiornota
# fim do módulo principal
