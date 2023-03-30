print("***** VERIFICAR A MÉDIA DO ALUNO *****")

def verificar(num):
    print(num)
    if(num >= 6):
        print("Aprovado com média= ", num)
    elif(num < 4.5):
        print("Reprovado= ", num)
    else:
        print("Recuperação: média= ", num)

meida = eval(input("Entre com a média do aluno: "))
verificar(meida)