# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 21:08:06 2021
Program: lista_telefonicaDicF.py
@author: Fabio Batista Rodrigues
"""
# Este programa lê um conjunto de tam nomes de um catálogo
# telefônico. Os nomes são dados pelo sobrenome, nome e número de
# telefone. O catálogo está ordenado pelo sobrenome. Após ler o
# catálogo, o programa lê um conjunto de num nomes (nome,
# sobrenome) e usando uma busca binária procura o nome de uma
# pessoa no catálogo. Se o nome foi encontrado, o programa
# imprime o nome, sobrenome e o telefone. Se o nome não for
# encontrado, o programa imprime o nome e o sobrenome e a
# mensagem informando que não tem telefone. O programa usa uma
# função busca() para procurar os telefones no catálogo.
# declaração das funções
def busca(nome, sobrenome, catalogo,tam):
     encontrou = False
# Passo 2.2.3. Inicialize o índice da busca
     i = 0
# Passo 2.2.4. Faça a busca de nome no catálogo
     while i < tam and not encontrou:
# Passo 2.2.6.1. Verifique se nome e sobrenome são iguais
         if catalogo[i]['sobrenome'] == sobrenome and catalogo[i]['nome'] == nome:
             pos = i
             encontrou = True
# Passo 2.2.6.2. Incremente o índice de busca
         i += 1
     if encontrou:
         msg = f"{catalogo[pos]['nome']} {catalogo[pos]['sobrenome']} {catalogo[pos]['telefone']}"
     else:
         msg = f'{nome} {sobrenome} não tem telefone'

     return msg
# início do módulo principal
# descrição das variáveis utilizadas
# list    catalogo[{}]
# list    chave[], dados[], nomes[]
# string  nome, numero
# bool    encontrou
# int     tam, num 

# pré: tam catalogo[0]..catalogo[tam-1]

# Passo 1. Leia a entrada e inicialize as variáveis
# Passo 1.1. Leia o tamanho do catálogo e inicialize as abstrações
tam = int(input())
chaves = ['sobrenome', 'nome', 'telefone']
catalogo = [dict.fromkeys(chaves) for i in range(tam)]
dados = []
# Passo 1.2. Leia os elementos do catálogo
for i in range(tam):
# Passo 1.3. Leia o número de buscas
    dados = list(map(str, input().split(', ')))
    catalogo[i]['sobrenome'] = dados[0]
    catalogo[i]['nome'] = dados[1]
    catalogo[i]['telefone'] = dados[2]
# Passo 1.4 Leia os num nomes da busca
num = int(input())
# Passo 2. Execute as num buscas
mensagem_retorno = ['']*num
i = 0
for j in range(num):
    nome, sobrenome = map(str, input().split())
# Passo 2.1 Recrutar a funçao para buscar na lista
    mensagem_retorno[i] =  busca(nome, sobrenome, catalogo, tam)
# Passo 2.2 Incremento da variavel contagem
    i += 1
# Passo 3. Imprima as respostas
for j in range(num):
    print(mensagem_retorno[j])  
   
# pós: for i in {0..num-1}:(catalogo[j] and nome ==
#      catalogo[i]['nome'] catalogo[i]['sobrenome'],
#      j em {0..tam-1}) or nome 'não tem telefone'
# fim do mpodulo principal