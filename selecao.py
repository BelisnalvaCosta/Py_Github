print("Algoritmo - ex. 01")

linha = input().split()
#Isto está formatado como código
A, B,C,D = list(map(int, linha))
if (B > C and D > A) and ((C + D) > (A + B)) and (C > 0 and D > 0) and (A%2 == 0):
    print("Valores aceitos")
else:
    print("Valores não aceito")  #Observação: só aceita estes números: 2326


print("** **\nAlgoritmo Ex. 02 - Pares, Ímpares, Positivos e Negativos **")
#OBS.: o int, faz uma conversão e eval é para avaliar as expressões
par = 0
impar = 0
positivo = 0
negativo = 0
for i in range(0, 5):
    x = int(input())
    if x%2 == 0:
        par += 1
    else:
        impar += 1
        if x > 0:
            positivo += 1
        elif x < 0:
            negativo += 1
print(par, "Valor(es) par(es)")
print(impar, "Valor(es) impar(es)")
print(positivo, "Valor(es) positivo(s)")
print(negativo, "Valor(es) negativo(s)")
