#Passo1. leia a entrada
palavra1, palavra2 = input('Leia duas palavras: ').split()

#Passo2. Compute a soma dos caracteres das duas palavras
tam1 = len(palavra1)
tam2 = len(palavra2)
soma = tam1 + tam2
#Passo3. Imprima o resultado
print(soma)