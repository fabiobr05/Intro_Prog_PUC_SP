# -*- coding: utf-8 -*-

# Programas: graus.py
# soma de duas medidas de um angulo
# descriçao das variaveis utilizadas
# int g1, mi, s1, g2, m2, s2

# Passo1. Leia as medidas
g1, m1, s1 = map(int, input().split())
g2, m2, s2 = map(int, input().split())
#Passo2. Calcule a soma
#Passo2.1. Calcule a soma dos segundos
totseg = s1 + s2
seg = totseg % 60
#Passo2.2. Calcule a soma dos minutos
totmin = m1 + m2 + totseg // 60
minu = totmin % 60
#Passo2.3. Calcule a soma dos graus
graus = g1 + g2 + totmin // 60
graus = graus % 360
# Passo 3. Imprima a soma
print('{0:3d} Graus {1:2d} Minutos {2:2d} Segundos +'.format(g1, m1, s1))
print('{0:3d} Graus {1:2d} Minutos {2:2d} Segundos ='.format(g2, m2, s2))
print('{0:3d} Graus {1:2d} Minutos {2:2d} Segundos'.format(graus,minu,seg))
