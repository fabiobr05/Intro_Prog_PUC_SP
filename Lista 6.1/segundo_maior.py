# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 18:06:27 2021

@author: Fabio Batista Rodrigues
"""

# Escreva um programa para encontrar o segundo maior valor em uma lista com 
# tam números inteiros numeros. A entrada é dada por duas linhas, sendo que a 
# primeira linha contém um número inteiro tam indicando o tamanho da lista, e
# a segunda linha contém tam números inteiros representando a lista. A saída
# consiste em imprimir o segundo maior valor referente a lista de entrada. 
# Sugestão: Use uma lista auxiliar, compute o maior e retire da lista. Use 
# a lista auxiliar sem o maior para computar o segundo maior.

# PS: Acabei nao usando
tam = int(input())

lista = list(map(int, input().split()))



# Modo C de se fazer
# 1º ordenar lista
for i in range (0, tam-1):
    pos = i
    menor = lista[i]
    for j in range(i+1,tam):
        if lista[j] < menor:
            menor = lista[j]
            pos = j
    lista[pos] = lista[i]
    lista[i] = menor
# Lista ordenada
# 2º Achar o indereço do maior
j = 0
for i in range(0,tam-1):
    
    if lista[i] <= lista[i+1]:
        j = i
# Condiçao para caso a lista seja apenas de um elemento
i = 0
if j > 0:
    print(lista[j])
else:
    print(lista[i])

"""
# MANEIRA DO PROFESSOR
lista1 = lista.copy()

maior1 = max(lista1)
lista1.remove(maior1)
maior2 = max(lista1)

print(maior2)
"""

"""
# Modo rapido ---------------------------------
maximo = max(num)
posicaoM = num.index(maximo)
num.pop(posicaoM)

seg_maximo = max(num)

print(seg_maximo)
# -----------------------------------------------
"""
