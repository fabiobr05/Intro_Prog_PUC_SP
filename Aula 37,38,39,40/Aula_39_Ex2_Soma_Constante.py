# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:16:05 2021
Program: somasconst.py
@author: fabio
"""
# Este programa lê uma matriz quadrada e verifica se possui somas
# constantes. Ou seja, se a soma das linhas, colunas e diagonais principal
# e secundária tem o mesmo valor.

# Leia o tamanho da matriz
n = int(input())
# Inicialize a matriz
matriz = [[0]*n for _ in range(n)]
# Leia a matriz linha a linha 
for i in range(n):
    matriz[i] = list(map(int, input().split()))
# Incialize a mensagem 
msg = 'CONSTANTE'
# Incialize as variaveis 
diag1 = 0
diag2 = 0
# Calcule as somas das linhas colunas e diagonais
i = 0
while i < n:
# Some o elemento da linha i nas diagonais 
    diag1 = diag1 + matriz[i][i]
    diag2 = diag2 + matriz[i][n-1-i]
# Some as linhas e as colunas
    somalin = 0
    somacol = 0
    for j in range(n):
        somalin = somalin + matriz[i][j]
        somacol = somacol + matriz[j][i]
# Armazene a soma da primeira linha
    if i == 0:
        soma = somalin
# Verifique se as somas das linhas e colunas são iguais a soma    
    if soma != somalin or soma != somacol:
        msg = 'NÃO É CONSTANTE'
        i = 2*n
# Calcule a proxima linha, coluna, diagonais
    i = i + 1
# Verificar as diagonais
if soma != diag1 or soma != diag2:
    msg = 'NÃO É CONSTANTE'
# Imprima o resultado
print(msg)
    
    
    
    
