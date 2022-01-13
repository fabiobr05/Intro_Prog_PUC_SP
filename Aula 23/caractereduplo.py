# -*- coding: utf-8 -*-
# Programa: caractereduplo.py
# Programador:
# Data: 26/04/2012
# O Diálogo:  Escreva um programa que conte todas as ocorrências de dois 
# caracteres consecutivos em um dada parágrafo de um texto lido de um arquivo. 
# Um parágrafo é um conjunto de frases num dado idioma e que é finalizado 
# por um ponto (.) e um '\n' (podem ocorrer .´s sem que isso signifique o 
# final do parágrafo, tais como 1.8 Mhz, reticências e final de frases no
# parágrafo). Nos idiomas utilizadas não existem conjuntos de caracteres  
# (palavras) com a ocorrência de três caracteres consecutivos iguais e nas
# frases não existem dois caracteres brancos consecutivos.
# Declaração das bibliotecas utilizadas
import sys

# início

# pré: texto[0] ... texto[n-1]

# Passo 1. Leia o texto e inicialize as variáveis
# Passo 1.1. Leia o texto
print('Leia o Texto')
texto = sys.stdin.read()
# Passo 1.2. Inicialize o número de caracteres duplos
numero = 0 
anterior = ''
# Passo 2. Conte os caracteres duplos do texto
for letra in texto:
    if letra == anterior:
        numero += 1
    anterior = letra
# Passo 3. Imprima o número de caracteres duplos na frase.
print('{0:d}'.format(numero))

# pós: numero == sum i em {1,...,n-1}: texto[i] == texto[i+1]

# fim
