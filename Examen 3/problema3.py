# -----------------------------------------------
# Solución al problema 3
# -----------------------------------------------

# Lee el valor de n
n = int(input())

# Lee la matriz completa
a = [[int(j) for j in input().split()] for i in range(n)]

respuesta = 'SIPIRILI'
for ren in range(n):
    for col in range(n):
        if ren == col:
            if a[ren][col] != 1:
                respuesta = 'NONES'
        else:
            if a[ren][col] != 0:
                respuesta = 'NONES'
print(respuesta)

