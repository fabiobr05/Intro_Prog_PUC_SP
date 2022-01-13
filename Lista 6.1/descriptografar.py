# -*- coding: utf-8 -*-
"""
Created on Mon May 31 23:12:30 2021

@author: Fabio Batista Rodrigues
"""
#  Para esse exercício a frase a ser codificada será expressa com um conjunto 
# de caracteres do alfabeto, sem o caractere espaço, números, ou quaisquer sinais
# de pontuação ou caracteres especiais. Os caracteres maiúsculos ou minúsculos 
# da palavra codificadora serão considerados com o mesmo valor para a codificação
# (A = 1, a = 1, B = 2, b = 2, etc.). Para simplificar, a mensagem a ser 
# codificada será toda expressa em caracteres maiúsculos.
# Escreva um programa para implementar este método de codificação da palavra chave.
# Para cada mensagem e palavra codificadora da entrada o seu programa deve 
# computar a mensagem criptografada correspondente.

textoc = input()
palavra = input()
textoc = textoc.upper()
palavra = palavra.upper()

texto = ''
tam = len(palavra)

i = 0
for char in textoc:
    codigo = (ord(char) - ord('A')-(ord(palavra[i%tam])-ord('A')+1))%26+ord('A')
    texto = texto + chr(codigo)
    i += 1
    
print(texto)