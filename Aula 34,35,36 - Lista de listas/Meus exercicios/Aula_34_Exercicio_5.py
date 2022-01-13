# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 23:09:14 2021

@author: Fabio Batista Rodrigues
"""
# Projete e implemente um programa para ler duas m x n matrizes, 0 < m,n <= 100
# de inteiros, calcular a sua soma, a matriz C, e imprimir C, onde cada
# elemento da matriz C, cij é dado por:
# cij = aij + bij

# Ler numero de linhas e colunas da matriz
linhas, colunas = map(int, input().split())
# Inicializando as matrizes
a = [[0]*colunas for i in range(linhas)]
b = [[0]*colunas for i in range(linhas)]
c = [[0]*colunas for i in range(linhas)]

# Ler matriz A
for i in range(linhas):
    a[i] = list(map(int, input().split()))[:colunas]
# Ler matriz B
for i in range(linhas):
    b[i] = list(map(int, input().split()))[:colunas]
    
# Computar a soma de A com B
for i in range(linhas):
    for j in range(colunas):    
        c[i][j] = a[i][j] + b[i][j]


for i in range(linhas):
    print(c[i])

