# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:38:04 2021

@author: Fabio Batista Rodrigues
"""
# Este programa lê um mini campo-minado composto de uma matriz, 4x4, 
# onde o número (0) indica espaços livres e o número (1) indica que 
# há uma bomba no local. O programa lê um número inteiro m de (pontos)
# tentativas, dados por linhas e colunas no campo-minado. O programa
# verifica se o ponto é uma bomba ou não. Caso seja, imprimir 1, senão 0.

campo = [[0] * 4 for _ in range(4)]

for i in range(4):
    campo[i] = list(map(int,input().split()))
    
    
tentativa = int(input())

for i in range(tentativa):
    x, y = map(int,input().split())
    if campo[x-1][y-1] == 0:
        print(0)
    else:
        print(1)
    
    
"""
(campominado00.py) Você, cansado após tantas provas, decide relaxar e fazer u
m mini campo-minado para brincar no seu tempo vago. Um mini campo-minado, é 
composto de uma matriz, 4x4, onde o número (0) indica espaços livres e o número
(1) indica que há uma bomba no local. Como no exemplo:

Campo Minado =

0	0	0	0
0	1	0	1
0	0	0	1
1	1	0	0

Nesse caso, as coordenadas (2,2), (2,4), (3,4), (4,1) e (4,2) possuem bombas.
Projetar e implementar um programa que leia um campo minado e um conjunto de
coordenadas (x,y), 1 ≤ x, y ≤ 4 e verificar se cada coordenada é ou não uma 
bomba. Caso a coordenada seja uma bomba, imprimir 1,  caso contrário imprima 
0. As coordenadas dos pontos variam de 1 a 4.

A entrada é dada por quatro linhas representando um campo-minado 4 x 4 e a 
linha seguir contém um número inteiro 0 < n <= 16, indicando a quantidade de
coordenadas (x,y) no campo minado. As n linhas seguintes contêm as coordenadas
do campo minado que devem ser analisadas.

A saída consiste em imprimir 1, caso a coordenada dada seja uma bomba
e 0 ao caso contrário.

Exemplo

# formato da entrada

0 0 0 0

0 0 0 0

0 0 0 1

0 1 1 0

3

1 1

3 4

4 4


# formato da saída

0

1

0

"""