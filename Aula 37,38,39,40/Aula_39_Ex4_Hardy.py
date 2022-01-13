# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 14:18:31 2021
Program: Hardy.py
@author: Fabio Batista Rodrigues
"""
# O famoso matemático G. H. Hardy uma vez mencionou ao jovem e brilhante 
# matemático Indiano Srinivasa Ramanujan que o número do táxi que ele havia 
# chegado era um número sem nenhuma característica especial. Ramanujan 
# imediatamente respondeu que não, pois o número era muito interessante visto
# que ele era o menor número inteiro que podia ser escrito como a soma de dois
# cubos (isto é, escrito da forma x3 + y3, com x e y inteiros) em duas formas 
# diferentes. Escreva um programa para encontrar o número do táxi em que Hardy 
# viajou.
# Este programa que gera o conjunto de pares de cubos i*i*i + j*j*j menores
# 10000 e encontra o menor valor que pode ser escrito como a soma de dois
# cubos. O programa usa uma matriz triangular inferior para armazenar os 
# cubos.

def ramanujan(n):
    results = []
    for a in range(1, n+1):
        a3 = pow(a, 3)
        if a3 > n:
            break
        for b in range(a, n+1):
            b3 = pow(b, 3)
            if b3 > n:
                break
            for c in range(a+1, n+1):
                c3 = pow(c, 3)
                if c3 > n:
                    break
                for d in range(c, n+1):
                    d3 = pow(d, 3)
                    if d3 > n:
                        break
                    elif a3 + b3 == c3 + d3:
                        start = c3 + d3
                        new = "{} = {}^3 + {}^3 = {}^3 + {}^3".format(start, a, b, c, d)
                        results.append(new)
                        break
                    else:
                        continue
    return results

fabio = int(input())
ramanujan(fabio)

