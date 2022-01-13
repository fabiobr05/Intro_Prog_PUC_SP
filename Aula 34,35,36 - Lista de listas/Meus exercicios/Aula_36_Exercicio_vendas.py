# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 15:10:04 2021

@author: Fabio Batista Rodrigues
"""
# Este programa lê uma tabela (m x n) com as vendas de m vendedores
# para cada um dos n itens comercializados e um vetor com os valores
# de venda para os n produtos. O programa calcula e imprime a 
# o total vendido por cada vendedor, a comissão obtida por cada um
# deles e o salário semanal de cada vendedor
# início do módulo principal
"""
1. Compute o total de reais faturados por cada vendedor.
2. Se a comissão de vendas é de 10 porcento, compute o
   total de comissão por cada vendedor.
3. Se cada vendedor recebe um salário fixo de R$ 200
   por semana em adição aos pagamentos referentes às
   comissões, encontre o total do salário para
   cada vendedor referente à semana.
"""

# Entre com o tamanho da matriz
m, n = map(int, input().split())

# Declaraçao da matriz
matriz = [[0]*n for i in range(m)]
'''
# Teste para saber se a matriz esta certa
# for i in range(m):
#    print(matriz[i])
'''
# Ler entrada do usuario
for i in range(m):
    matriz[i] = list(map(int, input().split()))[:n]
# Receber o vetor com as vendas
vendas = list(map(int, input().split()))[:n]

# Computar as vendas de cada vendedor
vendedor = [0]*m
for i in range(0, m):
    cont = 0
    for j in range(0, n):
        vendedor[i] = vendedor[i] + matriz[i][j]*vendas[cont]
        # Variavel que controla a lista vendas
        cont += 1
    vendedor[i] = vendedor[i]* 0.1 + 200
    
# Saída de dados
for i in range(0, m):
    print('{0:d} {1:.2f}'.format(i+1, vendedor[i]))
# fim do módulo principal

"""
Exemplo 1
# formato da entrada
4 5 # tamanho da matriz (linhas, colunas)
10 4 5 6 7 # linha 1 da matriz
7 0 12 1 3 # linha 2 da matriz
4 9 5 0 8 # linha 3 da matriz
3 2 1 5 6 # linha 4 da matriz
100 75 120 150 35 # vetor com as vendas

# formato da saída
1 504.50
2 439.50
3 395.50
4 353.00

Exemplo 2
# formato da entrada
2 3 # tamanho da matriz (linhas, colunas)
20 8 15 # linha 1 da matriz
9 30 20 # linha 2 da matriz
90 85 300 # vetor com as vendas

# formato da saída
1 898.00
2 1136.00
"""