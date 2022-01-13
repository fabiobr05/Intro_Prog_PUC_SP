# -*- coding: utf-8 -*-
"""
Created on Thu May 27 20:44:10 2021

@author: fabio
"""
# Projete e implemente um programa que leia uma string com no máximo 80 
# caracteres, inverta a string colocando o último caractere como o primeiro o 
# penúltimo como segundo, e assim sucessivamente, e imprima a string invertida.
# Neste exercício não pode ser usado a facilidade de inverter uma string 
# diretamente string[::-1]. O exercício deve manipular os caracteres 
# individualmente. A entrada é dada por uma strings qualquer (a string pode 
# conter espaços). A saída representa a string de entrada invertida.

# Receber string, armzenar e computar seu tamanho
entrada = input()
tam = len(entrada)

nome = ''
for i in range(tam, 0, -1):
# Receber a ultima letra do da entrada
    nome = nome + entrada[i-1]
    
# Imprima o nome correspondente
print(nome)
    
    



"""
i = 0
invert = ''
while tam > i:
    invert += entrada[tam]
    tam -= 1

"""