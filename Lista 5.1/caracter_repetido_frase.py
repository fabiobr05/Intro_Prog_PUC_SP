# -*- coding: utf-8 -*-
"""
Created on Mon May 31 15:58:50 2021

@author: Fabio  Batista Rodrigues
"""
# Escreva um programa que conte todas as ocorrências de duas letras seguidas 
# em uma dada frase de um texto lido de um arquivo. Uma frase é um conjunto de 
# no máximo 255 caracteres num dado idioma e que é finalizado por um ponto (.)

# ENTRADA DE DADOS: Ler frase
frase = input()
# ----------------------------------------------------------
# PROCESSAMENTO
i = 0
# Laço para avaliar ate aparecer o caracter '.' no final
while frase[i] != '.':
# Declarando variaveis 
    numero = 0
    anterior = ''
# Laço para verificar se há letras repetidas
    for letra in frase:
# Avaliando se há letras repetidas
        if letra == anterior:
            numero += 1
        anterior = letra
# Encrementar variavel i
    i += 1
# -----------------------------------------------------------
# SAÍDA DE DADOS: Imprimir o numero de vezes que se repeti letras
# consecutivas no texto
print('O numero de vezes que aparece letras repetidas é: {0:d}'.format(numero))
        