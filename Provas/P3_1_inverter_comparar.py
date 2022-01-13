# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 18:25:54 2021
Program: inverter_comparar.py
@author: Fabio Batista Rodrigues
"""
# Projete e implemente um programa que leia uma string com no máximo 80 
# caracteres, inverta a string colocando o último caractere como o primeiro 
# o penúltimo como segundo, e assim sucessivamente, e imprima a string invertida.
# Compare a string original com a string invertida e conte o número de 
# caracteres que são diferentes. Neste exercício não pode ser usado a facilidade
# de inverter uma string diretamente string[::-1]. O exercício deve manipular
# os caracteres individualmente. A entrada é dada por uma string qualquer 
# (a string pode conter espaços). A saída consiste em imprimir o número de 
# caracteres que diferem na comparação das duas strings.

# Passo 1. Ler string
string = input()
# Computar tamanho da string
tam = len(string)

# Passo 2. Inverter string e armazenar em outra
string_invertida = ''
for i in range(tam-1, -1, -1):
    string_invertida = string_invertida + string[i]
# Passo 2.1 Comparar string com string invertida
j = 0
for i in range(0, tam):
    if string[i] != string_invertida[i]:
        j +=1
# Passo 3. Imprima a saida com o numero de caracteres diferentes
print(j)
