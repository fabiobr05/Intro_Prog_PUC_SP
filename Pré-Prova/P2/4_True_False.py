# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:11:07 2021

@author: Fabio Batista Rodrigues
"""
# Projete e implemente um programa que leia uma lista L de números inteiros e 
# imprima true se o primeiro elemento de L for maior que todos os outros 
# elementos de L, e false caso contrário.
# A entrada é dada por duas linhas. A primeira linha contém um número inteiro 
# tam indicando o tamanho da lista, e a segunda linha contém tam números 
# inteiros (lista). A saída consiste em imprimir true se o primeiro elemento 
# da lista é maior que todos os demais elementos da lista e false caso contrário.

tam = int(input())
lista = list(map(int, input().split()))

primeiro = True
msg = 'true'
i = 1
while i < tam and primeiro:
    if lista[i] >= lista[0]:
        primeiro = False
        msg = 'false'
    i += 1
    
print(msg)