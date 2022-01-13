# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:22:31 2021
Program:produto_interno.py 
@author: Fabio Batista Rodrigues
"""
# Projete e implemente um programa para ler dois vetores a e b, representados 
# por duas listas, calcular o produto interno c⃗ =a⃗ ⋅b⃗  das duas
# listas e imprimir o resultado c.

# Passo 1.0 Leia os dois vetores
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# Passo 1.1 Compute o tamnho de um deles
tam = len(a)
c = [0]* tam
# Passo 2.0 Faça o produto interno
for i in range(0, tam):
    c[i] = a[i] * b[i]
a = 0.00
for i in range(0, tam):
    a = a + c[i]
# Passo 3.0 Imprima o produto interno dos dois vetores
print('{0:.2f}'.format(a))