# -*- coding: utf-8 -*-
# Programa: biblioteca01l.py
# Programador:
# Data: 01/07/2020
# Este programa lê uma lista de n livros, onde cada livro tem 
# como informação o título, nome do autor e a prateleira onde ele 
# se encontra e outra lista, com m títulos de livros, dizer qual 
# é o nome do autor do livro e em qual prateleira os livros que 
# estão nessa segunda lista se encontram. Caso o livro que esteja 
# na segunda lista, não steja na primeira lista, ou seja, não 
# exista na biblioteca, imprimir apenas 'não encontrado'. A
# entrada é dada pelo titulo, autor e estante separados por
# vírgulas. O problema usa três listas para armazenar o acervo.
# descrição das variáveis utilizadas
# list    titulo, autor, estante, nomes
# string  livro, msg
# bool    achei
# int     tam, num

# pré: tam titulo[0] autor[0] estante[0] .. titulo[tam-1] autor[tam-1]

tam = int(input())
titulo = ['']*tam
autor = ['']*tam
estante = ['']*tam
for i in range(0,tam):
    titulo[i], autor[i], estante[i] = map(str, input().split(', '))
num = int(input())
for j in range(0,num):
    livro = input()
    encontrou = False
    msg = f'{livro} não encontrado'
    i = 0
    while i < tam and not encontrou:
        if livro == titulo[i]:
            msg = f'{autor[i]} {estante[i]}'
            encontrou = True
        i += 1
    print(msg)
    