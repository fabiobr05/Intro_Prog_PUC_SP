# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:19:20 2021

@author: Fabio Batista Rodrigues 
"""
# Projete e implemente um programa que usando o método da seleção do menor 
# elemento, leia uma lista de números inteiros de tamanho tam, ordene a lista e 
# imprima o resultado .A entrada é dada por duas linha,s onde a primeira linha 
# contém um número inteiro tam indicando o tamanho da lista, e a segunda linha 
# contém uma lista de tam números inteiros representando a lista. A saída 
# consiste em imprimir a lista de entrada ordenada.

# Maneira python de se fazer
tam = int(input())

lista = list(map(int, input().split()))

for i in range(0,tam):
# Receber o menor elemento da lista e armazenar em 'menor'
    menor = min(lista[i:tam])
# Receber a localidade do menor e armazenar em 'menorpos'
    menorpos = lista[i:tam].index(menor)
# Pegar o elemento que esta em i e passar para o a localidade i + menorpos
    lista[i+menorpos]=lista[i]
# Agora colocar o menor no lugar de quem estava em i
    lista[i]=menor
# -------- Processo sera repetido de 0 à tam-----------------
# desenpacotar a lista coloca o '*'
print(*lista)

"""
# Maneira C ou java de se fazer

for i in range (0, tam-1):
    pos = i
    menor = lista[i]
    for j in range(i+1,tam):
        if lista[j] < menor:
            menor = lista[j]
            pos = j
    lista[pos] = lista[i]
    lista[i] = menor
    
for i in range(0, tam):
    print('{0:d}'.format(lista[i]),end=' ')
    
"""
