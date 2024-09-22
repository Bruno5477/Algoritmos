import random

numeros = random.sample(range(1, 100), 10)

def maior_menor (valores:list): 
    maior = max(valores)
    menor = min(valores)
    return [maior, menor]

resultado = maior_menor(numeros)

print(f"O maior valor da lista é {resultado[0]}\nO menor valor da lista é {resultado[1]}")