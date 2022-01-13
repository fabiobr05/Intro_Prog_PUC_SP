# -*- coding: utf-8 -*-
"""
Created on Wed May 26 19:35:13 2021

@author: fabio
"""
# Escreva um programa que leia uma lista L de 2 <= tam <= 100 números inteiros e
# verifique se os elementos da lista estão em ordem crescente. O programa deverá
# imprimir verdadeiro se os elementos da lista estiverem em ordem crescente ou 
# falso caso contrário. Note que o seguinte predicado pode ser usado para 
# descrever esta propriedade de L, caso os elementos de L estiverem em ordem
# crescente:

tam = int(input())

lista = list(map(int, input().split()))

crescente = True
msg = 'verdadeiro'
for i in range(0,tam-1): # [0,tam-1]
    if lista[i] >= lista[i+1]:
        crescente = False
        msg = 'falso'
        
# Ou podemos fazer desse jeito:

#i = 0 
#while i < tam-1 and crescente:
#    if lista[i] >= lista[i+1]:
#        crescente = False
#        msg = 'falso'
#    i += 1

print(msg)