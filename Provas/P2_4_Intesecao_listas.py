# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 20:39:02 2021

@author: Fabio Batista Rodrigues
"""
# Escreva um programa que leia os números dos produtos
# dos itens armazenados no depósito em Campo Grande e
# armazene-os no arranjo CampoGrande, e então repita
# este procedimento para os itens armazenados no depósito
# de Ponta Porã, armazenando esses números de produtos 
# no arranjo PontaPorã. O programa deve então encontrar
# e imprimir a interseção desses dois arranjos com as 
# informações dos produtos, isto é, a coleção de números
# de produtos que estão simultaneamente nos dois depósitos.
# Os elementos do arranjo da interseção devem aparecer na
# mesma ordem que ocorrem nos arranjos
# (produtos do depósito de Campo Grande).  Os estoques não
# devem ser assumidos como tendo o mesmo número de itens.

# Recer as duas lista
CampoGrande = list(map(int, input().split()))
tam1 = len(CampoGrande)
PontaPora = list(map(int, input().split()))
tam2 = len(PontaPora)

# Avaliar se há inteseçao
novaLista = []
for i in range(0,tam1):
    for j in range(0,tam2):
        if CampoGrande[i] == PontaPora[j]:
            novaLista.append(CampoGrande[i])

# Imprimir o resultado correspondente
if novaLista != []:
    print(novaLista)
else:
    print("[]")