# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 10:50:26 2021
Program: produto.py
@author: Fabio Batista Rodrigues
"""
# Projete e implemente um programa que leia duas matrizes A (m x n) e B (r x s)
# de inteiros e compute o produto C das matrizes. A entrada é dada por dois 
# blocos de linhas. A primeira linha do primeiro bloco contém dois números 
# inteiros m e n, indicando o número de linhas e colunas da matriz A, seguido 
# de m linhas, cada uma com n elementos, representando as colunas da matriz A. 
# A primeira linha do segundo bloco contém dois números inteiros r e s, indicando
# o número de linhas e colunas da matriz B, seguido de r linhas, cada uma com s 
# elementos, representado as colunas da matriz B. A saída consiste imprimir as m 
# linhas da matriz produto C, cada uma com n == r elementos.

# Insira o numero de linhas e colunas da matriz A
print('entre com as dimençoes')
m, n = map(int, input().split())
# Inicialize a matriz A
A = [[0]*n for _ in range(m)]
# Insira a matriz A
for i in range(m):
    A[i] = list(map(int, input().split()))[:n]
# Insira o numero de linhas e colunas da matriz B
r, s = map(int, input().split())
# Inicialize a matriz B
B = [[0]*s for _ in range(r)]
# Insira a matriz B
for i in range(r):
    B[i] = list(map(int, input().split()))[:s]

if n == r:
    # Multiplicaçao das matrizes
    # Inicialize a matriz resultante
    C = [[0]*s for _ in range(m)]
    # Loop para controlar a linha da matriz A
    for i in range(m):
        # Zerar contador toda vez que o processo se iniciar
        # Ele controla a coluna de C e B
        cont = 0
        # Loop para deslocar o local de armazenamento a 'direita' da matriz m vezes
        for _ in range(m):
            # Loop para controlar o numero de vezes que a conta vai se repetir
            for j in range(r):
                C[i][cont] = C[i][cont] + A[i][j] * B[j][cont]
            # Contador que desloca o armazenamento e o armazenamento de B
            cont += 1

    # Imprimir matriz correspondente
    for i in range(m):    
        print(C[i])
# Se não imprimir mensagem correspondente
else:
    print('produto não definido')


"""
Testes
C = [[0]*s for _ in range(m)]
cont = 0
# Rellize a operaçao de multiplicaçao
for i in range(m):
    for j in range(r):
        C[i][cont] = C[i][cont] + A[i][j] * B[j][i]
    cont += 1
"""
"""
C[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0]
C[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1]
C[0][2] = A[0][0]*B[0][2] + A[0][1]*B[1][2]

C[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0]
C[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1]
C[1][2] = A[1][0]*B[0][2] + A[1][1]*B[1][2]

C[2][0] = A[2][0]*B[0][0] + A[2][1]*B[1][0]
C[2][1] = A[2][0]*B[0][1] + A[2][1]*B[1][1]
C[2][2] = A[2][0]*B[0][2] + A[2][1]*B[1][2]
"""

# Exemplos de entrada

"""
Exemplo 1

# formato da entrada

3 2

0 6

-1 2

2 3

2 3

2 2 -2

3 -2 5


# formato da saída
[18, -12, 30]
[4, -6. 12]
[13, -2, 11]



Exemplo 2
# formato da entrada
2 3
1 4 3
2 7 -1
3 2
-6 3
2 -1
-4 7

# formato da saída
[-10, 20]
[6, -8]
"""