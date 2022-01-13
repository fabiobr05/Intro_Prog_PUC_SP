# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:26:41 2021

@author: Fabio Batista Rodrigues
"""
#Dado uma frase com no mínimo 3 caracteres e no máximo 40 caracteres 
#(caracteres visíveis e sem o caractere espaço) e uma string com 3 caracteres 
# (visíveis e sem o caractere espaço), projete e implemente um programa que 
# verifique se a string ocorre na frase. Caracteres maiúsculos e minúsculos da 
# mesma letra são considerados diferentes.
# A entrada é dada por duas linhas, a primeira linha contém a frase e a 
# segunda linha contém a string que será procurada no texto. Esse programa não 
# pode utilizar funções ou métodos pré-existentes em bibliotecas ou módulos que 
# computem diretamente a solução do problema. Sua solução só pode utilizar 
# instruções para analisar caracteres individualmente. A saída consiste em 
# imprimir o 'sim' se a string ocorre na frase, e 'não' caso contrário.

texto = input()
palavra = input()

tam = len(texto)
"""
msg = ''
for i in range(0,tam-1):
    if texto[i] == palavra[0] and texto[i+1] == palavra[1] and texto[i+2] == palavra[2]:
        msg = 'sim'

print(msg)
"""
i = 0 # indice do texto
j = 0 # indice da palavra

while i < tam and j < 3:
    if texto[i] == palavra[j]:
        i += 1
        j += 1
    else:
        i = i - j + 1
        j = 0
if j ==3:
    msg = 'sim'
else:
    msg = 'nao'
    
print(msg)