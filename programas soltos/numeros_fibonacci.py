# -*- coding: utf-8 -*-
# Programa: fibonaci01.py
# Programador:
# Data: 16/09/2010
# Este programa recebe um inteiro positivo numero e calcula e imprime
# o número de termos da sequência de Fibonaci dos números menores ou 
# iguais a numero usando um algoritmo iterativo.
# início do módulo principal
# int numero, fib1, fib2, novofib, numtermos

# pré: numero > 0

# Passo 1. Leia um inteiro positivo
numero = int(input())
# Passo 2. Calcule e conte a sequência de Fibonaci de 1,1,.., num
# Passo 2.1. Inicialize a sequencia de Fibonaci
fib = 0
fib2 = 1
numtermos = -1
novofib = 0
# Passo 2.2. Enquanto o próximo número de Fibonacci for <= numero
while novofib <= numero:
# Passo 2.2.1. Conte o número de termos da sequência
    numtermos = numtermos + 1
# Passo 2.2.3. Calcule o próximo número na sequência    
    fib1 = fib2
    fib2 = novofib
    novofib = fib1 + fib2
# Passo 3. Imprima o número de termos
print('Num. de termos: {0:d}'.format(numtermos))

# pós: numtermos == num {fib_i <= numero} | fib_1 == 1 and fib_2 == 1 
#      and fib_i == fib_(i-2) + fib_(i-1)
# fim do módulo principal
