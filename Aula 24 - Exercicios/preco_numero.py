# -*- coding: utf-8 -*-
"""
Created on Thu May 27 14:10:44 2021

@author: Fabio Batista Rodrigues
"""
# Projete e implemente um programa que dado um número de produto, e usando uma 
# busca binária, procure e imprima o seu preço unitário de venda. O seu programa
# deve ler uma lista com todos os números e respectivos preços de todos os 
# produtos. Os dados devem ser armazenados em dois arranjos numero e preco,
# onde numero[0] e preco[0] armazenam o número e o preço, respectivamente, do 
# primeiro produto, numero[1] e preco[1] do segundo produto, e assim sucessivamente. 

# Entrada da quantidade de produtos comercializados
tamProduto = int(input())
# Lista ordenada dos tam numeros dos produtos
listaProd = list(map(int, input().split()))[:tamProduto]

# Lista de preços para os respectivos produtos
ListaPreco = list(map(float, input().split()))

# O numero do Produto associado a Lista Produto
Num = int(input())

condicao = False
# Varrendo a lista e atribuindo os valores correspondentes
for i in range(0,tamProduto):
    # Condiçao caso ache a lista
    if listaProd[i] == Num:
        condicao = True
        valor = ListaPreco[i]

# Imprima o resultado baseado na pesquisa
if condicao == True:
    print('{:.2f}'.format(valor))
else:
    print('produto inexistente')
    