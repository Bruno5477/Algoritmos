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


