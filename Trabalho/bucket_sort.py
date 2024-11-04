
def insertion_sort(lista):
    
    n = len(lista)

    for i in range(1, n):
        
        element = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > element:
            
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = element
    
    return lista



def bucket_sort(arr):
    # Define o número de buckets
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Distribui os elementos entre os buckets
    for num in arr:
        index = int(num * n)  # Mapeia o valor ao índice do bucket
        buckets[index].append(num)

    # Ordena cada bucket individualmente
    for bucket in buckets:
        insertion_sort(bucket)  # Aqui usamos sort(), mas outros algoritmos podem ser usados

    # Concatena todos os buckets em uma lista ordenada
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

# Exemplo de uso
unsorted_list = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
sorted_list = bucket_sort(unsorted_list)
print("Array ordenado:", sorted_list)