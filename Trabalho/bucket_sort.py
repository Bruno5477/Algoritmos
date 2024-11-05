"""
Bucket Sort:
É um algoritmo de ordenação

Vantagens:


Desvantagens:


Passo a passo:


"""
from insertion_sort import insertion_sort

def bucket_sort(lista):
    # Definindo o número de buckets(baldes)
    n = len(lista)
    buckets = [[] for _ in range(n)]

    # Distribuindo os elementos entre os buckets
    for num in lista:
        # valor do índice do bucket
        index = int(num * n)  
        buckets[index].append(num)

    # Ordenando cada bucket individualmente usando o insertion sort
    for bucket in buckets:
        insertion_sort(bucket) 

    # Concatenando todos os buckets em uma lista ordenada
    
    lista_ordenada = []
    for bucket in buckets:
        lista_ordenada.extend(bucket)

    return lista_ordenada

# Exemplo de uso
lista = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
lista_ordenada = bucket_sort(lista)
print(f"\nLista não ordenada: {lista} \nLista ordenado: {lista_ordenada}\n")a