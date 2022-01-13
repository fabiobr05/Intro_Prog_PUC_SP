
#Entrada de dados com ';' como separador
#Tres variaveis inseridas
var1, var2, var3 = map(int,input().split(';'))
#Impressao de dados
#Impressao de 3 dados com 4 caracteres alinhados pela direita
print('Mostre os numeros {0:2d}  , {1:2d}  , {2:2d} '.format(var1, var2, var3))


number1, number2, number3 = map(float, input('Entre com 3 numeros: ').split(';'))

print('O numeros sao: {0:5.2f} , {1:5.2f} , {2:5.2f}'.format(number1,number2,number3))