# -*- coding: utf-8 -*-
# Programa: quadruplas.py
# Programador: Fabio Batista Rodrigues
# Data: 28/04/2021
# Este programa recebe duas quadruplas de numeros inteiros
# e imprimi para cada para de quadruplas de numeros 
# lidos os valores representados na soma de dias, horas, minutos
# e segundos.
#inicio do modulo principal
# int dia1, hr1, min1, seg1
# int dia2, hr2, min2, seg2

# Passo 1. Leia a primeira quadrupla
dia1, hr1, min1, seg1 = map(int, input().split())
#Passo 1.2. Leia a segunda quadrupla
dia2, hr2, min2, seg2 = map(int, input().split())
#Passo 2. Calcule a soma
#Passo 2.1 Calcule a soma dos segundos
totalSeg = seg1 + seg2
seg = totalSeg % 60
#Passo 2.1 Calcule a soma dos minutos
totalMin = min1 + min2 + totalSeg // 60
minu = totalMin % 60
#Passo 2.3 Calcule a soma das horas
totalHoras = hr1 + hr2 + totalMin // 60
hr = totalHoras % 24
#Passo 2.4 Calcule a soma dos dias
dias = dia1 + dia2 + totalHoras // 24
dias = dias % 24
# Passo 3 Imprima a soma
print('{0:d} {1:d} {2:d} {3:d}'.format(dias, hr, minu, seg))  

