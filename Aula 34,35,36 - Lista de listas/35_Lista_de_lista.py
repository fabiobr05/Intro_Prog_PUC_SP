# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:46:40 2021

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

"""
Formato da entrada
10 12

0 0 2 0 5 6 3 0 10 0 3 2

5 1 9 0 0 2 3 2 1 1 3 1

0 0 0 1 0 0 0 0 0 0 2 0

1 1 1 0 2 2 2 1 1 0 2 0

5 3 2 0 0 2 5 5 7 0 0 2

2 2 1 0 1 1 0 0 6 8 0 0

3 2 5 0 1 2 0 4 8 0 0 2

3 0 7 1 3 5 2 4 4 3 5 1

0 2 6 1 0 5 2 1 4 3 0 0

4 0 2 0 3 2 1 0 9 0 1 4

22000 25000 52000 27000 32000 21500 31125 38900 62000 71000 61000 68350

Formato da Saída

    1 R$  1426075.00
    2 R$  1201525.00
    3 R$   149000.00
    4 R$   491150.00
    5 R$  1252825.00
    6 R$  1139500.00
    7 R$  1239300.00
    8 R$  1712700.00
    9 R$  1058650.00
   10 R$  1254525.00
Total R$ 10925250.00





"""