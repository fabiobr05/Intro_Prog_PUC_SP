# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 19:51:45 2021
# Program: somamatf.py
@author: Fabio Batista Rodrigues
"""
# Este Programa lê duas matrizes de inteiros, calcula a soma das
# matrizes e imprime o resultado.
# 2 3     4 -2
# -1 3    3 -2
# 2 + 4    3 + (-2)
# -1 + 3   3 + (-2) 
# c[1][1] = a[1][1]+b[1][1]      c[1][2]=a[1][2]+b[1][2]
# c[2][1] = a[2][1]+b[2][1]      c[2][2]=a[2][2]+b[2][2]

def somamat(m, n, a, b, c):
    
    for i in range(m):
        c[i] = [a[i][j]+b[i][j] for j in range(n)]
    
    return

# pré: linhas, colunas, para i em {1,...,linhas} &&
#      para j em {1,...,colunas}: mat1[i][j] &&
#      linhas, colunas, para i em {1,...,linhas} &&
#      para j em {1,...,colunas}: mat2[i][j]


# Passo 1. Leia as matrizes
lin,col = map(int, input().split())
a = [[0]*col for _ in range(lin)]
b = [[0]*col for _ in range(lin)]
c = [[0]*col for _ in range(lin)]
for i in range(lin):
    a[i] = list(map(int, input().split()))
for i in range(lin):
    b[i] = list(map(int, input().split()))
# Passo 2. Calcule a soma
somamat(lin, col, a, b, c)
# Passo 3. Imprima o resultado linha a linha
print(c)

# pós: para todo i em {1,...,linhas}: para todo j em {1,...,colunas}: somaMat[i][j]
#      && somaMat[i][j] == mat1[i][j] + mat2[i][j]
# fim da função principal

