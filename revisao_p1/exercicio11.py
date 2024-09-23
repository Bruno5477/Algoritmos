numeros = [1, 30, 21, 2, 9, 65, 34, 8]

def soma_pares(lista:list):
    pares = [numero for numero in lista if numero % 2== 0]
    return sum(pares)


print(f"A soma dos números pares da lista é igual à: {soma_pares(numeros)}")