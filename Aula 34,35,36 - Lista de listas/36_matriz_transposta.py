# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:03:37 2021

@author: Fabio Batista Rodrigues
"""
# Matriz transposta, em matemática, é o resultado da troca de linhas por 
# colunas em uma determinada matriz. Este programa lê um número inteiro
# n indicando a quantidade de matrizes, (com no máximo 100 linhas e
# 100 colunas < 100) em diversos formatos, lê as matrizes e computa e
# imprime a matriz transposta para cada uma dessas matrizes da entrada.

# pré: m, n, para i em {0,...,m-1} &&
#      para j em {0,...,n-1}: A[i][j] 

lin, col = map(int,input().split())

# Inicializar matriz
mat = [[0] * col for _ in range(lin)]
# Inicializar matriz transposta
matt = [[0] * lin for _ in range(col)]

# Receber cada linha
for i in range(lin):
    mat[i] = list(map(int,input().split()))

# trocar linha por coluna
for i in range(col):
    for j in range(lin):
        matt[i][j] = mat[j][i]
"""
Outra maneira de fazer que funciona em python

matt  = [[mat[j][i] for j in range(lin)] for i in range(col)]
"""
# Imprimir mensagem correspondente 
for i in range(col):
    print(matt[i])

# pós: n, m, para j em {0,...,n-1} &&
#      para i em {0,...,m-1}: A[j][i] 