from random import sample
def media(numeros:list) -> float:
    soma = 0
    for numero in numeros:
        soma += numero

        return soma/len(numeros)


numeros = sample(range(1, 1000), 10)

resultado = media(numeros)

print(f"A média dos números da lista é {resultado}\n")