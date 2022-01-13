# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 11:59:13 2021
Program: Somamatriz.py
@author: Fabio Batista Rodrigues
"""
# Projete e implemente um programa para ler dois vetores a e b,
# representados por duas listas, calcular a soma c = a + b das 
# duas listas e imprimir o resultado c.

# Leia o vetor A
A = list(map(int, input().split()))
# Leia o vetor B
B = list(map(int, input().split()))
# Compute o tamanho de um dos vetores
tam = len(A)
# Faça a operaçao
C = [0]*tam
for i in range(tam):
    C[i] = A[i] + B[i]
# Imprima a saída correspondente
print(C)
    

