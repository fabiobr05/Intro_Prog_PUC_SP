# -*- coding: utf-8 -*-
# Programa: telefonistal.py
# Programador:
# Data: 20/11/2019
# Este programa lê um conjunto de tam nomes de um catálogo
# telefônico. Os nomes são dados pelo sobrenome, nome e número de
# telefone. O catálogo está ordenado pelo sobrenome. Após ler o
# catálogo, o programa lê um conjunto de num nomes (nome e
# sobrenome) de pessoas e efetua num buscas de pessoas no catálogo.
# Se o nome for encontrado, o programa imprime o nome, sobrenome e
# o telefone doo assinante. Se o nome não for encontrado, o
# programa imprime o nome e o sobrenome e a mensagem informando que
# a pessoa não tem telefone.
# início do módulo principal
# descrição das variáveis utilizadas
# list    sobrenome, nome, telefone
# list    nomes, dados
# string  pnome, snome
# bool    encontrou
# int     tam, num 

# pré: tam sobrenome[0] nome[0] telefone[0]..sobrenome[tam-1]
#      nome[tam-1] numero[tam-1] num nomes[0]..nomes[num-1]

# Leia o tamanho da lista
tam = int(input())
# Inicialize as listas
sobrenome = ['']*tam
nome = ['']*tam
telefone = ['']*tam
# Leia as listas
for i in range(0,tam):
    sobrenome[i], nome[i], telefone[i] = map(str, input().split(', '))
# Leia o numero de consultas
num = int(input())
# Faça as consultas
for j in range(0,num):
    pnome, snome = map(str, input().split())
# Procure na lista 
    encontrou = False
    msg = f'{pnome} {snome} não tem telefone'
    i = 0
    while i < tam and not encontrou:
        if snome == sobrenome[i] and pnome == nome[i]:
            msg = f'{pnome} {snome} {telefone[i]}'
            encontrou = True
        i += 1
    print(msg)
    
    
    
    
    
    
