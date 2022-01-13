# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 19:35:43 2021

@author:  Fabio Batista Rodrigues
"""
# Escreva um programa que leia uma lista L de 2 <= tam <= 100 números inteiros
# e verifique se os elementos da lista estão em ordem decrescente. O programa
# deverá imprimir verdadeiro se os elementos da lista estiverem em ordem
# decrescente ou falso caso contrário. Note que o seguinte predicado pode ser
# usado para descrever esta propriedade de L, caso os elementos de L estiverem
# em ordem decrescente:
# para todo i em {0,...,tam-2}: L[i] > L[i+1]

# Passo 1. Inserir os numeros e armazenar em uma lista
entrada = list(map(int, input().split()))
tam = len(entrada)

# Passo 2. Avaliar se é ou nao decrescente
i = 0
decrescente = False
msg = 'falso'
while i < tam-1 and decrescente:
    if entrada[i] > entrada[i+1]:
        decrescente = True
        msg = 'verdadeiro'
    i += 1
# Passo3. Imprimir mensagem correspondente
print(msg)


"""
# NAO ESTA TOTALMENTE CERTO
# Passo 2. Analisar variaveis
j = 0
for i in range(0,tam-2):
    
    if entrada[i] >= entrada[i+1]:
        j += 1

# Passo 3. Atribuir a mensagem correspondente ao resultado
if tam-2 == j:
    msg = 'verdadeiro'
else:
    msg = 'falso'
# Imprimir a mensagem
print(msg)

"""