# -*- coding: utf-8 -*-
"""
Created on Thu May 27 16:03:59 2021

@author: Fabio Batista Rodrigues
"""

# Escreva um programa para verificar se um dado elemento pertence a uma lista 
# com no máximo 1000 inteiros. A entrada é dada por tam+2 linhas. A primeira 
# linha contém um número inteiro tam indicando o tamanho da lista. As tam linhas
# seguintes contêm os tam números inteiros, um em cada linha, representando a 
# lista e a última linha contém um número inteiro, representando o elemento com
# o qual efetuaremos a busca na lista para saber se ele pertence ou não a lista.
# A saída é dada por uma linha contendo uma mensagem 'sim' se o elemento pertence
# a lista e uma mensagem 'não' caso contrário.

# Entre com o tamanho da lista
tam = int(input())

# Laço para entrada de numero e armazenar na lista
i = 0
lista = []*tam
while i < tam:
# Entrada dos numeros
    numero = int(input())
# Acrescentar o numero ao final da lista
    lista.append(numero)
# Acrecentar o valor de i e varrer de novo
    i += 1

# Receber a busca do usuario
busca = int(input())

msg = 'não'
for i in range(0, tam):
# varrer a lista prcurando pela busca
    if lista[i] == busca:
        msg = 'Sim'

# Imprima a mensagem adequada
print(msg)
        
        
        
        