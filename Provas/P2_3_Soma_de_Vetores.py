# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 20:10:13 2021

@author: Fabio Batista Rodrigues
"""
# Projete e implemente um programa para ler dois vetores a e b, representado
# por duas listas, calcular a soma c = a + b das duas listas e imprimir
# o resultado c. A entrada é dada por duas linhas, cada uma delas com tam
# elementos, representado os vetores a e b, respectivamente. A saída consiste
# em imprimir a lista resultante da soma das duas listas que representam os
# dois vetores. Neste programa não pode ser utilizada nenhuma função ao método
# que some diretamente duas listas.

# Entrada. Inserir os dois vetores
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Avaliar o tamanho das duas listas
tam = len(a)
# Inicializar as variaveis
c = []
i = 0
numero = 0
# Somar e acrescentar a lista c
while i <= tam-1:
    numero = a[i] + b[i]
    c.append(numero)
    i += 1
# Imprimri a lista c
print(c)
    
