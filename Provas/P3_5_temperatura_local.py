# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:55:49 2021
Program: temperatura_local.py
@author: Fabio Batista Rodrigues
"""
# projete e implemente um programa que leia as 3 temperaturas nos respectivos
# locais, 4 vezes ao dia (seis horas, meio dia, dezoito horas e meia noite),
# calcule a temperatura média em cada um dos horários em que temperatura foi 
# registrada, e imprima os resultados. Utilize um arranjo unidimensional tempMed
# para armazenar a temperatura média em cada uma das vezes que ela foi coletada.
# Os valores das temperaturas são medidos com pelo menos uma casa decimal.

# Passo 1.0. Estruturas para armazenar a tabela e as médias
tabtemp = [[0.0]*3 for i in range(4)]
media = [0.0]*4
# Passo 1.1 Leia as temperaturas
for i in range(4):
    tabtemp[i] = list(map(float, input().split()))
# Passo 2.0 Faça a soma e media
for i in range(4):
    for j in range(3):
        media[i] = media[i] + tabtemp[i][j]
    media[i] = media[i]/3
# Passo 3.0 Imprima a saida correspondente
saida = [round(item,1) for item in media]
print(saida)