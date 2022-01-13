# -*- coding: utf-8 -*-
# Programa: quadrados_impares.py
# Programador: Fabio Batista Rodrigues
# Data: 28/04/2021
# Este programa lê dois números inteiros, num1 e num2,
# calcula e imprima os quadrados dos números ímpares
# maiores que o menor número e menores maior número. 
# A entrada é dada por dois números inteiros indicando 
# os números que definem o intervalo. A saída consiste 
# em imprimir os quadrados dos números ímpares maiores ou 
# iguais que o menor número e menores ou iguais ao maior número.
# Inicio do modulo principal.
# Descriçao das variaveis utilizadas
# int

# Passo 1. Leia a entrada
num1, num2 = map(int, input().split())
# Passo 2. Compute o menor eo maior numero. (troque se necessario)
if num1 > num2:
    num1, num2 = num2, num1
if num1 % 2 == 0:
    num1 = num1 + 1
if num2 % 2 == 0:
    num2 = num2 - 1
# Passo 2.1 Compute os quadrados dos números ímpares
for i in range(num1 + 2, num2, 2):
    quadrado = i*i
# Passo3 Imprima os quadrados dos números ímpares
    print(quadrado, end=' ')
# fim do modulo principal


