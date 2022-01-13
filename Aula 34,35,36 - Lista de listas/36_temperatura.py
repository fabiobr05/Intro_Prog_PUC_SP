# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:22:03 2021

@author: Fabio Batista Rodrigues
"""
# Este programa lê um conjunto de temperaturas lidas em determinados locais
# durante os dias da semana, computa e imprime a temperatura média em
# cada um dos locais. As medidas são tomadas diariamente, em 
# determinados horários e em determinados locais. 
# Projete e implemente um programa que leia a temperatura em três locais 
# distintos e quatro vezes ao dia. Utilize uma lista tempMed para armazenar a 
# temperatura média das quatro medidas em um dado local.
# A entrada é dada por uma tabela (matriz)  (4 x 3) de floats, representando as
# temperaturas coletadas na cidade em um dado dia e cada linha da tabela 
# representa as temperaturas dos três locais distintos da cidade onde as medidas
# foram efetuadas. Use uma lista de listas para representar a tabela.


# pré: tempo, local, para i em {0,...,tempo-1} &&
#      para j em {0,...,local-1}: tabelaTemp[i][j] 

tabela = [[0.0]*3 for _ in range(4)]

for i in range(4):
    tabela[i] = list(map(float, input().split()))

tempmed = [0.0] * 3

for j in range(3):
    for i in range(4):
        tempmed[j] += tabela[i][j]
    tempmed[j] = tempmed[j]/4.0
    
for i in range(3):
    print('{0:d} {1:.1f}'.format(i+1, tempmed[i]))

# pós: para j em {0,...,local-1}:tempMed[j] && tempMed[j] == soma
#      j em {0,...,tempo-1}:tabelaTemp[i][j]

"""
Tipos de entrada:

Exemplo 1

#formato da entrada

25.5 28.7 22.2 # matriz das temperaturas

28.8 28.9 24.5

30.4 29.4 26.3

28.5 29.1 25.8

#formato da saída

1 28.3

2 29.0

3 24.7


Exemplo 2

#formato da entrada

15.5 18.7 22.2 # matriz das temperaturas

18.8 18.9 24.5

20.4 19.4 22.3

18.5 19.1 15.8

# formato da saída
1 18.3
2 19.0

3 21.2

"""
