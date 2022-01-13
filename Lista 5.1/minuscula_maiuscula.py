# -*- coding: utf-8 -*-
"""
Created on Thu May 27 19:11:02 2021

@author: fabio
"""
# Projete e implemente um programa que leia uma string str com no máximo 20 
# caracteres, todos do alfabeto e minúsculos. O programa deve transformar todos 
# os caracteres da string str para caracteres maiúsculos e imprimir a string só 
# com caracteres maiúsculos. O programa não pode utilizar o método str.upper(). 
# A entrada é dada por uma string str só de caracteres minúsculos. A saída por 
# uma string só de caracteres maiúsculos.

# Receber string de entrada e armazenar numa lista
entrada = input()
tam = len(entrada)
# Trocar cada letra para maiuscula
maiuscula =''
i = 0
while tam > i:
    if entrada[i] >= 'a' and entrada <= 'z':
        maiuscula += chr(ord(entrada[i])-32)
    else:
        maiuscula += chr(ord(entrada[i]))
    i += 1

print(maiuscula)