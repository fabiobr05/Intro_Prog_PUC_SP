# -*- coding: utf-8 -*-
"""
Created on Thu May 27 16:18:52 2021

@author: Fabio Batista Rodrigues
"""

# Escreva um programa que leia os números dos produtos dos itens armazenados 
# no depósito em Campo Grande e armazene-os no arranjo CampoGrande, e então 
# repita este procedimento para os itens armazenados no depósito de Ponta Porã,
# armazenando esses números de produtos no arranjo PontaPorã. O programa deve 
# então encontrar e imprimir a união desses dois arranjos com as informações dos
# produtos de produtos, isto é, a coleção de números de produtos que estão em pelo
# menos um dos dois depósitos. Os elementos do arranjo da união devem aparecer 
# na mesma ordem que ocorrem nos arranjos, sendo que os da lista de Campo Grande
# aparecem antes dos da lista de Ponta Porã. Os estoques não devem ser assumidos
# como tendo o mesmo número de itens.

tam1 = int(input())
CampoGrande = list(map(int,input().split()))[:tam1]

tam2 = int(input())
PontaPorã = list(map(int,input().split()))[:tam2]

# Adicione os produtos na lista
tam = tam1 + tam2
NovaLista = []*tam
for i in range(0,tam1-1):
    NovaLista.append(CampoGrande[i])
for i in range(0,tam2-1):
    NovaLista.append(PontaPorã[i])

# Nao deu certo
# Varrer Lista Campo Grande e deletar duplicatas da de Ponta Porã
for i in range(tam1,tam2 -1):
    for j in range(0,tam1-1):
        if NovaLista[j] == NovaLista[i]:
            NovaLista.pop(11)
            
# Se a lista for vazia, devolver lista vazia
if tam1 == 0 and tam2 == 0:
    NovaLista = []



print(NovaLista)
    