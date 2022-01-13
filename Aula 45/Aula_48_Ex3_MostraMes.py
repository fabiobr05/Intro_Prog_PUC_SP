# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 18:46:25 2021
# Program: mostrames.py
@author: Fabio Batists Rodrigues
"""
# Este Programa ilustra a passagem de uma string como refência.
# O programa lê um número entre um e 12 e usando uma função 
# def mostrames(mes)
# computa o mês (Janeiro a Dezembro) referente ao valor lido,
# retorna o mês para a função principal que imprime o resultado.
# funções
def mostrames(mes):
    
    meses = ['Janeiro','Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    if mes > 0 and mes <= 12:
        msg = meses[mes - 1]
    else:
        msg = 'Número inválido'

    return msg

# pré: mes

# início

# Passo 1. Leia o número do mês	
mes = int(input())
# Passo 2. Compute o mês equivalente
nome = mostrames(mes)
# Passo 3. Imprima o mês equivalnete
print(nome)

# fim

# pós: nome == (Janeiro || Fevereiro || ... || Dezembro) || Nome inválido

