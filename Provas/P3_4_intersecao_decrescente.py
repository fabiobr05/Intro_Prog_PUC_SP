# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:34:49 2021
Program: Intercecao_decrescente.py
@author: Fabio Batista Rodrigues
"""
# Projete e implemente um programa que, usando listas, leia dois conjuntos
# A e B, onde A é um conjunto de tamA > 0 números inteiros distintos, 
# ordenados em ordem decrescente e B é um conjunto de tamB > 0 números inteiros
# distintos, ordenados em ordem decrescente e compute um conjunto C de números
# inteiros distintos, ordenado em ordem não crescente, obtido com a intercalação
# dos conjuntos A e B. Observe que os conjuntos A e B contêm números inteiros 
# distintos, mas pode haver números que estão em A e que também podem pertencer 
# a B e nesse caso esses possíveis números que aparecem simultaneamente em A e B
# devem aparecer duas vezes em C.

# Passo 1.0 Leia o tamanho da lista1
tam1 = int(input())
# Passo 1.1 Leia a primeira lista
lista1 = list(map(int, input().split()))
# Passo 1.2 Leia o tamanho da lista2
tam2 = int(input())
# Passo 1.3 Leia a segunda lista
lista2 = list(map(int, input().split()))
tam = tam1 + tam2
lista = []*tam 
# Passo 2.0 Fazer a junçao das listas
for i in range(0, tam1):
   lista.append(lista1[i])
for i in range(0, tam2):
    lista.append(lista2[i])
# Passo 2.1 Ordenar a lista pelo maior
for i in range(0,tam):
    maior = max(lista[i:tam])
    maiordepois = lista[i:tam].index(maior)
    lista[i+maiordepois]=lista[i]
    lista[i]=maior
# Passo 3.0 Imprimir a lista em ordem decrescente
print(lista)