# -*- coding: utf-8 -*-
"""
Created on Fri May 21 17:40:18 2021

@author: Fabio Batista Rodrigues
"""
# Este programa lê dois vetores a e b de inteiros, do mesmo
# tamanho, computa a intercalação de a e b e imprime o
# resultado 
# Intercalação de vetores de mesmo tamanho.
# a == [1, 3, 5, 7, 9]
# b == [4, 2, 8, 6, 10]
# a intercalado com b
# c = [a[0],b[0],a[1],b[1],a[2],b[2],a[3],b[3],a[4],b[4]]
# nesse caso específico, os dois vetores tem o mesmo tamanho
# c = [1,4,3,2,5,8,7,6,9,10]
# início do módulo principal
# descrição das variáveis utilizadas
# list a, b, c
# int tam

# pré: tam a[0]..a[tam-1] b[0]..b[tam-1]

# Passo 1. Leia os vetores
# Passo 1.1. Leia o tamanho dos vetores
tam = int(input())
# Passo 1.2. Leia o vetor a
a = list(map(int, input().split()))[:tam]
# Passo 1.3. Leia o vetor b
b = list(map(int, input().split()))[:tam]
# Passo 2. Intercale os vetores
c = []
for i in range(0, tam):
    c.append(a[i])
    c.append(b[i])
# Passo 3. Imprima os vetores intercalados
print(c)

# pós: c == [a[0], b[0],..,a[tam-1], b[tam-1]
# fim do módulo principal
