# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:19:20 2021

@author: Fabio Batista Rodrigues 
"""
# Projete e implemente um programa que leia uma lista L de tam números inteiros
# e retire todos os elementos duplicados da lista. A entrada é dada por duas
# linhas. A primeira linha contém um número inteiro tam indicando o tamanho
# da lista. A segunda linha contém uma lista de tam números inteiros. A saída 
# consiste em imprimir a lista de inteiros da entrada sem repetição.
"""
tam = int(input())
lista = list(map(int, input().split()))[:tam]
j = 0
for i in range(0, tam-1):
    a = lista[i]
    while i != j:
        for j in range(0, tam - 1):
                if a == lista[j]:
                    del(lista[j])
        j = 0
print(lista)
"""
tam = int(input())

lista= list(map(int, input().split()))[:tam]

novalista = []

for num in lista:
    if num not in novalista:
        novalista.append(num)

print(novalista)