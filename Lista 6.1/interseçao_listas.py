# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 19:35:01 2021

@author: Fabio Batista Rodrigues
"""
# Escreva um programa que leia os números dos produtos dos itens armazenados no
# depósito em Campo Grande e armazene-os no arranjo CampoGrande, e então repita
# este procedimento para os itens armazenados no depósito de Ponta Porã, 
# armazenando esses números de produtos no arranjo PontaPorã. O programa deve 
# então encontrar e imprimir a interseção desses dois arranjos com as 
# informações dos produtos de produtos, isto é, a coleção de números de produtos 
# que estão simultaneamente nos dois depósitos. Os elementos do arranjo da 
# interseção devem aparecer na mesma ordem que ocorrem nos arranjos (produtos 
# do depósito de Campo Grande).  Os estoques não devem ser assumidos como tendo
# o mesmo número de itens.

# Meu Jeito de Fazer o exercicio

tam1 = int(input())
lista1 = list(map(int, input().split()))[:tam1]

tam2 = int(input())
lista2 = list(map(int, input().split()))[:tam2]


novaLista = []
for i in range(0,tam1):
    for j in range(0,tam2):
        if lista1[i] == lista2[j]:
            novaLista.append(lista1[i])

if novaLista != []:
    print(novaLista)
else:
    print("[]")

"""
# Jeito do Professor de Fazer 

tam1 = int(input())
campogrande = list(map(int,input().split()))
tam2 = int(input())
pontapora = list(map(int,input().split()))

cgpp = []

for produto in campogrande:
    if produto in pontapora:
        cgpp.append(produto)
        
print(cgpp)

"""







