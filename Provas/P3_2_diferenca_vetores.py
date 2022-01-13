# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:13:26 2021
Program: diferenca_vetores.py
@author: Fabio Batista Rodrigues
"""
# Projete e implemente um programa para ler dois vetores a e b, 
# representados por duas listas, calcular a diferença c = a - b 
# das duas listas e imprimir o resultado c.

# Passo 1.0 Leia o tamanho dos vetores
tam = int(input())
# Passo 1.1 Leia o vetor a
a = list(map(int, input().split()))
# Passo 1.2 Leia o vetor b
b = list(map(int, input().split()))
# Passo2.0 Compute a diferença dos dois
c = [0]*tam
for i in range(0, tam):
    c[i] = a[i] - b[i]
# Passo 3.0 Imprima o vetor diferença
print(c)