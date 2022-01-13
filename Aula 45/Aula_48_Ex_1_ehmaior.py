# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:13:41 2021
Program: ehmaiorf.py
@author: Fabio Batista Rodrigues
"""
# Este programa lê um conjunto de números, verifica se o primeiro elemento
# é o maior elemento da lista e imprime sim/não. O programa usa uma função
# ehMaior para verificar se o primeior elemento é o maior da lista

def ehMaior(lista, n):
    resp = True
    i = 1
    while i < n:
        if lista[0] <= lista[i]:
            resp = False
            i = n
        i += 1
    

    return resp
 
# pré: tam lista[0] lista[1] .. lista[tam-1]

tam = int(input())
lista = list(map(int, input().split()))

res = ehMaior(lista,tam)

if res:
    msg = 'sim'
else:
    msg = 'não'
print(msg)
# pós: ('sim' && lista[0] == max i em {0,...,tam-1}: lista[i] &&
#       lista[0] > lista[j], j em {1,2,...,tam-1}) || 'não'
# fim

