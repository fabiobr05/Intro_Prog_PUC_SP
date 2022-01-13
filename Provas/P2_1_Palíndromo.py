# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 18:58:51 2021

@author: Fabio Batista Rodrigues
"""
# Escreva um programa para ler uma string de no máximo 80 caracteres e então
# determinar se ela é um palíndromo. Caracteres maiúsculos e minúsculos de um
# mesmo símbolo são considerados iguais. A string pode ter caracteres espaço.
# Neste exercício não pode ser usado nenhuma função ou módulo para manipular
# blocos da string. Só pode ser utilizado a manipulação e concatenação de
# 'caracteres' e comparação de strings.

# Passo1. Ler String
string = input()
# Passo1.1. Computar o tamanho da sttring
tam = len(string)
# Passo 2. Passar todos os caracteres para maiuscula
# Passo 2.1. Inicializar variaveis 
maius =''
i = 0
# Passo2.2. Se for caractere do alfabeto passar para letra maiuscula
while tam > i:
    if string[i] >= 'a' and string <= 'z':
        maius += chr(ord(string[i])-32)
    else:
        maius += chr(ord(string[i]))
    i += 1
# Passo3. Analisar se é palindromo ou nao
# Passo3.1 Inicializar variaveis
cont = 0
j = tam
# Passo3.2. Enquanto j for igual a zero, repita o processo
while j > 0:
# Passo3.1 Varrer a string comparando a primeira string com a ultima, a segunda
# com a penultima e assim por diante 
    for i in range(0, tam):
        j -= 1
# Passo3.3 Comparar e acrescentar na variavel cont
        if maius[i] == maius[j]:
            cont += 1

# Imprimir saída correspondente 
if cont == tam:
    print('palíndromo')
else:
    print('não palíndromo')


