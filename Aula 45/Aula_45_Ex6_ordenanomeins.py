# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:38:32 2021
Programa: ordenanomeinsf.py
@author: Fabio Batista Rodrigues
"""
# Este programa lê uma lista de nomes, ordena os nomes em ordem
# não decrescente usando uma função e imprime os nomes ordenados.
# Esta função recebe um lista de elementos lista[0]...lista[n-1]
# e ordena a lista em ordem não decrescente usando o algoritmo
# da ordenação por inserção. Na ordenação por inserção a lista é
# dividida em duas partes, uma ordenada e outra para ser ordenada.
# A cada passo, o primeiro elemento da lista a ser ordenada é
# inserido na sua posição correta na lista ordenada.
def ordenains(n, lista):

    for i in range(1,n):
        temp = lista[i]
        j = i-1
        while j >= 0 and lista[j] > temp:
            lista[j+1] = lista[j]
            j -= 1
            lista[j+1] = temp
        return lista

# início do módulo principal
# descrição das variáveis locais
# list lista[] - lista de nomes a serem ordenados
# int  tam     - tamanho da lista

# pré: tam para i em {0,..,tam-1}:lista[i]

# Passo 1. Leia a lista
tam = int (input())
lista = ['']*tam
for i in range(tam):
    lista[i] = str(input())
# Passo 2. Ordene a lista
ordenains(tam,lista)

# Passo 3. Imprima a lista de nomes ordenada
for i in range(tam):
   print(lista[i])

# pós: para i em {0,.., tam-2}:lista[i] <= lista[i+1]
# fim do módulo principal

