# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 12:15:41 2021
Program: Intersec_listas.py
@author: Fabio Batista Rodrigues
"""
# Projete e implemente um programa para computar a interseção das duas listas
# das matrículas dos alunos nessas disciplinas.
 
# Leia o tamanho da primeira lista
tam1 = int(input())
# Leia a primeira lista
list1 = list(map(int, input().split()))
# Leia o tamanho da segunda lista
tam2 = int(input())
# Leia a segunda lista
list2 = list(map(int, input().split()))
tam2 = int
# Inicialize a lista
lista = []
# Compute a intersecçao
for i in list1:
    if i in list2:
        lista.append(i)
# Imprima a saída adequada
print(lista)
    
