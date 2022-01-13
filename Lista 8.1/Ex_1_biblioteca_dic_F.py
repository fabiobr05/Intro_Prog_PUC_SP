# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 13:27:50 2021
Program: biblioteca_dic_F.py
@author: Fabio Batista Rodrigues
"""
# Sua tarefa é, dado uma lista de n livros, onde cada livro tem como informação
# o nome de seu autor e a estante onde ele se encontra e outra lista, com m 
# nomes de livros, dizer qual é o nome do autor do livro e em qual prateleira 
# os livros que estão nessa segunda lista se encontram. Caso o livro que esteja
# na segunda lista, não esteja na primeira lista, ou seja, não exista na 
# biblioteca, imprimir o nome do livro com a mensagem "não encontrado".

# Função que busca o livro no acerto e retorna uma mensagem
def busca(livro, tam):
    
    encontrou = False
# Inicialize o índice da busca
    i = 0
# Faça a busca de nome no catálogo
    while i < tam and not encontrou:
# Verifique se o nome do livro é igual
        if catalogo[i]['livro'] == nome_livro:
            pos = i
            encontrou = True
# Incremente o índice de busca
        i += 1
# Atribua a mensagem adequada
    if encontrou:
        msg = f"{catalogo[pos]['Autor']} {catalogo[pos]['Estante']}"
    else:
        msg = f'{livro} não encontrado'
# Retorne a funçao
    return msg
# PROGRAMA PRINCIPAL
#Leia o numero de livros no catalogo
n_livros = int(input())
chaves = ['livro', 'Autor', 'Estante']
catalogo = [dict.fromkeys(chaves) for i in range(n_livros)]
dados = []
# Leia os elementos do catalogo
for i in range(n_livros):
    dados = list(map(str, input().split(', ')))
    catalogo[i]['livro'] = dados[0]
    catalogo[i]['Autor'] = dados[1]
    catalogo[i]['Estante'] = dados[2]
# Entre com o numero de buscas
n_buscas = int(input())
# Execute as n_buscas buscas
mensagem_retorno = ['']*n_buscas
i = 0
for j in range(n_buscas):
    nome_livro = str(input())
# Passo 2.1 Recrutar a funçao para buscar na lista
    mensagem_retorno[i] = busca(nome_livro, n_livros)
# Passo 2.2 Incremento da variavel contagem
    i += 1
# Passo 3. Imprima as respostas
for j in range(n_buscas):
    print(mensagem_retorno[j])  

"""
Problema:
 A Biblioteca da UFMS ficou sabendo da sua implementação impecável do sistema 
 telefônico, o LEDES tomou conhecimento do seu incrível software feito para o 
 sistema telefônico da UFMS e convidou-o para um estágio. Sua primeira tarefa é
 o de desenvolver um sistema para a Biblioteca Central da UFMS. Agora, sua 
 tarefa é, dado uma lista de n livros, onde cada livro tem como informação 
 o nome de seu autor e a estante onde ele se encontra e outra lista, com m 
 nomes de livros, dizer qual é o nome do autor do livro e em qual prateleira 
 os livros que estão nessa segunda lista se encontram. Caso o livro que esteja
 na segunda lista, não esteja na primeira lista, ou seja, não exista na
 biblioteca, imprimir o nome do livro com a mensagem "não encontrado". 
 A entrada é dada pelo arquivo biblioteca.in onde a primeira linha contém um 
 inteiro n indicando o número de livros, seguido dos n nomes de livros, nomes
 dos autores dos livros e as estantes onde os livros de encontram, após isso,
 um outro número inteiro m, indicando o número de livros da lista de buscas, 
 onde para os m livros dados, você deverá fazer uma busca para ver se o livro
 está no acervo e nesse caso imprimir o autor do livro, seguido da estante
 onde o livro se encontra. Caso o livro não esteja no acervo, escrever o nome
 do livro com a mensagem "não encontrado". A saída é dada pela impressão do 
 nome dos autores do livro e as prateleiras onde os livros se encontram, ou o
 nome do livro seguido da mensagem "não encontrado", caso o
 livro não exista na biblioteca.
 
 EXEMPLO
# formato da entrada (biblioteca.in)
5
Capitaes de Areia, Jorge Amado, 1
Helena, Machado de Assis, 1
Iracema, Jose de Alencar, 1
Memorias Inventadas, Manoel de Barros, 2
Cacau, Jorge Amado, 1
3
Alma Inquieta
Rio Vermelho
Capitaes de Areia

# formato da saída
Olavo Bilac 2
Rio Vermelho não encontrado
Jorge Amado 1
"""
