# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 19:00:52 2021
Program: trocof.py
@author: Fabio Batista Rodrigues
"""
# Este programa que lê o valor de uma dada compra e o
# valor pago. O programa então calcula o troco, informando
# o valor em reais, e a quantidade de cada cédula e moeda
# que deve ser dado no troco. O programa deve utilizar
# funções para ler, calcular o troco e imprimir a número
# de cédulas e moedas do troco.

import math
# declaração de funções
# Função: calculatroco.py
# Esta função calcula o troco referente a um pagamento efetuado
# calculando o número de células e moedas do troco. A função
# utiliza o menor número de notas e moedas.
def calculatroco(comp, pag, troco):
# declaração das variáveis locais
# int trocoaux
# Passo ct1. Calcule o troco
   troco[0] = pag - comp
# Passo ct2. Converta o valordo troco para centavos
   trocoaux = math.trunc(100.0*troco[0]+0.5)
# Passo ct3. Calcule o numero de notas de 10
   troco[1] = trocoaux//1000  # 10,00 = 1000 centavos.
   trocoaux = trocoaux%1000   # resto do troco
# Passo ct4. Calcule o numero de notas de 5
   troco[2] = trocoaux//500   # 5,00 = 500 centavos.
   trocoaux = trocoaux%500    #resto do troco
# Passo ct5. Calcule o numero de notas de 2
   troco[3] = trocoaux//200    # 2,00 = 200 centavos.
   trocoaux = trocoaux%200    # resto do troco
# Passo cT6. Calcule o numero de moedas de 1
   troco[4] = trocoaux//100    # 1,00 = 100 centavos.
   trocoaux = trocoaux%100    # resto do troco
# Passo cT7. Calcule o numero de moedas de 50
   troco[5] = trocoaux//50
   trocoaux = trocoaux%50     # resto do troco
# Passo cT8. Calcule o numero de moedas de 25
   troco[6] = trocoaux//25
   trocoaux = trocoaux%25     # resto do troco
# Passo cT9. Calcule o numero de moedas de 10
   troco[7] = trocoaux//10
   trocoaux = trocoaux%10     # resto do troco
# Passo cT10. Calcule o numero de moedas de 5
   troco[8] = trocoaux//5
   trocoaux = trocoaux%5      # resto do troco
# Passo cT11. Calcule o numero de moedas de 1
   troco[9] = trocoaux
# Passo 1. Leia os valores da compra e do pagamento
compra, pagamento = map(float, input().split())
# Inicialize a variavel troco
troco = [0.00, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Passo 2. Calcule o troco
calculatroco(compra, pagamento, troco)
# Passo 3. Imprime os resultados
print('Valor do troco: R$ {0:5.2f}'.format(troco[0]))
print('{0:d} Nota     de R$ 10.00'.format(troco[1]))
print('{0:d} Nota     de R$  5.00'.format(troco[2]))
print('{0:d} Nota(s)  de R$  2.00'.format(troco[3]))
print('{0:d} Moeda    de R$  1.00'.format(troco[4]))
print('{0:d} Moeda    de R$  0.50'.format(troco[5]))
print('{0:d} Moeda    de R$  0.25'.format(troco[6]))
print('{0:d} Moeda(s) de R$  0.10'.format(troco[7]))
print('{0:d} Moeda    de R$  0.05'.format(troco[8]))
print('{0:d} Moeda    de R$  0.01'.format(troco[9]))

# pré: troco and número de cédulas e moedas do troco
# fim do módulo principal


