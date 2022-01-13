# -*- coding: utf-8 -*-
"""
Created on Mon May 31 16:29:41 2021

@author: Fabio Batista Rodrigues
"""
# Escreva um programa para localizar e retornar as posições do maior e do menor
# inteiro em uma lista com no máximo 1000 inteiros representada pelo vetor de 
# inteiros. Caso haja mais de um máximo ou mínimo na lista, a função deve 
# retornar o menor índice do máximo ou do mínimo na lista. O seu programa deve 
# também computar a variação entre números, isto é a diferença entre o máximo 
# e o mínimo valor da lista.

# PRIMEIRA MANEIRA
# ENTRADA DE DADOS: Leia os numeros em forma de lista
tam = int(input())
valores = list(map(int, input().split()))[:tam]

# Processamento

for i in range(0,tam-1):
    
    if valores[i] > valores[i+1]:
        aux = i
        temp = valores[i]



print(valores[i], temp)

"""
SEGUNDA MANEIRA

# ENTRADA DE DADOS: Leia os numeros em forma de lista
tam = int(input())
valores = list(map(int, input().split()))[:tam]

# Processamento
maximo = max(valores)
posicao_max = valores.index(maximo) 
minimo = min(valores)
posicao_min = valores.index(minimo)

variacao = maximo - minimo

# SAIDA DE DADOS
print(posicao_max, maximo, posicao_min, minimo, variacao)

"""