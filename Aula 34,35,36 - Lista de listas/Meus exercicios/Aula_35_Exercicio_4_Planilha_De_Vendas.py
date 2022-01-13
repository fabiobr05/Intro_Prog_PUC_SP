# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 10:28:22 2021

@author: Fabio Batista Rodrigues
"""

# Projete e implemente um programa para ler a planilha das vendas, onde cada
# linha representa a quantidade de vendas de cada vendedor para cada um dos
# modelos comercializado, e a lista de preços dos automóveis. Calcule o total
# de reais vendidos por cada vendedor e o total de reais das vendas de todos
# os vendedores. 
# A entrada é dada por um bloco, onde a primeira linha do bloco indica as
# dimensões m <= 25 e n <= 25 da tabela de vendas, seguida de m linhas, com
# n colunas, cada uma representando a tabela das vendas da revenda e um vetor
# com n linhas representado o valores de venda de cada modelo comercializado
# pela revenda. A saída consiste em imprimir tabela com os valores das vendas
# totais de cada um do m vendedores e a venda total da revenda com cabeçalhos
# apropriados. Utilize o seguinte formato para imprimir os resultados:
    
# tabela[m][n] * preco[m][1] = total[m][1]

# Ler os dados
lin, col = map(int,input().split())

# Inicializar a tabela
tabela = [[0]*col for i in range(lin)]

for i in range(lin):
    tabela[i] =  list(map(int,input().split()))
precos = list(map(float,input().split()))

# Calcular o produto da tabela pelo vetor de produto
vendas = [0.0]*lin
for i in range(lin):
    for j in range(col):
        vendas[i] += tabela[i][j] * precos[j]
total = sum(vendas)
# Imprimir o resultado
for i in range(lin):
    print('{0:5d} R${1:12.2f}'.format(i+1,vendas[i]))

print('Total R${0:12.2f}'.format(total))
