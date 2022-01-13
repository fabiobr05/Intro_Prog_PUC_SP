
#Computador esta lendo como string
print('Soma de strings')
print('Entre com dois numeros separados por enter')
numero = input()
numero1 = input()
soma = numero + numero1
print(soma)

#Ler numeros inteiros e imprimir a soma
print('Soma de inteiros')
print('Entre com dois numeros separados por enter')
numero = int(input())
numero1 = int(input())
soma = numero + numero1
print(soma)

#Armazenar numero e ver que tipo de variavel
#esta la dentro
print('Entre com 3 numeros (separados por enter) e retornara com o tipo de variavel armazenado')
numero = input()
numero1 = int(input())
numero2 = float(input())
print(type(numero))
print(type(numero1))
print(type(numero2))

#Declaraçao e impressao com mensagem junto
print('Entrada com mensagem')
print('Entre com um numero')
numero = int(input('leia um numero inteiro: '))
print(type(numero))

#ler o numero1 e o numero2 com criterios (map)
#Entrada inteira e separado por espaço.
print('Entre com duas entradas separadas por espaços')
numero1, numero2 = map(int,input().split())
#Imprimir esses valores
print(numero1, numero2)

#outro exemplo com numeros separados por barra
print('Entre com uma data separada por barra ex. xx/xx/xx' )
dia,mes,ano = map(int,input('entre com a data: ').split('/'))
print(dia,mes,ano)

