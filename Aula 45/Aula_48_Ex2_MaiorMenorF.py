# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:26:35 2021
Program: maiormenorf
@author: Fabio Batista Rodrigues
"""
# Este programa lê um conjunto de números, calcula o maior, o
# menor número e a variação entre eles e imprime o resultado. 
# O programa usa a função maiormenor para computar o maior, 
# o menor número da lista.

# Esta função recebe uma lista (tamanho e elementos) e computa
# os índices dos elementos máximo e mínimo da lista
def maiormenor(n, lista):
    
# Passo eM.1. Compute o máximo e o índice onde ocorre o máximo
    maximo = lista[0]
    indmax = 0
    minimo = lista[0]
    indmin = 0
    for i in range(1,n):
        if lista[i] > maximo:
            maximo = lista[i]
            indmax = i
        if lista[i] < minimo:
            minimo = lista[i]
            indmin = i
# Passo eM.2. Compute o mínimo e o índice onde ocorre o mínimo

    return indmax, indmin

# pré: tam lista[0] lista[1] .. lista[tam-1]

# Passo 1. Leia a lista
# Passo 1.1. Leia o tamanho da lista
tam = int(input())
# Passo 1.2. Leia os elementos da lista
lista = list(map(int,input().split()))
# Passo 2. Compute o maior e o menor elemento da lista
indmax, indmin = maiormenor(tam,lista)
maximo = lista[indmax]
minimo = lista[indmin]
# Passo 3. Compute a variação
variacao = maximo - minimo
# Passo 4. Imprima os resultados
print('[{0:d},{1:d}] [{2:d},{3:d}] {4:d}'.format(indmax, maximo, indmin, minimo, variacao))

# pós: maximo && maximo == max i em {0,...,tam-1}: lista[i]
#      minimo && minimo == min i em {0,...,tam-1}: lista[i]
# fim



