# -*- coding: utf-8 -*-
# Programa: poluicao.py
# Programador: Fabio Batista Rodrigues
# Data: 28/04/2021
# Este programa lê quatro numeros inteiros
# A entrada por quatro inteiros indicando as 
# medidas de poluição. A saída consiste em imprimir
# para o conjunto das quatro de medidas de poluição
# uma mensagem apropriada indicando a condição da
# qualidade do ar na cidade.
# Inicio do modulo principal.
# Descriçao das variaveis utilizadas
# int

# Passo 1. Leia a entrada
olaria, Bolicho, Carixa, aleatorio = map(int, input().split())
# Passo 2. Calcule o indice de poluiçao 
indice = (olaria + Bolicho + Carixa + aleatorio) / 4.0
# Passo 2.1 Compute a mensagem apropriada
if indice < 50:
    msg = 'Qualidade do Ar Boa'
elif indice <= 100:
    msg = 'Qualidade do Ar Regular'
elif indice <= 200:
    msg = 'Qualidade do Ar Inadequada'
elif indice < 300:
    msg = 'Qualidade do Ar Ruim'
elif indice >= 300:
    msg = 'Qualidade do Ar Péssima'
# Passo 3. Imprima o resultado apropriado
print(msg)
# fim do modulo principal





