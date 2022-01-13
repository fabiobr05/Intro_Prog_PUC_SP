# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:59:26 2021
Program: CampoMinado.py
@author: fabio
"""
# Este programa lê um mini campo-minado composto de uma matriz, 4x4, 
# onde o número (0) indica espaços livres e o número (1) indica que 
# há uma bomba no local. O programa lê um número inteiro m de (pontos)
# tentativas, dados por linhas e colunas no campo-minado. O programa
# verifica se o ponto é uma bomba ou não. Caso seja, imprimir 1, senão 0.

campo = [[0] * 4 for _ in range(4)]

for i in range(4):
    campo[i] = list(map(int,input().split()))
    
    
tentativa = int(input())

for i in range(tentativa):
    x, y = map(int,input().split())
    if campo[x-1][y-1] == 0:
        print(0)
    else:
        print(1)
    
