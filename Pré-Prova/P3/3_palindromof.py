# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 12:31:15 2021
Program: palindromof.py
@author: Fabio Batista Rodrigues
"""
# Escreva um programa para ler uma string de no máximo 80 caracteres e então
# determinar se ela é um palíndromo. Caracteres maiúsculos e minúsculos de
# um mesmo símbolo são considerados iguais. A string pode ter caracteres espaço. 

# 
def teste_palindromo(string):
    tam = len(string)
    # Passar todos os caracteres para maiuscula
    # Inicializar variaveis 
    maius =''
    i = 0
    # Se for caractere do alfabeto passar para letra maiuscula
    while tam > i:
        if string[i] >= 'a' and string <= 'z':
            maius += chr(ord(string[i])-32)
        else:
            maius += chr(ord(string[i]))
        i += 1
    # Analisar se é palindromo ou nao
    # Inicializar variaveis
    cont = 0
    j = tam
    # Enquanto j for igual a zero, repita o processo
    while j > 0:
    # Varrer a string comparando a primeira string com a ultima, a segunda
    # com a penultima e assim por diante 
        for i in range(0, tam):
            j -= 1
    # Comparar e acrescentar na variavel cont
            if maius[i] == maius[j]:
                cont += 1
    
    # Imprimir saída correspondente 
    if cont == tam:
        msg = 'palíndromo'
    else:
        msg = 'não palíndromo'
    
    return msg

# Programa principal
# Leia a string
entrada = input()
# Recrute a funçao teste_palindromo
saida = teste_palindromo(entrada)

print(saida)

