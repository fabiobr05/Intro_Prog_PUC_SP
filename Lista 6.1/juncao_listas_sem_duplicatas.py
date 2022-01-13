# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:17:24 2021

@author: fabio
"""


tam1 = int(input())
lista1 = list(map(int, input().split()))[:tam1]

tam2 = int(input())
lista2 = list(map(int, input().split()))[:tam2]

tam = tam1 + tam2

nlista = []*tam
#Receber da primeira lista
for i in range(0,tam1):
    nlista.append(lista1[i])

#Receber da segunda lista
for i in range(0, tam2):
    nlista.append(lista2[i])

# Retirar as duplicatas
novalista = []

for num in nlista:
    if num not in novalista:
        novalista.append(num)

# Imprimir o correspondente
print(novalista)

"""
# Jeito do professor de fazer o exercicio:
    
tam1 = int(input())
cg = list(map(int, input().split()))

tam2 = int(input())
pp = list(map(int, input().split()))

cgpp = cg.copy()
for produto in pp:
    if produto not in cg:
        cgpp.append(produto)
        
print(cgpp)

"""