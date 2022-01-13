# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 13:58:18 2021
Program: contagem_suco_UFMS.py
@author: Fabio Batista Rodrigues
"""
# Seu trabalho agora é dado n <= 1000 sucos, computar quantas vezes o sabor
# de um dado suco foi vendido. Você também deve imprimir a relação dos sabores
# dos sucos e a quantidade vendida de cada uma. A relação dos sabores deve ser
# na ordem em que o sabor do suco aparece na lista da entrada. 


# PROGRAMA PRINCIPAL
#Leia o numero de livros no catalogo
n_sucos = int(input())
chaves = ['suco']
catalogo = [dict.fromkeys(chaves) for i in range(n_sucos)]
dados = []
# Leia os elementos do catalogo
for i in range(n_sucos):
    dados = input()
    catalogo[i]['suco'] = dados
# Computar quantos sucos foram pedidos de cada
msg =['']*n_sucos
for i in range(n_sucos):
    alvo = catalogo[i]['suco']
    contador = 0
    for j in range(n_sucos):
        if alvo == catalogo[j]['suco']:
            contador +=1
    msg[i] = f"{alvo} {contador}"

# Retirar as duplicatas do dicionario
new_msg = []
for num in msg:
    if num not in new_msg:
        new_msg.append(num)
# Calcule o tamanho da nova mensagem
tam_n_msg = len(new_msg)
# Passo 3. Imprima as respostas
for j in range(0, tam_n_msg):
    print(new_msg[j])


"""
Você, como todo acadêmico da nossa querida universidade, adora ir tomar aquele
 delicioso suco com seus amigos. Após chegar lá e pedir o seu suco, seu 
 espírito empreendedor aflora e você decide observar por 1 dia quais são 
 os sabores dos sucos mais vendidos na universidade para futuramente, abrir
 uma nova barraquinha e faturar milhões. A cada suco vendido você anota qual
 o sabor do suco vendido. Ao final do dia você tem uma lista com os sabores 
 dos n sucos vendidos no dia.  Seu trabalho agora é dado n <= 1000 sucos, 
 computar quantas vezes o sabor de um dado suco foi vendido. Você também deve
 imprimir a relação dos sabores dos sucos e a quantidade vendida de cada uma.
 A relação dos sabores deve ser na ordem em que o sabor do suco aparece na 
 lista da entrada. O programa deve ser implementado com a utilização de um 
 dicionário para armazenar as vendas dos sucos. A entrada por um número inteiro
 n que indica a quantidade de sucos vendidos num dado dia, seguido de n linhas,
 cada uma com uma string indicando o  sabor do suco vendido. A saída consiste 
 em escrever o nome do sabor de cada suco, sem repetição, e o número de quantos
 sucos daquele sabor foram vendidos no dia.

Exemplo
# formato da entrada

8

morango

laranja

mamao

laranja

uva

acerola

laranja

laranja

 

# formato da saída

morango 1

laranja 4

mamao 1

uva 1

acerola 1
"""