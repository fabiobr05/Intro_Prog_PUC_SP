# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 20:12:28 2021
program: lista_telefonica.py
@author: Fabio Batista Rodrigues
"""
# Projete e implemente um programa que leia o número num de assinantes
# (para testar o programa o número de assinantes será no máximo 1000), a
# seguir leia os dados dos num assinantes. Os dados dos num assinantes serão
# armazenados em uma lista de registros (dicionário), onde o registro 
# (dicionário) é composto por três strings. 
# A primeira string armazenará o sobrenome do assinante, a segunda o nome 
# e a terceira o numero do telefone. Para simplificar, não existem dois clientes
# com o mesmo nome e sobrenome. 

# Passo 1.0 Leia o numero de assinantes
tam = int(input())
sobrenome = [''] * tam
nome = ['']*tam
telefone = [''] * tam
# Passo 1.1 Leia as listas
for i in range(0,tam):
    sobrenome[i], nome[i], telefone[i] = map(str, input().split(', '))
# Passo 1.2 Leia o numero de consultas
tam1 = int(input())
# Passo 1.3 Receber a consulta do usuario
for j in range(0,tam1):
    pri_nome, sob_nome = map(str, input().split())
# Passo 3.0  Procurar na lista
    encontrou = False
    msg = f'{pri_nome} {sob_nome} não tem telefone'
    i = 0
    while i < tam and not encontrou:
        if sob_nome == sobrenome[i] and pri_nome == nome[i]:
            msg = f'{pri_nome} {sob_nome} {telefone[i]}'
            encontrou = True
        i += 1
    # Imprimir resposta adequada
    print(msg)
    