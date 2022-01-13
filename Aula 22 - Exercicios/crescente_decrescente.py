# -*- coding: utf-8 -*-
"""
Spyder Editor
Pragrammer: Fabio Batista Rodrigues

"""

# Escreva um programa que leia uma lista L de 2 <= tam <= 100 números inteiros
# e verifique se os elementos da lista estão em ordem não decrescente. 
# O programa deverá imprimir verdadeiro se os elementos da lista estiverem em 
# ordem não decrescente ou falso caso contrário. Note que o seguinte predicado 
# pode ser usado para descrever esta propriedade de L, caso os elementos de L 
# estiverem em ordem não decrescente:
# para todo i em {1,...,tam-1}: L[i] <= L[i+1]

# 1.0 Insira a entrada sendo o tamanho da lista
tam = int(input())
# 1.1 Insira a lista com elementos = tam
lista = list(map(int, input().split()))[:tam]

# 2.0 Compare os numeros da lista
j = 1
for i in range(0, tam - 2):
    a = lista[i]
    b = lista[i + 1]
    if a <= b:
        j += 1
# 2.1 Atribua a mensagem correta
if tam == j:
    msg = 'verdadeiro'
else:
    msg = 'falso'

# 3.0 Imprima a mensagem
print(msg)

