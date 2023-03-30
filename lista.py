print("#Outro exemplo de Lista Multidimensionais")
print("Listas bidimensional\n")
def simetrica(m):
    nlinhas = len(m)
    ncolunas = len(m[0])
    for i in range(nlinhas):
        for j in range(i + 1, ncolunas):
            if m[i][j] != m[j][i]:
                return False
        return True

m = [[1, 2, 2],[4, 3, 2],[3, 5, 2]]
print("Simétrica", m)
print(simetrica(m))

print("##########")
print("Exemplo 2 - Lista, range percorrer de 0 a 10 ")
for x in range(10):
    print(x)
