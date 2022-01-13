# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:31:31 2021

@author: Fabio Batista Rodrigues
"""
# Escreva um programa que leia uma lista L de 2 <= tam <= 100 números 
# inteiros e verifique se os elementos da lista estão em ordem decrescente. 
# O programa deverá imprimir verdadeiro se os elementos da lista estiverem em 
# ordem decrescente ou falso caso contrário. Note que o seguinte predicado pode 
# ser usado para descrever esta propriedade de L, caso os elementos de L 
# estiverem em ordem decrescente:
# para todo i em {1,...,tam-1}: L[i] > L[i+1]
# A entrada é dada por duas linhas. A primeira linha contém um número inteiro 
# tam indicando o tamanho da lista, e a segunda linha contém uma lista de tam 
# números inteiros. A saída consiste em imprimir verdadeiro se a lista está em 
# ordem decrescente e falso caso contrário.

tam = int(input())
lista = list(map(int,input().split()))

decrescente = True
msg = 'verdadeiro'
i = 0
while i < tam-1 and decrescente:
    if lista[i+1] >= lista[i]:
        decrescente = False
        msg = 'falso'
    i += 1
print(msg)

