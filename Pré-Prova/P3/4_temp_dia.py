# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 12:48:14 2021
Program: 
@author: Fabio Batista Rodrigues
"""
# Projete e implemente um programa que leia a temperatura em três locais
# distintos, quatro vezes ao dia. Utilize uma lista de listas para armazenar
# a temperatura média das quatro medidas em um dado local. A entrada é dada
# por uma tabela com 4 linhas e 3 colunas com números do tipo float,
# representando as temperaturas coletadas. A lista de listas representa 
# as temperaturas coletadas na cidade em um dado dia e cada linha da tabela
# representa as temperaturas dos três locais distintos da cidade onde as 
# medidas foram efetuadas. A saída é dada por três linhas, cada uma contendo
# o local e a temperatura média computada. A impressão deve usar o formato
# abaixo, onde tempMed é a lista das temperaturas médias em cada um dos locais:

# Funçao que transforma as temperaturas medias
def temp_Med(a):
    temp_Med = [0.0]*3
    j = 0
    for i in range(3):
        for a in range(4):
            temp_Med[j] = temp_Med[j] + temp[a][i]
        j +=1
    for i in range(3):
        temp_Med[i] = temp_Med[i]/4
    return temp_Med
# Programa principal
# Inicializar lista
temp = [[0.0]*3 for _ in range(4)]
# Ler temperturas 4 vezes
for i in range(4):
    temp[i] = list(map(float, input().split()))
# Recrutar função que transforma as temperturas em medias
tempMed = temp_Med(temp)
# Imprimir saida adequada
for local in range(3):
    print('{0:d} {1:5.1f}'.format(local+1,tempMed[local]))
