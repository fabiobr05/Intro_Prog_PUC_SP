# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:51:03 2021

@author: Fabio Batista Rodrigues
"""
# O seu programa programa deve ler um inteiro tamA, tamanho da lista que 
# representa a disciplina discA, a lista de inteiros com os tamA RGA´s dos 
# alunos matriculados na disciplina discA, um inteiro tamB, tamanho da lista da 
# disciplina discB, e a lista de inteiros com os tamB RGA´s dos alunos 
# matriculados na disciplina discB. O seu programa deve computar e imprimir a 
# lista intAB, com a interseção das matriculas das disciplinas discA e discB. 
# Caso não tenha nenhum aluno matriculado simultaneamente nas duas disciplinas, 
# o programa deve imprimir uma lista vazia.

tamA = int(input())

discA = list(map(int,input().split()))[:tamA]

tamB = int(input())

discB = list(map(int, input().split( )))[:tamB]

novaLista = []
for i in range(0,tamA):
    for j in range(0,tamB):
        if discA[i] == discB[j]:
            novaLista.append(discA[i])

print(novaLista)


# O jeito do professor esta na pasta " Lista 6.1"
